<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EN→HI Transformer NMT — README</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0a0a0f;
    --bg2: #111118;
    --bg3: #18181f;
    --bg4: #1e1e28;
    --border: #2a2a38;
    --border2: #3a3a4f;
    --text: #e8e8f0;
    --text2: #a0a0b8;
    --text3: #68687e;
    --accent: #7c6af7;
    --accent2: #a594f9;
    --accent-dim: rgba(124,106,247,0.12);
    --accent-glow: rgba(124,106,247,0.25);
    --green: #4ade80;
    --green-dim: rgba(74,222,128,0.1);
    --amber: #fbbf24;
    --amber-dim: rgba(251,191,36,0.1);
    --red: #f87171;
    --red-dim: rgba(248,113,113,0.1);
    --blue: #60a5fa;
    --blue-dim: rgba(96,165,250,0.1);
    --teal: #2dd4bf;
    --teal-dim: rgba(45,212,191,0.1);
    --mono: 'JetBrains Mono', monospace;
    --sans: 'Inter', sans-serif;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: var(--sans);
    font-size: 15px;
    line-height: 1.7;
    min-height: 100vh;
  }

  /* ── HERO ── */
  .hero {
    background: linear-gradient(135deg, #0a0a0f 0%, #12102a 50%, #0a0f1a 100%);
    border-bottom: 1px solid var(--border);
    padding: 72px 0 60px;
    position: relative;
    overflow: hidden;
  }
  .hero::before {
    content: '';
    position: absolute;
    top: -200px; left: 50%;
    transform: translateX(-50%);
    width: 700px; height: 700px;
    background: radial-gradient(circle, rgba(124,106,247,0.08) 0%, transparent 70%);
    pointer-events: none;
  }
  .hero-inner {
    max-width: 860px;
    margin: 0 auto;
    padding: 0 32px;
    position: relative;
  }
  .hero-tag {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-family: var(--mono);
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--accent2);
    background: var(--accent-dim);
    border: 1px solid rgba(124,106,247,0.3);
    border-radius: 20px;
    padding: 5px 14px;
    margin-bottom: 24px;
  }
  .hero-tag::before {
    content: '';
    width: 6px; height: 6px;
    border-radius: 50%;
    background: var(--accent2);
    box-shadow: 0 0 8px var(--accent2);
  }
  .hero h1 {
    font-size: 52px;
    font-weight: 700;
    letter-spacing: -0.03em;
    line-height: 1.08;
    margin-bottom: 20px;
    background: linear-gradient(135deg, #ffffff 0%, #a594f9 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  .hero h1 span {
    background: linear-gradient(90deg, var(--accent2), var(--teal));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  .hero-sub {
    font-size: 18px;
    color: var(--text2);
    max-width: 600px;
    line-height: 1.6;
    margin-bottom: 36px;
    font-weight: 300;
  }
  .hero-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }
  .badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 14px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 500;
    font-family: var(--mono);
    border: 1px solid;
  }
  .badge.purple { background: var(--accent-dim); color: var(--accent2); border-color: rgba(124,106,247,0.3); }
  .badge.green { background: var(--green-dim); color: var(--green); border-color: rgba(74,222,128,0.25); }
  .badge.amber { background: var(--amber-dim); color: var(--amber); border-color: rgba(251,191,36,0.25); }
  .badge.blue { background: var(--blue-dim); color: var(--blue); border-color: rgba(96,165,250,0.25); }
  .badge.teal { background: var(--teal-dim); color: var(--teal); border-color: rgba(45,212,191,0.25); }

  /* ── LAYOUT ── */
  .container {
    max-width: 860px;
    margin: 0 auto;
    padding: 0 32px;
  }

  /* ── NAV ── */
  .toc-bar {
    background: var(--bg2);
    border-bottom: 1px solid var(--border);
    position: sticky;
    top: 0;
    z-index: 100;
  }
  .toc-inner {
    max-width: 860px;
    margin: 0 auto;
    padding: 0 32px;
    display: flex;
    gap: 0;
    overflow-x: auto;
    scrollbar-width: none;
  }
  .toc-inner::-webkit-scrollbar { display: none; }
  .toc-link {
    display: block;
    padding: 14px 18px;
    font-size: 12.5px;
    font-weight: 500;
    color: var(--text3);
    text-decoration: none;
    white-space: nowrap;
    border-bottom: 2px solid transparent;
    transition: color 0.2s, border-color 0.2s;
    letter-spacing: 0.02em;
  }
  .toc-link:hover { color: var(--accent2); border-bottom-color: var(--accent2); }

  /* ── SECTIONS ── */
  section { padding: 64px 0; border-bottom: 1px solid var(--border); }
  section:last-of-type { border-bottom: none; }

  .section-eyebrow {
    font-family: var(--mono);
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 8px;
  }
  .section-title {
    font-size: 30px;
    font-weight: 700;
    letter-spacing: -0.02em;
    margin-bottom: 16px;
    color: var(--text);
  }
  .section-body {
    color: var(--text2);
    line-height: 1.8;
    font-size: 15px;
    max-width: 720px;
  }
  .section-body + * { margin-top: 36px; }
  p + p { margin-top: 12px; }

  /* ── CARDS GRID ── */
  .cards { display: grid; gap: 16px; margin-top: 32px; }
  .cards-2 { grid-template-columns: 1fr 1fr; }
  .cards-3 { grid-template-columns: 1fr 1fr 1fr; }
  @media (max-width: 640px) { .cards-2, .cards-3 { grid-template-columns: 1fr; } }

  .card {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 24px;
    transition: border-color 0.2s;
  }
  .card:hover { border-color: var(--border2); }
  .card-icon { font-size: 22px; margin-bottom: 14px; }
  .card-title { font-size: 14px; font-weight: 600; color: var(--text); margin-bottom: 8px; }
  .card-val { font-family: var(--mono); font-size: 28px; font-weight: 700; color: var(--accent2); margin-bottom: 6px; }
  .card-body { font-size: 13px; color: var(--text2); line-height: 1.6; }

  .stat-card {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px 24px;
  }
  .stat-label { font-size: 12px; color: var(--text3); font-family: var(--mono); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 8px; }
  .stat-value { font-size: 32px; font-weight: 700; font-family: var(--mono); }
  .stat-sub { font-size: 12px; color: var(--text2); margin-top: 4px; }
  .stat-green { color: var(--green); }
  .stat-amber { color: var(--amber); }
  .stat-accent { color: var(--accent2); }
  .stat-blue { color: var(--blue); }

  /* ── ARCH DIAGRAM ── */
  .arch-wrap {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 32px 24px;
    margin-top: 36px;
    overflow-x: auto;
  }
  .arch-wrap svg { display: block; margin: 0 auto; }

  /* ── CODE ── */
  pre {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 20px 24px;
    overflow-x: auto;
    font-family: var(--mono);
    font-size: 13px;
    line-height: 1.7;
    color: #cdd6f4;
    margin-top: 20px;
  }
  code { font-family: var(--mono); }
  .kw { color: #cba6f7; }
  .fn { color: #89b4fa; }
  .str { color: #a6e3a1; }
  .cm { color: var(--text3); font-style: italic; }
  .num { color: #fab387; }
  .op { color: #89dceb; }

  /* ── METRIC TABLE ── */
  .metric-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 28px;
    font-size: 14px;
  }
  .metric-table th {
    text-align: left;
    padding: 12px 16px;
    font-size: 11px;
    font-weight: 600;
    font-family: var(--mono);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--text3);
    border-bottom: 1px solid var(--border);
  }
  .metric-table td {
    padding: 14px 16px;
    border-bottom: 1px solid var(--border);
    vertical-align: top;
    color: var(--text2);
  }
  .metric-table tr:last-child td { border-bottom: none; }
  .metric-table td:first-child { color: var(--text); font-weight: 600; font-family: var(--mono); font-size: 13px; }
  .metric-table td .pill {
    display: inline-block;
    padding: 2px 10px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 600;
    margin-left: 6px;
    vertical-align: middle;
  }
  .pill-used { background: var(--green-dim); color: var(--green); border: 1px solid rgba(74,222,128,0.2); }
  .pill-better { background: var(--amber-dim); color: var(--amber); border: 1px solid rgba(251,191,36,0.2); }
  .pill-avoid { background: var(--red-dim); color: var(--red); border: 1px solid rgba(248,113,113,0.2); }

  /* ── TRAINING CURVE ── */
  .curve-wrap {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 24px;
    margin-top: 28px;
  }

  /* ── CALLOUT ── */
  .callout {
    border-left: 3px solid;
    padding: 16px 20px;
    border-radius: 0 8px 8px 0;
    margin-top: 20px;
    font-size: 14px;
  }
  .callout-info { border-color: var(--blue); background: var(--blue-dim); color: var(--text2); }
  .callout-warn { border-color: var(--amber); background: var(--amber-dim); color: var(--text2); }
  .callout-good { border-color: var(--green); background: var(--green-dim); color: var(--text2); }
  .callout strong { color: var(--text); }

  /* ── LOSS DETAIL ── */
  .loss-block {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 24px 28px;
    margin-top: 20px;
  }
  .loss-block h3 { font-size: 16px; font-weight: 600; margin-bottom: 10px; }
  .loss-block .formula {
    font-family: var(--mono);
    font-size: 13px;
    color: var(--accent2);
    background: var(--bg4);
    border: 1px solid var(--border);
    padding: 12px 16px;
    border-radius: 8px;
    margin: 12px 0;
    overflow-x: auto;
  }
  .loss-block p { color: var(--text2); font-size: 14px; line-height: 1.7; }
  .loss-block p + p { margin-top: 8px; }

  /* ── COMPARISON GRID ── */
  .compare-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-top: 28px;
  }
  @media (max-width: 640px) { .compare-grid { grid-template-columns: 1fr; } }
  .compare-card {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px 24px;
  }
  .compare-card.highlight { border-color: rgba(124,106,247,0.4); }
  .compare-card h4 { font-size: 14px; font-weight: 600; margin-bottom: 4px; }
  .compare-card .sub { font-size: 12px; color: var(--text3); margin-bottom: 12px; font-family: var(--mono); }
  .compare-card ul { list-style: none; padding: 0; }
  .compare-card ul li { font-size: 13px; color: var(--text2); padding: 4px 0; display: flex; align-items: flex-start; gap: 8px; }
  .compare-card ul li::before { content: '↳'; color: var(--accent); flex-shrink: 0; margin-top: 2px; }
  .compare-card ul li.pro::before { content: '✓'; color: var(--green); }
  .compare-card ul li.con::before { content: '✗'; color: var(--red); }

  /* ── DIVIDER ── */
  .divider { height: 1px; background: var(--border); margin: 32px 0; }

  /* ── FOOTER ── */
  footer {
    background: var(--bg2);
    border-top: 1px solid var(--border);
    padding: 40px 0;
    text-align: center;
    color: var(--text3);
    font-size: 13px;
  }
  footer strong { color: var(--text2); }

  /* ── STEP LIST ── */
  .steps { margin-top: 28px; display: flex; flex-direction: column; gap: 0; }
  .step { display: flex; gap: 20px; position: relative; }
  .step:not(:last-child)::before {
    content: '';
    position: absolute;
    left: 17px; top: 40px;
    width: 1px; height: calc(100% + 0px);
    background: var(--border);
  }
  .step-num {
    width: 36px; height: 36px;
    border-radius: 50%;
    background: var(--accent-dim);
    border: 1px solid rgba(124,106,247,0.3);
    color: var(--accent2);
    font-family: var(--mono);
    font-size: 13px;
    font-weight: 600;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-top: 2px;
  }
  .step-body { padding-bottom: 32px; }
  .step-body h4 { font-size: 15px; font-weight: 600; margin-bottom: 6px; line-height: 1.4; }
  .step-body p { font-size: 13.5px; color: var(--text2); line-height: 1.7; }

  /* ── INLINE CODE ── */
  .ic {
    font-family: var(--mono);
    font-size: 12.5px;
    background: var(--bg4);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 1px 6px;
    color: var(--accent2);
  }
</style>
</head>
<body>

<!-- ══════════════════════ HERO ══════════════════════ -->
<header class="hero">
  <div class="hero-inner">
    <div class="hero-tag">Neural Machine Translation</div>
    <h1>English <span>→ हिन्दी</span></h1>
    <p class="hero-sub">
      A from-scratch Transformer architecture for sequence-to-sequence translation, built without <code>torch.nn.Transformer</code> — every attention head, mask, and residual connection hand-coded in PyTorch.
    </p>
    <div class="hero-badges">
      <span class="badge purple">PyTorch · CUDA</span>
      <span class="badge green">d_model = 256</span>
      <span class="badge amber">4 attention heads</span>
      <span class="badge blue">3 encoder + 3 decoder layers</span>
      <span class="badge teal">BPE tokenization</span>
    </div>
  </div>
</header>

<!-- ══════════════════════ NAV ══════════════════════ -->
<nav class="toc-bar">
  <div class="toc-inner">
    <a href="#architecture" class="toc-link">Architecture</a>
    <a href="#metrics" class="toc-link">Metrics & Loss</a>
    <a href="#perplexity" class="toc-link">Why Perplexity</a>
    <a href="#training" class="toc-link">Training</a>
    <a href="#inference" class="toc-link">Inference</a>
    <a href="#better-metrics" class="toc-link">Better Metrics</a>
    <a href="#interview" class="toc-link">Interview Q&A</a>
    <a href="#quickstart" class="toc-link">Quickstart</a>
  </div>
</nav>

<!-- ══════════════════════ ARCHITECTURE ══════════════════════ -->
<section id="architecture">
  <div class="container">
    <div class="section-eyebrow">Model Design</div>
    <div class="section-title">Transformer Architecture</div>
    <p class="section-body">
      A faithful encoder-decoder Transformer. The encoder reads the English source with bidirectional self-attention. The decoder generates Hindi tokens autoregressively using masked self-attention and cross-attention over the encoder's output.
    </p>

    <!-- Arch SVG -->
    <div class="arch-wrap">
      <svg width="780" height="560" viewBox="0 0 780 560" xmlns="http://www.w3.org/2000/svg" style="font-family:'Inter',sans-serif">
        <defs>
          <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M2 1L8 5L2 9" fill="none" stroke="#7c6af7" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </marker>
          <marker id="arr2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M2 1L8 5L2 9" fill="none" stroke="#4ade80" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </marker>
          <marker id="arr3" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M2 1L8 5L2 9" fill="none" stroke="#60a5fa" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </marker>
        </defs>

        <!-- ENCODER column header -->
        <text x="165" y="28" text-anchor="middle" font-size="11" font-weight="600" fill="#7c6af7" letter-spacing="0.12em">ENCODER ×3</text>
        <!-- DECODER column header -->
        <text x="568" y="28" text-anchor="middle" font-size="11" font-weight="600" fill="#4ade80" letter-spacing="0.12em">DECODER ×3</text>

        <!-- Encoder box outline -->
        <rect x="30" y="36" width="270" height="432" rx="12" fill="rgba(124,106,247,0.05)" stroke="#2a2a50" stroke-width="1" stroke-dasharray="4,3"/>
        <!-- Decoder box outline -->
        <rect x="436" y="36" width="270" height="432" rx="12" fill="rgba(74,222,128,0.04)" stroke="#1a3020" stroke-width="1" stroke-dasharray="4,3"/>

        <!-- ─ ENCODER layers ─ -->
        <!-- Input Embedding + PE -->
        <rect x="55" y="448" width="220" height="36" rx="7" fill="#1a1830" stroke="#2d2a55" stroke-width="1"/>
        <text x="165" y="461" text-anchor="middle" font-size="11.5" font-weight="600" fill="#a594f9">Input Embedding</text>
        <text x="165" y="476" text-anchor="middle" font-size="10" fill="#6b688a">+ Sinusoidal Positional Encoding</text>

        <!-- Multi-Head Self-Attention (enc) -->
        <rect x="55" y="358" width="220" height="44" rx="7" fill="#1d1635" stroke="#3d3068" stroke-width="1"/>
        <text x="165" y="376" text-anchor="middle" font-size="12" font-weight="600" fill="#c4b5fd">Multi-Head Self-Attention</text>
        <text x="165" y="392" text-anchor="middle" font-size="10" fill="#7c6af7">Q = K = V = src  ·  4 heads  ·  d_k=64</text>

        <!-- Add & Norm 1 (enc) -->
        <rect x="55" y="314" width="220" height="28" rx="7" fill="#151520" stroke="#2a2a38" stroke-width="1"/>
        <text x="165" y="332" text-anchor="middle" font-size="11" fill="#68687e">Add &amp; Norm (LayerNorm)</text>

        <!-- Feed Forward (enc) -->
        <rect x="55" y="234" width="220" height="44" rx="7" fill="#1d1635" stroke="#3d3068" stroke-width="1"/>
        <text x="165" y="252" text-anchor="middle" font-size="12" font-weight="600" fill="#c4b5fd">Feed Forward Network</text>
        <text x="165" y="268" text-anchor="middle" font-size="10" fill="#7c6af7">Linear(256→512) · ReLU · Drop · Linear(512→256)</text>

        <!-- Add & Norm 2 (enc) -->
        <rect x="55" y="194" width="220" height="28" rx="7" fill="#151520" stroke="#2a2a38" stroke-width="1"/>
        <text x="165" y="212" text-anchor="middle" font-size="11" fill="#68687e">Add &amp; Norm (LayerNorm)</text>

        <!-- Encoder output label -->
        <rect x="95" y="100" width="140" height="28" rx="7" fill="#1a2f1a" stroke="#2a482a" stroke-width="1"/>
        <text x="165" y="118" text-anchor="middle" font-size="11" font-weight="600" fill="#4ade80">enc_out [B, S, 256]</text>

        <!-- Encoder arrows -->
        <line x1="165" y1="448" x2="165" y2="404" stroke="#7c6af7" stroke-width="1.2" marker-end="url(#arr)"/>
        <line x1="165" y1="358" x2="165" y2="344" stroke="#7c6af7" stroke-width="1.2" marker-end="url(#arr)"/>
        <line x1="165" y1="314" x2="165" y2="280" stroke="#7c6af7" stroke-width="1.2" marker-end="url(#arr)"/>
        <line x1="165" y1="234" x2="165" y2="224" stroke="#7c6af7" stroke-width="1.2" marker-end="url(#arr)"/>
        <line x1="165" y1="194" x2="165" y2="130" stroke="#7c6af7" stroke-width="1.2" marker-end="url(#arr)"/>

        <!-- Residual connections encoder -->
        <path d="M46 371 L36 371 L36 322 L54 322" fill="none" stroke="#3d2f7a" stroke-width="1" stroke-dasharray="3,2"/>
        <path d="M46 247 L36 247 L36 206 L54 206" fill="none" stroke="#3d2f7a" stroke-width="1" stroke-dasharray="3,2"/>
        <text x="20" y="350" font-size="9" fill="#3d2f7a" text-anchor="middle">+</text>
        <text x="20" y="226" font-size="9" fill="#3d2f7a" text-anchor="middle">+</text>

        <!-- Source tokens label -->
        <text x="165" y="510" text-anchor="middle" font-size="12" fill="#a0a0b8">English tokens</text>
        <text x="165" y="527" text-anchor="middle" font-size="11" fill="#68687e" font-family="'JetBrains Mono',monospace">"My father is a good man"</text>

        <!-- CROSS ATTENTION arrow (enc → dec) -->
        <path d="M275 114 Q360 114 436 250" fill="none" stroke="#4ade80" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#arr2)"/>
        <text x="355" y="164" text-anchor="middle" font-size="10" fill="#4ade80">enc_out → K, V</text>

        <!-- ─ DECODER layers ─ -->
        <!-- Output Embedding + PE -->
        <rect x="458" y="448" width="220" height="36" rx="7" fill="#0e2010" stroke="#1a3a1a" stroke-width="1"/>
        <text x="568" y="461" text-anchor="middle" font-size="11.5" font-weight="600" fill="#86efac">Output Embedding</text>
        <text x="568" y="476" text-anchor="middle" font-size="10" fill="#3d6840">+ Sinusoidal Positional Encoding</text>

        <!-- Masked Self-Attention (dec) -->
        <rect x="458" y="370" width="220" height="44" rx="7" fill="#0e2010" stroke="#2a5530" stroke-width="1"/>
        <text x="568" y="386" text-anchor="middle" font-size="12" font-weight="600" fill="#86efac">Masked Self-Attention</text>
        <text x="568" y="402" text-anchor="middle" font-size="10" fill="#4ade80">Causal mask · Q = K = V = trg</text>

        <!-- Add & Norm dec1 -->
        <rect x="458" y="328" width="220" height="26" rx="7" fill="#151520" stroke="#2a2a38" stroke-width="1"/>
        <text x="568" y="345" text-anchor="middle" font-size="11" fill="#68687e">Add &amp; Norm (LayerNorm)</text>

        <!-- Cross Attention (dec) -->
        <rect x="458" y="268" width="220" height="44" rx="7" fill="#0e2010" stroke="#2a5530" stroke-width="1"/>
        <text x="568" y="284" text-anchor="middle" font-size="12" font-weight="600" fill="#86efac">Cross-Attention</text>
        <text x="568" y="300" text-anchor="middle" font-size="10" fill="#4ade80">Q = decoder · K = V = enc_out</text>

        <!-- Add & Norm dec2 -->
        <rect x="458" y="228" width="220" height="26" rx="7" fill="#151520" stroke="#2a2a38" stroke-width="1"/>
        <text x="568" y="244" text-anchor="middle" font-size="11" fill="#68687e">Add &amp; Norm (LayerNorm)</text>

        <!-- FFN decoder -->
        <rect x="458" y="162" width="220" height="44" rx="7" fill="#0e2010" stroke="#2a5530" stroke-width="1"/>
        <text x="568" y="178" text-anchor="middle" font-size="12" font-weight="600" fill="#86efac">Feed Forward Network</text>
        <text x="568" y="194" text-anchor="middle" font-size="10" fill="#4ade80">Linear(256→512) · ReLU · Drop · Linear(512→256)</text>

        <!-- Add & Norm dec3 -->
        <rect x="458" y="122" width="220" height="26" rx="7" fill="#151520" stroke="#2a2a38" stroke-width="1"/>
        <text x="568" y="138" text-anchor="middle" font-size="11" fill="#68687e">Add &amp; Norm (LayerNorm)</text>

        <!-- Linear + Softmax -->
        <rect x="458" y="62" width="220" height="44" rx="7" fill="#0a2420" stroke="#1a504a" stroke-width="1"/>
        <text x="568" y="78" text-anchor="middle" font-size="12" font-weight="600" fill="#2dd4bf">Linear Projection</text>
        <text x="568" y="94" text-anchor="middle" font-size="10" fill="#5eead4">256 → vocab_size_hi · Softmax</text>

        <!-- Decoder arrows -->
        <line x1="568" y1="448" x2="568" y2="416" stroke="#4ade80" stroke-width="1.2" marker-end="url(#arr2)"/>
        <line x1="568" y1="370" x2="568" y2="356" stroke="#4ade80" stroke-width="1.2" marker-end="url(#arr2)"/>
        <line x1="568" y1="328" x2="568" y2="314" stroke="#4ade80" stroke-width="1.2" marker-end="url(#arr2)"/>
        <line x1="568" y1="268" x2="568" y2="256" stroke="#4ade80" stroke-width="1.2" marker-end="url(#arr2)"/>
        <line x1="568" y1="228" x2="568" y2="208" stroke="#4ade80" stroke-width="1.2" marker-end="url(#arr2)"/>
        <line x1="568" y1="162" x2="568" y2="150" stroke="#4ade80" stroke-width="1.2" marker-end="url(#arr2)"/>
        <line x1="568" y1="122" x2="568" y2="108" stroke="#4ade80" stroke-width="1.2" marker-end="url(#arr2)"/>

        <!-- Residual dec -->
        <path d="M686 383 L700 383 L700 338 L679 338" fill="none" stroke="#1a4a24" stroke-width="1" stroke-dasharray="3,2"/>
        <path d="M686 281 L700 281 L700 238 L679 238" fill="none" stroke="#1a4a24" stroke-width="1" stroke-dasharray="3,2"/>
        <path d="M686 175 L700 175 L700 136 L679 136" fill="none" stroke="#1a4a24" stroke-width="1" stroke-dasharray="3,2"/>

        <!-- Target tokens label -->
        <text x="568" y="510" text-anchor="middle" font-size="12" fill="#a0a0b8">Hindi tokens (shifted right)</text>
        <text x="568" y="527" text-anchor="middle" font-size="11" fill="#68687e" font-family="'JetBrains Mono',monospace">[SOS] मेरे पिताजी ...</text>

        <!-- Output label -->
        <text x="568" y="40" text-anchor="middle" font-size="12" font-weight="600" fill="#2dd4bf">▶ मेरे पिताजी एक बहुत अच्छे आदमी हैं</text>
      </svg>
    </div>

    <!-- Config stats -->
    <div class="cards cards-3" style="margin-top:28px">
      <div class="stat-card">
        <div class="stat-label">d_model</div>
        <div class="stat-value stat-accent">256</div>
        <div class="stat-sub">Embedding dimension</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">FFN hidden</div>
        <div class="stat-value stat-accent">512</div>
        <div class="stat-sub">2× expansion ratio</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Heads × Layers</div>
        <div class="stat-value stat-accent">4 × 3</div>
        <div class="stat-sub">d_k = d_v = 64 per head</div>
      </div>
    </div>

    <div class="callout callout-info" style="margin-top:24px">
      <strong>Attention math:</strong> Each head computes
      <span class="ic">Attention(Q,K,V) = softmax(QKᵀ / √d_k) · V</span>
      where d_k = 256/4 = 64. The <code>√d_k</code> scaling prevents vanishingly small gradients from sharp softmax outputs.
    </div>
  </div>
</section>

<!-- ══════════════════════ METRICS & LOSS ══════════════════════ -->
<section id="metrics">
  <div class="container">
    <div class="section-eyebrow">Training Objective</div>
    <div class="section-title">Metrics &amp; Loss Function</div>
    <p class="section-body">
      The model is trained with padded cross-entropy loss and evaluated using perplexity (PPL). These two are mathematically linked — understanding the relationship is critical for interpretation.
    </p>

    <!-- Loss block -->
    <div class="loss-block">
      <h3 style="color: var(--accent2)">Loss: Cross-Entropy with Padding Ignore</h3>
      <div class="formula">
        L = −(1/N) · Σᵢ log P(yᵢ | y&lt;i , x)
        <br>where N = number of non-padding tokens
      </div>
      <p>The model outputs a logit vector of shape <span class="ic">[B × T, vocab_size_hi]</span>. The criterion computes log-softmax and measures the negative log probability of the correct Hindi token at each position. Padding tokens are excluded via <span class="ic">ignore_index=tokenizer_hi.token_to_id('[pad]')</span> — this is essential for fair comparison across batches with variable-length sequences.</p>
      <p style="margin-top:10px">PyTorch's <span class="ic">nn.CrossEntropyLoss</span> combines LogSoftmax + NLLLoss in a numerically stable way using the log-sum-exp trick, avoiding floating-point underflow when probabilities are very small.</p>
    </div>

    <!-- Perplexity block -->
    <div class="loss-block" style="margin-top:16px; border-color: rgba(74,222,128,0.2);">
      <h3 style="color: var(--green)">Metric: Perplexity (PPL)</h3>
      <div class="formula" style="color: var(--green)">
        PPL = exp(L)  =  exp(cross-entropy loss)
      </div>
      <p>Perplexity is a measure of how "surprised" the model is by the next token on average. A PPL of <strong style="color:var(--text)">K</strong> means the model is as uncertain as if choosing uniformly from K equally likely tokens. Lower is always better. If the model perfectly predicted every token, PPL = 1.</p>
      <p style="margin-top:10px"><strong style="color:var(--text)">The code computes it directly:</strong> <span class="ic">math.exp(train_loss)</span> and <span class="ic">math.exp(valid_loss)</span> are printed every epoch alongside the raw loss.</p>
    </div>

    <!-- Full metrics table -->
    <table class="metric-table" style="margin-top:32px">
      <thead>
        <tr>
          <th>Metric</th>
          <th>What it measures</th>
          <th>Range</th>
          <th>Status in this project</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Cross-Entropy Loss <span class="pill pill-used">used ✓</span></td>
          <td>Log probability of correct token. Training objective directly optimised by Adam.</td>
          <td>0 → ∞, lower better</td>
          <td>Train &amp; validation loss logged every epoch. Checkpointing on best val loss.</td>
        </tr>
        <tr>
          <td>Perplexity (PPL) <span class="pill pill-used">used ✓</span></td>
          <td>Geometric mean inverse probability. exp(loss). Human-interpretable scale of model confusion.</td>
          <td>1 → ∞, lower better</td>
          <td>Computed as <span class="ic">math.exp(loss)</span> and printed every epoch.</td>
        </tr>
        <tr>
          <td>BLEU Score <span class="pill pill-better">best practice</span></td>
          <td>N-gram precision overlap between prediction and reference translation. Industry standard for NMT.</td>
          <td>0–100, higher better</td>
          <td>Not implemented. Should be added on the test set post-training.</td>
        </tr>
        <tr>
          <td>METEOR <span class="pill pill-better">better than BLEU</span></td>
          <td>Accounts for synonyms, morphological variants, word order. Better for morphologically rich languages like Hindi.</td>
          <td>0–1, higher better</td>
          <td>Not implemented. Strongly recommended for Hindi evaluation.</td>
        </tr>
        <tr>
          <td>chrF / chrF++ <span class="pill pill-better">best for Hindi</span></td>
          <td>Character-level F-score. Works at the character n-gram level — far more robust for Devanagari script.</td>
          <td>0–100, higher better</td>
          <td>Not implemented. Ideal for Hindi given script complexity.</td>
        </tr>
        <tr>
          <td>Token Accuracy <span class="pill pill-avoid">avoid</span></td>
          <td>Fraction of tokens predicted correctly. Dominated by frequent/simple tokens, misleadingly inflated.</td>
          <td>0–100%</td>
          <td>Not used. Inappropriate for sequence generation tasks.</td>
        </tr>
        <tr>
          <td>BERTScore <span class="pill pill-better">semantic</span></td>
          <td>Contextual embedding cosine similarity between hypothesis and reference. Captures semantic correctness.</td>
          <td>0–1, higher better</td>
          <td>Not implemented. Requires a Hindi-capable BERT model (e.g. MuRIL).</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<!-- ══════════════════════ WHY PERPLEXITY ══════════════════════ -->
<section id="perplexity">
  <div class="container">
    <div class="section-eyebrow">Metric Deep Dive</div>
    <div class="section-title">Why Perplexity — Not Accuracy</div>
    <p class="section-body">
      Token-level accuracy is one of the worst choices for a language model. Understanding why reveals something deep about how generative models are evaluated.
    </p>

    <div class="compare-grid">
      <div class="compare-card highlight">
        <h4 style="color:var(--accent2)">Perplexity (PPL)</h4>
        <div class="sub">exp(cross-entropy) — what we use</div>
        <ul>
          <li class="pro">Directly linked to the training loss — no mismatch</li>
          <li class="pro">Penalises every bit of uncertainty, not just wrong argmax</li>
          <li class="pro">Interpretable: PPL=50 means model "chooses" among ~50 tokens</li>
          <li class="pro">Sensitive to calibration — a confident wrong guess is punished hard</li>
          <li class="pro">Standard in NMT, LM, and speech research</li>
        </ul>
      </div>
      <div class="compare-card">
        <h4 style="color:var(--red)">Token Accuracy</h4>
        <div class="sub">argmax == gold — what we avoid</div>
        <ul>
          <li class="con">Ignores probability mass — 51% confident = same as 99%</li>
          <li class="con">Misleadingly high: common tokens ("[pad]", "है", "का") dominate</li>
          <li class="con">A model that outputs "है" every step may hit 40%+ accuracy</li>
          <li class="con">Doesn't reflect translation quality at all</li>
          <li class="con">Not differentiable — can't use as a training signal</li>
        </ul>
      </div>
    </div>

    <div class="callout callout-warn" style="margin-top:24px">
      <strong>The core problem with accuracy in NMT:</strong> Translation has many valid outputs. "मेरे पिताजी" and "मेरे पिता" are both correct translations of "my father." Accuracy would penalise one even though both are right. Perplexity at least reflects confidence in whatever the model chose.
    </div>

    <!-- PPL intuition visual -->
    <div class="curve-wrap">
      <div style="margin-bottom:16px; font-size:13px; color:var(--text2); font-weight:500">
        📊 Perplexity intuition — what PPL values mean in practice
      </div>
      <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:12px;text-align:center">
        <div>
          <div style="font-family:var(--mono);font-size:22px;font-weight:700;color:#f87171">1000+</div>
          <div style="font-size:11px;color:var(--text3);margin-top:4px">Random model<br>Untrained</div>
        </div>
        <div>
          <div style="font-family:var(--mono);font-size:22px;font-weight:700;color:#fbbf24">200–500</div>
          <div style="font-size:11px;color:var(--text3);margin-top:4px">Early training<br>epochs 1–3</div>
        </div>
        <div>
          <div style="font-family:var(--mono);font-size:22px;font-weight:700;color:#60a5fa">50–200</div>
          <div style="font-size:11px;color:var(--text3);margin-top:4px">Mid training<br>learning structure</div>
        </div>
        <div>
          <div style="font-family:var(--mono);font-size:22px;font-weight:700;color:#4ade80">15–50</div>
          <div style="font-size:11px;color:var(--text3);margin-top:4px">Good model<br>this project's range</div>
        </div>
        <div>
          <div style="font-family:var(--mono);font-size:22px;font-weight:700;color:#a594f9">&lt;15</div>
          <div style="font-size:11px;color:var(--text3);margin-top:4px">Excellent<br>Large data/params</div>
        </div>
      </div>
      <div style="margin-top:16px;height:6px;border-radius:3px;background:linear-gradient(90deg,#f87171,#fbbf24,#60a5fa,#4ade80,#a594f9)"></div>
      <div style="display:flex;justify-content:space-between;margin-top:6px;font-size:10px;color:var(--text3);font-family:var(--mono)">
        <span>WORSE</span><span>BETTER →</span>
      </div>
    </div>
  </div>
</section>

<!-- ══════════════════════ TRAINING ══════════════════════ -->
<section id="training">
  <div class="container">
    <div class="section-eyebrow">Training Pipeline</div>
    <div class="section-title">Training Setup &amp; Tricks</div>
    <p class="section-body">Several engineering decisions make this model train stably on ≈6GB GPU memory.</p>

    <div class="cards cards-2" style="margin-top:32px">
      <div class="card">
        <div class="card-icon">⚡</div>
        <div class="card-title">Mixed Precision (AMP)</div>
        <div class="card-body"><span class="ic">torch.amp.autocast('cuda')</span> runs forward pass in float16 (half the memory, faster matmuls on Tensor Cores). <span class="ic">GradScaler</span> scales the loss before backward to prevent float16 gradient underflow, then unscales before gradient clipping.</div>
      </div>
      <div class="card">
        <div class="card-icon">✂️</div>
        <div class="card-title">Gradient Clipping (clip=1)</div>
        <div class="card-body">Transformers are prone to gradient explosions especially early in training when attention weights are near-uniform. <span class="ic">clip_grad_norm_(model.parameters(), 1.0)</span> rescales the global gradient norm if it exceeds 1, preventing parameter updates from becoming catastrophically large.</div>
      </div>
      <div class="card">
        <div class="card-icon">📉</div>
        <div class="card-title">LR Scheduler: ReduceLROnPlateau</div>
        <div class="card-body">Monitors validation loss. If it doesn't improve for <span class="ic">patience=2</span> epochs, the learning rate is multiplied by <span class="ic">factor=0.1</span>. This anneals learning to fine-tune details once the model has learned coarse structure. Initial LR: 0.0005.</div>
      </div>
      <div class="card">
        <div class="card-icon">🎯</div>
        <div class="card-title">Best-Checkpoint Saving</div>
        <div class="card-body">Only saves <span class="ic">transformer_model.pt</span> when validation loss strictly improves. Prevents saving an overfit model from a later epoch. Automatically reloaded on next run, supporting resumable training.</div>
      </div>
      <div class="card">
        <div class="card-icon">🔤</div>
        <div class="card-title">BPE Tokenization</div>
        <div class="card-body">Byte Pair Encoding splits rare words into sub-word units. Handles out-of-vocabulary Hindi words gracefully (e.g. named entities, inflected verb forms). Separate tokenizers for English and Hindi ensure language-specific vocabularies.</div>
      </div>
      <div class="card">
        <div class="card-icon">🎲</div>
        <div class="card-title">Dropout (p=0.1)</div>
        <div class="card-body">Applied after every sub-layer: attention output, FFN intermediate, and positional encoding. Prevents the model from co-adapting neurons, acting as a strong regulariser. Disabled automatically during <span class="ic">model.eval()</span>.</div>
      </div>
    </div>

    <div class="callout callout-info" style="margin-top:28px">
      <strong>Optimizer:</strong> Adam with β₁=0.9, β₂=0.999, ε=1e-8 (PyTorch defaults). Adam's adaptive per-parameter learning rates are well-suited to Transformers where different weight matrices need very different update magnitudes.
    </div>

    <!-- Training pseudocode -->
    <pre>
<span class="cm"># Training loop (simplified from notebook)</span>
<span class="kw">for</span> epoch <span class="kw">in</span> <span class="fn">range</span>(<span class="num">15</span>):
    <span class="cm"># Forward pass with AMP</span>
    <span class="kw">with</span> torch.amp.<span class="fn">autocast</span>(<span class="str">'cuda'</span>):
        output = <span class="fn">model</span>(src, dec_input)           <span class="cm"># [B, T, vocab_hi]</span>
        output = output.<span class="fn">reshape</span>(-<span class="num">1</span>, vocab_size)   <span class="cm"># [B*T, vocab_hi]</span>
        loss = <span class="fn">criterion</span>(output, trg_label)       <span class="cm"># cross-entropy, pad ignored</span>

    <span class="cm"># Scaled backward + unscale + clip + step</span>
    scaler.<span class="fn">scale</span>(loss).<span class="fn">backward</span>()
    scaler.<span class="fn">unscale_</span>(optimizer)
    nn.utils.<span class="fn">clip_grad_norm_</span>(model.<span class="fn">parameters</span>(), <span class="num">1.0</span>)
    scaler.<span class="fn">step</span>(optimizer)
    scaler.<span class="fn">update</span>()

    <span class="cm"># Perplexity = exp(cross-entropy loss)</span>
    ppl = math.<span class="fn">exp</span>(valid_loss)
    scheduler.<span class="fn">step</span>(valid_loss)  <span class="cm"># reduce LR if no improvement</span></pre>
  </div>
</section>

<!-- ══════════════════════ INFERENCE ══════════════════════ -->
<section id="inference">
  <div class="container">
    <div class="section-eyebrow">Generation</div>
    <div class="section-title">Autoregressive Inference</div>
    <p class="section-body">At inference, the decoder generates tokens one at a time. Two decoding parameters control output quality.</p>

    <div class="steps">
      <div class="step">
        <div class="step-num">1</div>
        <div class="step-body">
          <h4>Encode the English source</h4>
          <p>Tokenize the input sentence with the English BPE tokenizer. Pass through the encoder once to get <span class="ic">enc_out [1, S, 256]</span>. This is computed only once and reused at every decoder step — efficient.</p>
        </div>
      </div>
      <div class="step">
        <div class="step-num">2</div>
        <div class="step-body">
          <h4>Prime the decoder with [SOS]</h4>
          <p>Initialise the decoder input tensor with a single <span class="ic">[SOS]</span> (start-of-sequence) token. This tells the decoder to begin generation.</p>
        </div>
      </div>
      <div class="step">
        <div class="step-num">3</div>
        <div class="step-body">
          <h4>Autoregressive loop (max 50 steps)</h4>
          <p>At each step: run the decoder with the growing token sequence → get logits for the last position <span class="ic">[1, vocab_hi]</span> → apply repetition penalty → apply temperature scaling → softmax → argmax. Append the new token and repeat.</p>
        </div>
      </div>
      <div class="step">
        <div class="step-num">4</div>
        <div class="step-body">
          <h4>Repetition penalty (default 1.2–1.5)</h4>
          <p>For every token already generated, if its logit is positive it is divided by the penalty factor; if negative, it is multiplied. This discourages the model from looping — a common failure mode in small Transformers. Higher penalty = more diverse output, but can reduce fluency.</p>
        </div>
      </div>
      <div class="step">
        <div class="step-num">5</div>
        <div class="step-body">
          <h4>Temperature scaling</h4>
          <p>Divide all logits by temperature before softmax. <span class="ic">temp=1.0</span> = standard distribution. <span class="ic">temp&lt;1</span> = sharper, more deterministic. <span class="ic">temp&gt;1</span> = flatter, more random. We use greedy decoding (argmax) after this, so temperature only affects the penalty scoring step here.</p>
        </div>
      </div>
      <div class="step">
        <div class="step-num">6</div>
        <div class="step-body">
          <h4>Stop on [EOS] or max_len</h4>
          <p>If the model predicts the end-of-sequence token, decoding stops immediately. Otherwise it continues until max_len=50 tokens.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ══════════════════════ BETTER METRICS ══════════════════════ -->
<section id="better-metrics">
  <div class="container">
    <div class="section-eyebrow">What's Next</div>
    <div class="section-title">Better Metrics &amp; Improvements</div>
    <p class="section-body">
      PPL tells you how confident the model is. It doesn't tell you if the translations are actually good. Here's what you'd add to make evaluation production-grade.
    </p>

    <div class="cards cards-2" style="margin-top:32px">
      <div class="card" style="border-color:rgba(74,222,128,0.25)">
        <div class="card-icon">📐</div>
        <div class="card-title" style="color:var(--green)">BLEU (Bilingual Evaluation Understudy)</div>
        <div class="card-body">
          Precision of 1–4 grams in the hypothesis against references, with a brevity penalty. The baseline metric for MT papers since 2002. Use <span class="ic">sacrebleu</span> for standardised computation.
          <br><br><em style="color:var(--text3)">Limitation: doesn't handle synonyms or paraphrases well.</em>
        </div>
      </div>
      <div class="card" style="border-color:rgba(45,212,191,0.25)">
        <div class="card-icon">🔤</div>
        <div class="card-title" style="color:var(--teal)">chrF / chrF++ (for Hindi)</div>
        <div class="card-body">
          Character-level F-score. Devanagari script has many morphological variations — character n-grams capture these better than word n-grams. chrF++ also includes word n-grams. Strongly recommended for any Indic script translation.
          <br><br><em style="color:var(--text3)">Best choice for this specific language pair.</em>
        </div>
      </div>
      <div class="card" style="border-color:rgba(251,191,36,0.25)">
        <div class="card-icon">🌟</div>
        <div class="card-title" style="color:var(--amber)">METEOR</div>
        <div class="card-body">
          Matches via exact tokens, stems, synonyms, and paraphrases. Aligns words between hypothesis and reference, then computes F-score with a fragmentation penalty. Correlates better with human judgement than BLEU at sentence level.
        </div>
      </div>
      <div class="card" style="border-color:rgba(96,165,250,0.25)">
        <div class="card-icon">🧠</div>
        <div class="card-title" style="color:var(--blue)">BERTScore</div>
        <div class="card-body">
          Computes contextual token embeddings for hypothesis and reference using a pretrained BERT model, then measures cosine similarity. Captures semantic equivalence that surface-form metrics miss entirely.
          <br><br><em style="color:var(--text3)">Needs a multilingual/Hindi BERT (MuRIL, IndicBERT).</em>
        </div>
      </div>
    </div>

    <div class="callout callout-good" style="margin-top:24px">
      <strong>Beam search over greedy decoding:</strong> This project uses greedy argmax inference. Beam search (keeping top-k hypotheses at each step) typically improves BLEU by 3–8 points at the cost of beam_size× compute. It would be the single highest-impact inference improvement to add.
    </div>

    <!-- Additional improvements -->
    <div style="margin-top:32px">
      <h3 style="font-size:17px;font-weight:600;margin-bottom:16px;color:var(--text)">Architecture improvements worth exploring</h3>
      <table class="metric-table">
        <thead><tr><th>Improvement</th><th>Expected Impact</th></tr></thead>
        <tbody>
          <tr><td>Label Smoothing (ε=0.1)</td><td>Prevents the model from becoming overconfident. Regularises the output distribution by assigning a small probability ε/(V-1) to non-gold tokens. Very common in NMT — usually adds 0.5–1 BLEU.</td></tr>
          <tr><td>Warmup LR schedule (Transformer paper)</td><td>Linear warmup for warmup_steps then inverse-square-root decay. Helps early gradient flow before the attention learns meaningful patterns. The original paper used 4000 warmup steps.</td></tr>
          <tr><td>Larger d_model (512) + more layers (6)</td><td>The original "Transformer Base" uses d_model=512, 8 heads, 6 layers. Would increase parameter count ~4× at the cost of requiring more VRAM and longer training.</td></tr>
          <tr><td>Pre-layer normalisation</td><td>This implementation uses post-LN (the original). Pre-LN (norm applied before sublayer) is more stable and allows training without warmup. Used in most modern Transformers.</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<!-- ══════════════════════ INTERVIEW Q&A ══════════════════════ -->
<section id="interview">
  <div class="container">
    <div class="section-eyebrow">Interview Prep</div>
    <div class="section-title">Questions &amp; Answers</div>
    <p class="section-body">The questions an ML interviewer will ask about this project, answered precisely from the code.</p>

    <div style="margin-top:32px;display:flex;flex-direction:column;gap:20px">

      <div class="loss-block">
        <h3 style="color:var(--accent2)">Q: Why use cross-entropy loss and not MSE?</h3>
        <p>MSE on one-hot targets doesn't make probabilistic sense — a prediction of 0.4 is not "twice as bad" as 0.2 in a meaningful way for classification. Cross-entropy is the proper negative log-likelihood for a categorical distribution. It's directly the KL-divergence between the true distribution and the model's predicted distribution (minus a constant entropy term). Minimising CE is equivalent to maximising the log-likelihood of the correct translation token.</p>
      </div>

      <div class="loss-block">
        <h3 style="color:var(--accent2)">Q: Why is padding ignored in the loss?</h3>
        <p>Batches contain sequences of different lengths, padded to the maximum length. If we included padding tokens in the loss, the model would be penalised for not predicting <span class="ic">[PAD]</span> tokens even though they carry no linguistic information — and it would learn that predicting <span class="ic">[PAD]</span> is a cheap way to reduce loss on longer sequences. <span class="ic">ignore_index</span> masks these positions so the gradient flows only through real tokens.</p>
      </div>

      <div class="loss-block">
        <h3 style="color:var(--accent2)">Q: What does the causal mask do in the decoder?</h3>
        <p>During training we feed the entire target sequence shifted right (teacher forcing). Without a mask, position i could attend to all future positions j > i, meaning the model would "cheat" by looking ahead at tokens it should be predicting. The upper-triangular mask (filled with −∞, yielding 0 after softmax) ensures token i can only attend to tokens 0 through i. At inference, this is naturally enforced because we generate one token at a time.</p>
        <div class="formula">mask[i,j] = −∞  if  j &gt; i,  else  0</div>
      </div>

      <div class="loss-block">
        <h3 style="color:var(--accent2)">Q: Why do we scale embeddings by √d_model?</h3>
        <p>The word embedding vectors are initialised with small values (roughly unit variance). The positional encoding values, however, are bounded between −1 and 1 (sin/cos). Without scaling, the PE values would dominate the embedding signal, especially for large d_model. Multiplying embeddings by <span class="ic">√256 = 16</span> brings them to a comparable magnitude, letting the model combine both signals more effectively.</p>
      </div>

      <div class="loss-block">
        <h3 style="color:var(--accent2)">Q: Why does gradient clipping help Transformers specifically?</h3>
        <p>Attention weights are computed as softmax(QKᵀ/√d_k). Early in training, these are near-uniform. A single batch with an unusually sharp attention pattern can produce a gradient spike. The depth of the network (3 encoder + 3 decoder layers + residuals) means these spikes multiply through many weight matrices. Clipping the global gradient norm to 1 ensures the parameter update never exceeds a fixed magnitude, regardless of batch content.</p>
      </div>

      <div class="loss-block">
        <h3 style="color:var(--accent2)">Q: What's the difference between perplexity on train vs. val?</h3>
        <p>Train PPL measures how well the model has fit the training distribution. Val PPL measures generalisation. A large gap (low train PPL, high val PPL) indicates overfitting — the model has memorised training sentences rather than learning translation patterns. We checkpoint on val loss, not train loss, precisely to select the best-generalising model, not the most-overfit one.</p>
      </div>

    </div>
  </div>
</section>

<!-- ══════════════════════ QUICKSTART ══════════════════════ -->
<section id="quickstart">
  <div class="container">
    <div class="section-eyebrow">Usage</div>
    <div class="section-title">Quickstart</div>

    <div class="cards cards-2" style="margin-top:28px">
      <div class="stat-card">
        <div class="stat-label">Batch size</div>
        <div class="stat-value stat-accent">60</div>
        <div class="stat-sub">Tuned for ≈6GB VRAM + AMP</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Max epochs</div>
        <div class="stat-value stat-green">15</div>
        <div class="stat-sub">Early stop via val loss plateau</div>
      </div>
    </div>

    <pre>
<span class="cm"># Install dependencies</span>
pip install torch tokenizers pandas tqdm

<span class="cm"># Files expected in working directory</span>
<span class="cm"># cleaned_english_tr.txt   cleaned_hindi_tr.txt</span>
<span class="cm"># cleaned_english_val.txt  cleaned_hindi_val.txt</span>
<span class="cm"># tokenizer_en.json        tokenizer_hi.json</span>

<span class="cm"># Run training (resumes from checkpoint if present)</span>
jupyter nbconvert --to script transformer.ipynb
python transformer.py

<span class="cm"># Translate a sentence (after training)</span>
predict_sentence(
    <span class="str">"My father is a very good man"</span>,
    model, device,
    temperature=<span class="num">1.0</span>,
    penalty=<span class="num">1.5</span>
)</pre>

    <div class="callout callout-info" style="margin-top:20px">
      <strong>CUDA memory note:</strong> <span class="ic">PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True</span> is set at the top of the notebook. This prevents CUDA from pre-allocating fixed-size blocks and reduces fragmentation — important when training with AMP on limited VRAM.
    </div>
  </div>
</section>

<!-- ══════════════════════ FOOTER ══════════════════════ -->
<footer>
  <div class="container">
    <p style="margin-bottom:8px">
      Built with <strong>PyTorch</strong> · <strong>BPE Tokenizers</strong> · <strong>AMP</strong> · from scratch
    </p>
    <p style="font-size:12px">Author: <strong>Shrestha Kumar</strong> · English → Hindi Neural Machine Translation</p>
    <p style="font-size:11px;margin-top:12px;color:var(--text3)">d_model=256 · 4 heads · 3 layers · FFN=512 · dropout=0.1 · Adam lr=5e-4</p>
  </div>
</footer>

</body>
</html>
