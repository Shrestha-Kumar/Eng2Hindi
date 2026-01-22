import os
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

import math
import time
import random
import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import torch.nn.functional as F

from torch.utils.data import Dataset, DataLoader
from tokenizers import Tokenizer
from tqdm import tqdm

# ======================= DATA =======================

if not all([
    os.path.exists('cleaned_english_tr.txt'),
    os.path.exists('cleaned_hindi_tr.txt'),
    os.path.exists('cleaned_english_val.txt'),
    os.path.exists('cleaned_hindi_val.txt')
]):
    raise FileNotFoundError("Cleaned dataset files not found.")

train_en = pd.read_csv('cleaned_english_tr.txt', sep='^^', header=None, engine='python', quoting=3)
train_hi = pd.read_csv('cleaned_hindi_tr.txt', sep='^^', header=None, engine='python', quoting=3)
val_en = pd.read_csv('cleaned_english_val.txt', sep='^^', header=None, engine='python', quoting=3)
val_hi = pd.read_csv('cleaned_hindi_val.txt', sep='^^', header=None, engine='python', quoting=3)

train_en_list = train_en[1].to_list()
train_hi_list = train_hi[1].to_list()
val_en_list = val_en[1].to_list()
val_hi_list = val_hi[1].to_list()

# ======================= TOKENIZERS =======================

if not all([
    os.path.exists('tokenizer_en.json'),
    os.path.exists('tokenizer_hi.json')
]):
    raise FileNotFoundError("Tokenizer files not found.")

tokenizer_en = Tokenizer.from_file('tokenizer_en.json')
tokenizer_hi = Tokenizer.from_file('tokenizer_hi.json')

tokenizer_en.enable_padding(
    pad_id=tokenizer_en.token_to_id('[pad]'),
    pad_token='[pad]'
)
tokenizer_hi.enable_padding(
    pad_id=tokenizer_hi.token_to_id('[pad]'),
    pad_token='[pad]'
)

# ======================= DATALOADER =======================

class customDataset(Dataset):

    def __init__(self, src, trg):
        self.src = src
        self.trg = trg

    def __len__(self):
        return len(self.src)

    def __getitem__(self, index):
        return self.src[index], self.trg[index]


def collate_fn(batch):

    src = [x[0] for x in batch]
    trg = [x[1] for x in batch]

    src = tokenizer_en.encode_batch(src)
    trg = tokenizer_hi.encode_batch(trg)

    src = torch.LongTensor([enc.ids for enc in src])
    trg = torch.LongTensor([enc.ids for enc in trg])

    dec_input = trg[:, :-1]
    trg = trg[:, 1:]

    return src, dec_input, trg


train_dataloader = DataLoader(
    customDataset(train_en_list, train_hi_list),
    batch_size=60,
    shuffle=True,
    collate_fn=collate_fn
)

val_dataloader = DataLoader(
    customDataset(val_en_list, val_hi_list),
    batch_size=60,
    shuffle=False,
    collate_fn=collate_fn
)

# ======================= CONFIG =======================

n_heads = 4
d_model = 256
hidden_size = 512
p = 0.1
num_layers = 3
EPOCHS = 15
CLIP = 1

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# ======================= MODEL =======================

class PositionalEncoding(nn.Module):

    def __init__(self, d_model, p, max_len=5000):
        super().__init__()

        self.dropout = nn.Dropout(p)

        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len).unsqueeze(1)
        div_term = torch.exp(
            torch.arange(0, d_model, 2) * (-math.log(10000.0) / d_model)
        )

        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)

        pe = pe.unsqueeze(0)
        self.register_buffer('pe', pe)

    def forward(self, x):
        # x : [batch, src, emb_size]
        return self.dropout(x + self.pe[:, :x.size(1), :])


class feedForward(nn.Module):

    def __init__(self, d_model, hidden_size, p):
        super().__init__()
        self.fc1 = nn.Linear(d_model, hidden_size)
        self.fc2 = nn.Linear(hidden_size, d_model)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(p)

    def forward(self, x):
        return self.fc2(self.dropout(self.relu(self.fc1(x))))


class EncoderLayer(nn.Module):

    def __init__(self, d_model, n_heads, hidden_size, p):
        super().__init__()

        self.attention = nn.MultiheadAttention(d_model, n_heads, batch_first=True)
        self.norm1 = nn.LayerNorm(d_model)
        self.dropout1 = nn.Dropout(p)

        self.ff = feedForward(d_model, hidden_size, p)
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout2 = nn.Dropout(p)

    def forward(self, src, src_mask):

        # src: [batch, src, emb_size]
        attn_out, _ = self.attention(src, src, src, key_padding_mask=src_mask)
        src = self.norm1(src + self.dropout1(attn_out))

        ff_out = self.ff(src)
        src = self.norm2(src + self.dropout2(ff_out))

        return src


class Encoder(nn.Module):

    def __init__(self, input_size, d_model, n_heads, hidden_size, num_layers, p):
        super().__init__()

        self.d_model = d_model
        self.embedding = nn.Embedding(input_size, d_model)
        self.pe = PositionalEncoding(d_model, p)

        self.layers = nn.ModuleList([
            EncoderLayer(d_model, n_heads, hidden_size, p)
            for _ in range(num_layers)
        ])

    def forward(self, src, src_mask):

        # src: [batch, src]
        src = self.embedding(src) * math.sqrt(self.d_model)
        src = self.pe(src)

        for layer in self.layers:
            src = layer(src, src_mask)

        return src


