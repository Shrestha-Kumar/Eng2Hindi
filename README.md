# English to Hindi Neural Machine Translation (Transformer)

This project implements an **English → Hindi Neural Machine Translation system**
using a **Transformer architecture built from scratch** (no torch.nn.Transformer).

## Model Architecture
- Encoder: Multi-Head Self-Attention + Feed Forward
- Decoder: Masked Self-Attention + Cross-Attention
- Positional Encoding (Sinusoidal)
- Number of Heads: 4
- Model Dimension: 256
- Feed Forward Dimension: 512
- Layers: 3

## Features
- Custom Transformer implementation
- Proper source and target masking
- Byte Pair Encoding (BPE) tokenization
- Mixed Precision Training (AMP)
- Gradient clipping for stability
- Learning rate scheduling

## Dataset
- English–Hindi parallel corpus
- Dataset and cleaned text files are **not included** due to size constraints

## Training
```bash
python final_code.py
```

If a trained model checkpoint already exists, it is loaded automatically.

## Inference Example

predict_sentence(
    "My father is a very good man",
    model,
    device,
    temperature=1.0,
    penalty=1.5
)

## Notes

Model checkpoints and datasets are excluded from version control

Designed to run on limited GPU memory (≈6GB)

Suitable for experimentation and educational purposes

## Author

Shrestha Kumar