class DecoderLayer(nn.Module):

    def __init__(self, d_model, n_heads, hidden_size, p):
        super().__init__()

        self.self_attn = nn.MultiheadAttention(d_model, n_heads, batch_first=True)
        self.norm1 = nn.LayerNorm(d_model)
        self.dropout1 = nn.Dropout(p)

        self.cross_attn = nn.MultiheadAttention(d_model, n_heads, batch_first=True)
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout2 = nn.Dropout(p)

        self.ff = feedForward(d_model, hidden_size, p)
        self.norm3 = nn.LayerNorm(d_model)
        self.dropout3 = nn.Dropout(p)

    def forward(self, trg, enc_out, trg_mask, src_mask):

        attn_out, _ = self.self_attn(trg, trg, trg, attn_mask=trg_mask)
        trg = self.norm1(trg + self.dropout1(attn_out))

        attn_out, _ = self.cross_attn(trg, enc_out, enc_out, key_padding_mask=src_mask)
        trg = self.norm2(trg + self.dropout2(attn_out))

        ff_out = self.ff(trg)
        trg = self.norm3(trg + self.dropout3(ff_out))

        return trg


class Decoder(nn.Module):

    def __init__(self, output_size, d_model, n_heads, hidden_size, num_layers, p):
        super().__init__()

        self.d_model = d_model
        self.embedding = nn.Embedding(output_size, d_model)
        self.pe = PositionalEncoding(d_model, p)

        self.layers = nn.ModuleList([
            DecoderLayer(d_model, n_heads, hidden_size, p)
            for _ in range(num_layers)
        ])

        self.fc_out = nn.Linear(d_model, output_size)

    def forward(self, trg, enc_out, trg_mask, src_mask):

        trg = self.embedding(trg) * math.sqrt(self.d_model)
        trg = self.pe(trg)

        for layer in self.layers:
            trg = layer(trg, enc_out, trg_mask, src_mask)

        return self.fc_out(trg)


class Transformer(nn.Module):

    def __init__(self, encoder, decoder, device):
        super().__init__()
        self.encoder = encoder
        self.decoder = decoder
        self.device = device

    def src_mask(self, src):
        return src == tokenizer_en.token_to_id('[pad]')

    def trg_mask(self, trg):
        return torch.triu(
            torch.ones(trg.size(1), trg.size(1), device=self.device) * float('-inf'),
            diagonal=1
        )

    def forward(self, src, dec_input):

        src_mask = self.src_mask(src)
        trg_mask = self.trg_mask(dec_input)

        enc_out = self.encoder(src, src_mask)
        return self.decoder(dec_input, enc_out, trg_mask, src_mask)

# ======================= TRAIN / LOAD =======================

encoder = Encoder(
    tokenizer_en.get_vocab_size(),
    d_model,
    n_heads,
    hidden_size,
    num_layers,
    p
).to(device)

decoder = Decoder(
    tokenizer_hi.get_vocab_size(),
    d_model,
    n_heads,
    hidden_size,
    num_layers,
    p
).to(device)

model = Transformer(encoder, decoder, device).to(device)

optimizer = optim.Adam(model.parameters(), lr=0.0005)
criterion = nn.CrossEntropyLoss(ignore_index=tokenizer_hi.token_to_id('[pad]'))
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, patience=2, factor=0.1)
scaler = torch.amp.GradScaler('cuda')

if os.path.exists('transformer_model.pt'):
    model.load_state_dict(torch.load('transformer_model.pt'))
else:
    best_valid_loss = float('inf')

    for epoch in range(EPOCHS):

        model.train()
        train_loss = 0

        loop = tqdm(train_dataloader, desc=f"Epoch {epoch+1}/{EPOCHS}")
        for src, dec_input, trg in loop:

            src, dec_input, trg = src.to(device), dec_input.to(device), trg.to(device)
            optimizer.zero_grad()

            with torch.amp.autocast('cuda'):
                output = model(src, dec_input)
                loss = criterion(
                    output.reshape(-1, output.shape[-1]),
                    trg.reshape(-1)
                )

            scaler.scale(loss).backward()
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), CLIP)
            scaler.step(optimizer)
            scaler.update()

            train_loss += loss.item()
            loop.set_postfix(loss=loss.item())

        model.eval()
        valid_loss = 0

        with torch.no_grad():
            for src, dec_input, trg in val_dataloader:
                src, dec_input, trg = src.to(device), dec_input.to(device), trg.to(device)
                output = model(src, dec_input)
                loss = criterion(
                    output.reshape(-1, output.shape[-1]),
                    trg.reshape(-1)
                )
                valid_loss += loss.item()

        valid_loss /= len(val_dataloader)

        if valid_loss < best_valid_loss:
            best_valid_loss = valid_loss
            torch.save(model.state_dict(), 'transformer_model.pt')

        scheduler.step(valid_loss)

# ======================= INFERENCE =======================

def predict_sentence(sentence, model, device, max_len=50, temperature=1.0, penalty=1.2):

    model.eval()

    src = torch.LongTensor(
        tokenizer_en.encode(sentence).ids
    ).unsqueeze(0).to(device)

    src_mask = model.src_mask(src)

    with torch.no_grad():
        enc_out = model.encoder(src, src_mask)

    sos = tokenizer_hi.token_to_id('[sos]')
    eos = tokenizer_hi.token_to_id('[eos]')

    trg = torch.LongTensor([[sos]]).to(device)
    generated = []

    for _ in range(max_len):
        trg_mask = model.trg_mask(trg)
        output = model.decoder(trg, enc_out, trg_mask, src_mask)
        logits = output[:, -1, :] / temperature
        probs = F.softmax(logits, dim=-1)

        token = probs.argmax(dim=-1).item()
        if token == eos:
            break

        generated.append(token)
        trg = torch.cat([trg, torch.LongTensor([[token]]).to(device)], dim=1)

    return tokenizer_hi.decode(generated)

print(predict_sentence("my father is a very good man", model, device))
