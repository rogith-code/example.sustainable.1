import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# ──────────────────────────────────────────────────────────
# PAGE CONFIG
# ──────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Ethos Invest · Sustainable Portfolio Tool",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ──────────────────────────────────────────────────────────
# GLOBAL CSS
# ──────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,300;0,14..32,400;0,14..32,500;0,14..32,600;0,14..32,700;1,14..32,400&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --bg:       #0e1014;
    --bg-alt:   #0b0d11;
    --panel:    #13161c;
    --panel2:   #161920;
    --line:     rgba(255,255,255,0.07);
    --line2:    rgba(255,255,255,0.04);
    --text:     #e7eaf0;
    --muted:    #8b93a3;
    --faint:    #525a69;
    --green:    #52c98a;
    --green-dk: #1f6b42;
    --blue:     #3b82f6;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background: var(--bg);
    color: var(--text);
}

.stApp {
    background:
        radial-gradient(ellipse 60% 40% at 0% 0%, rgba(82,201,138,0.07), transparent),
        radial-gradient(ellipse 40% 30% at 100% 0%, rgba(59,130,246,0.06), transparent),
        var(--bg);
}

#MainMenu, footer, header { visibility: hidden; }

.block-container {
    padding-top: 1.4rem;
    padding-bottom: 3rem;
    max-width: 1380px;
}

/* ══ HERO ════════════════════════════════════════════════ */
.hero {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: linear-gradient(135deg,
        rgba(82,201,138,0.09) 0%,
        rgba(59,130,246,0.05) 60%,
        transparent 100%);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 22px;
    padding: 26px 32px;
    margin-bottom: 8px;
    box-shadow: 0 16px 48px rgba(0,0,0,0.28),
                0 0 0 0.5px rgba(255,255,255,0.04) inset;
}
.hero-left h1 {
    font-size: 2rem;
    font-weight: 700;
    letter-spacing: -0.045em;
    margin: 0 0 6px;
    color: #f5f7fb;
    line-height: 1.1;
}
.hero-left p {
    margin: 0;
    color: var(--muted);
    font-size: 0.94rem;
    line-height: 1.5;
    max-width: 520px;
}
.hero-pills {
    display: flex;
    gap: 8px;
    margin-top: 14px;
    flex-wrap: wrap;
}
.pill {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 5px 11px;
    border-radius: 999px;
    border: 1px solid rgba(82,201,138,0.2);
    background: rgba(82,201,138,0.07);
    color: #a8dfc0;
    font-size: 11px;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 0.04em;
}
.hero-right {
    text-align: right;
    flex-shrink: 0;
}
.hero-stat-row {
    display: flex;
    gap: 20px;
    justify-content: flex-end;
}
.hero-stat {
    text-align: center;
}
.hero-stat-val {
    font-family: 'JetBrains Mono', monospace;
    font-size: 22px;
    font-weight: 600;
    color: var(--green);
    line-height: 1;
}
.hero-stat-lbl {
    font-size: 10px;
    color: var(--faint);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-top: 4px;
}

/* ══ SECTION LABELS ══════════════════════════════════════ */
.section-label {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 32px 0 16px;
}
.section-label-bar {
    width: 3px;
    height: 18px;
    background: linear-gradient(180deg, var(--green), var(--green-dk));
    border-radius: 999px;
    flex-shrink: 0;
}
.section-label-text {
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.12em;
    color: var(--green);
    text-transform: uppercase;
}
.section-label-rule {
    flex: 1;
    height: 1px;
    background: var(--line2);
}

/* ══ CARDS ═══════════════════════════════════════════════ */
.card {
    background: var(--panel);
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 20px 22px 18px;
    margin-bottom: 14px;
    box-shadow: 0 1px 2px rgba(0,0,0,0.4),
                0 20px 48px rgba(0,0,0,0.14);
    position: relative;
    overflow: hidden;
}
.card-title {
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--green);
    margin-bottom: 14px;
    padding-bottom: 10px;
    border-bottom: 1px solid var(--line2);
}
.card-subtitle {
    font-size: 12px;
    color: var(--muted);
    margin-top: 8px;
    line-height: 1.55;
}
.card-field-label {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.06em;
    color: var(--faint);
    text-transform: uppercase;
    margin-bottom: 4px;
    margin-top: 10px;
}

/* ══ METRIC TILES ════════════════════════════════════════ */
.metric-tile {
    background: var(--panel);
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 18px 20px 16px;
    margin-bottom: 12px;
    box-shadow: 0 1px 2px rgba(0,0,0,0.4);
    position: relative;
    overflow: hidden;
}
.metric-tile::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--green-dk), var(--green), transparent);
}
.metric-tile .label {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--faint) !important;
    margin-bottom: 10px;
}
.metric-tile .value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 30px;
    font-weight: 600;
    color: var(--text) !important;
    letter-spacing: -0.03em;
    line-height: 1;
}
.metric-tile .sub {
    font-size: 11px;
    color: var(--faint) !important;
    margin-top: 8px;
    font-family: 'JetBrains Mono', monospace;
}

/* ══ ALLOCATION BARS ══════════════════════════════════════ */
.bar-row { margin-bottom: 12px; }
.bar-label-row {
    display: flex;
    justify-content: space-between;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 7px;
    font-family: 'JetBrains Mono', monospace;
}
.bar-track {
    height: 7px;
    background: rgba(255,255,255,0.06);
    border-radius: 999px;
    overflow: hidden;
}
.bar-fill {
    height: 7px;
    border-radius: 999px;
}

/* ══ COMPARISON TABLE ════════════════════════════════════ */
.cmp-wrap {
    background: var(--panel);
    border: 1px solid var(--line);
    border-radius: 18px;
    overflow: hidden;
    box-shadow: 0 1px 2px rgba(0,0,0,0.4), 0 20px 48px rgba(0,0,0,0.14);
}
.cmp-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 12.5px;
    font-family: 'JetBrains Mono', monospace;
}
.cmp-table th {
    padding: 13px 18px;
    text-align: left;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    border-bottom: 1px solid rgba(82,201,138,0.18);
    background: rgba(255,255,255,0.015);
}
.cmp-table th:first-child { color: var(--muted); }
.cmp-table th.col-esg     { color: var(--green); background: rgba(82,201,138,0.06); }
.cmp-table th.col-other   { color: var(--muted); }
.cmp-table td {
    padding: 11px 18px;
    border-bottom: 1px solid var(--line2);
    color: #c0c5d0;
}
.cmp-table td.col-esg {
    color: var(--green) !important;
    font-weight: 600;
    background: rgba(82,201,138,0.04);
    border-left: 2px solid rgba(82,201,138,0.25);
}
.cmp-table tr:last-child td { border-bottom: none; }
.cmp-table tr:hover td { background: rgba(255,255,255,0.02); }
.cmp-table tr:hover td.col-esg { background: rgba(82,201,138,0.07); }
.cmp-table td:first-child { color: var(--muted); font-weight: 500; }

/* ══ CHIPS ═══════════════════════════════════════════════ */
.chip {
    display: inline-block;
    padding: 5px 14px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 0.02em;
}
.chip-pos { background: rgba(82,201,138,0.12); color: #52c98a !important; border: 1px solid rgba(82,201,138,0.22); }
.chip-neg { background: rgba(224,90,90,0.12);  color: #e05a5a !important; border: 1px solid rgba(224,90,90,0.22); }
.chip-neu { background: rgba(255,255,255,0.05);color: #7a8090 !important; border: 1px solid rgba(255,255,255,0.10); }

/* ══ DIVIDERS ════════════════════════════════════════════ */
hr.fancy-divider {
    border: none;
    height: 1px;
    background: var(--line2);
    margin: 32px 0;
}

/* ══ INFO / WARN ═════════════════════════════════════════ */
.info-box {
    background: rgba(82,201,138,0.05);
    border: 1px solid rgba(82,201,138,0.14);
    border-left: 3px solid var(--green);
    padding: 14px 18px;
    border-radius: 0 14px 14px 0;
    color: #b9e7ce !important;
    font-size: 13px;
    line-height: 1.55;
    margin: 12px 0;
}
.warn-box {
    background: rgba(220,170,60,0.05);
    border: 1px solid rgba(220,170,60,0.14);
    border-left: 3px solid #dcaa3c;
    padding: 14px 18px;
    border-radius: 0 14px 14px 0;
    color: #e5c57b !important;
    font-size: 13px;
    line-height: 1.55;
    margin: 12px 0;
}

/* ══ RESULTS BAND ════════════════════════════════════════ */
.results-band {
    background: var(--bg-alt);
    border-top: 1px solid var(--line2);
    border-bottom: 1px solid var(--line2);
    margin: 0 -3rem;
    padding: 0 3rem;
}

/* ══ INPUTS ══════════════════════════════════════════════ */
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input,
[data-baseweb="select"] > div,
[data-baseweb="textarea"] textarea {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(255,255,255,0.09) !important;
    border-radius: 10px !important;
    color: #eef2f7 !important;
    font-size: 13px !important;
    transition: border-color 0.15s ease, box-shadow 0.15s ease;
}
[data-testid="stTextInput"] input:hover,
[data-testid="stNumberInput"] input:hover {
    border-color: rgba(82,201,138,0.3) !important;
}
[data-testid="stTextInput"] input:focus,
[data-testid="stNumberInput"] input:focus,
[data-baseweb="select"]:focus-within {
    border-color: rgba(82,201,138,0.45) !important;
    box-shadow: 0 0 0 2px rgba(82,201,138,0.12) !important;
}

/* ══ CALCULATE BUTTON ════════════════════════════════════ */
.cta-wrap .stButton > button {
    background: linear-gradient(135deg, #1a5c38 0%, #24884f 100%) !important;
    border: 1px solid rgba(82,201,138,0.22) !important;
    border-radius: 14px !important;
    color: #e2f5eb !important;
    font-size: 14px !important;
    font-weight: 700 !important;
    letter-spacing: 0.05em;
    padding: 0.85rem 2rem !important;
    width: 100%;
    box-shadow: 0 8px 28px rgba(33,122,74,0.22),
                0 0 0 0.5px rgba(82,201,138,0.14) inset;
    transition: all 0.2s ease;
}
.cta-wrap .stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 14px 32px rgba(33,122,74,0.30) !important;
    background: linear-gradient(135deg, #1f6e43 0%, #299457 100%) !important;
}

/* ══ PROFILE BADGE ═══════════════════════════════════════ */
.profile-badge {
    background: rgba(82,201,138,0.08);
    border: 1px solid rgba(82,201,138,0.18);
    border-radius: 14px;
    padding: 14px 18px;
    text-align: center;
    margin-top: 8px;
}
.profile-badge .pname {
    font-size: 17px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 4px;
}
.profile-badge .pnote {
    font-size: 12px;
    color: var(--muted);
    line-height: 1.5;
}

/* ══ HELPER TEXT ═════════════════════════════════════════ */
.helper { font-size: 12px; color: var(--muted); line-height: 1.55; }
</style>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────
# CORE LOGIC
# ──────────────────────────────────────────────────────────
def portfolio_return(w1, r1, r2):
    return w1 * r1 + (1 - w1) * r2

def portfolio_sd(w1, sd1, sd2, rho):
    return np.sqrt(w1**2*sd1**2 + (1-w1)**2*sd2**2 + 2*rho*w1*(1-w1)*sd1*sd2)

def portfolio_esg(w1, esg1, esg2):
    return w1 * esg1 + (1 - w1) * esg2

def convert_to_100(score, agency):
    agency = agency.lower()
    try:
        if agency == "sustainalytics":
            s = float(score)
            return max(0.0, min(100.0, 100-(s/50)*100)) if s < 50 else 0.0
        elif agency == "msci":
            m = {"ccc":0.0,"b":16.7,"bb":33.4,"bbb":50.1,"a":66.8,"aa":83.5,"aaa":100.0}
            return m.get(str(score).strip().lower(), 0.0)
        elif agency == "refinitiv":
            r = {0:0.0,1:10.0,2:25.0,3:50.0,4:75.0,5:95.0}
            return r.get(int(float(score)), 0.0)
        elif agency == "s&p":
            return max(0.0, min(100.0, float(score)))
    except Exception:
        return 0.0
    return 0.0


# ──────────────────────────────────────────────────────────
# UI HELPERS
# ──────────────────────────────────────────────────────────
def section_label(text):
    st.markdown(f"""
    <div class="section-label">
      <div class="section-label-bar"></div>
      <div class="section-label-text">{text}</div>
      <div class="section-label-rule"></div>
    </div>""", unsafe_allow_html=True)

def esg_hex(score):
    score = max(0.0, min(100.0, score))
    if score <= 50:
        t = score/50.0
        r=239; g=int(68+t*(180-68)); b=int(68+t*(8-68))
    else:
        t=(score-50.0)/50.0
        r=int(234+t*(34-234)); g=int(180+t*(197-180)); b=int(8+t*(94-8))
    return f"#{r:02x}{g:02x}{b:02x}"

def progress_ring_html(score, subtitle="ESG Score", size=154):
    col = esg_hex(score)
    R = 52; circ = 2*np.pi*R
    dash = (score/100)*circ; gap = circ-dash
    return f"""
    <div style="display:flex;flex-direction:column;align-items:center;gap:8px;padding:10px 0;">
      <svg width="{size}" height="{size}" viewBox="0 0 120 120">
        <circle cx="60" cy="60" r="{R}" fill="none" stroke="{col}28" stroke-width="13"/>
        <circle cx="60" cy="60" r="{R}" fill="none" stroke="{col}" stroke-width="13"
                stroke-dasharray="{dash:.2f} {gap:.2f}" stroke-linecap="round"
                transform="rotate(-90 60 60)"/>
        <text x="60" y="53" text-anchor="middle" font-family="Inter,sans-serif"
              font-size="21" font-weight="700" fill="{col}">{score:.1f}</text>
        <text x="60" y="70" text-anchor="middle" font-family="Inter,sans-serif"
              font-size="11" fill="#94a3b8">/ 100</text>
      </svg>
      <span style="font-size:11px;font-weight:700;letter-spacing:0.1em;
                   text-transform:uppercase;color:#7a9a8a;">{subtitle}</span>
    </div>"""

def alloc_bar_html(w1, w2, name1, name2):
    c1,c2 = "#2e7d36","#3b82f6"
    p1=f"{w1*100:.1f}%"; p2=f"{w2*100:.1f}%"
    return f"""
    <div class="bar-row">
      <div class="bar-label-row">
        <span style="color:{c1};">{name1}</span>
        <span style="color:{c1};">{p1}</span>
      </div>
      <div class="bar-track">
        <div class="bar-fill" style="width:{p1};background:linear-gradient(90deg,#1a5c32,{c1});"></div>
      </div>
    </div>
    <div class="bar-row" style="margin-top:14px;">
      <div class="bar-label-row">
        <span style="color:{c2};">{name2}</span>
        <span style="color:{c2};">{p2}</span>
      </div>
      <div class="bar-track">
        <div class="bar-fill" style="width:{p2};background:linear-gradient(90deg,#1e3a8a,{c2});"></div>
      </div>
    </div>"""

def alloc_card_html(title, w1, w2, name1, name2):
    c1,c2="#52c98a","#3b82f6"
    p1=f"{w1*100:.1f}%"; p2=f"{w2*100:.1f}%"
    return f"""
    <div class="card">
      <div class="card-title">{title}</div>
      <div class="bar-row">
        <div class="bar-label-row">
          <span style="color:{c1};">{name1}</span>
          <span style="color:{c1};">{p1}</span>
        </div>
        <div class="bar-track">
          <div class="bar-fill" style="width:{p1};background:linear-gradient(90deg,#1f6b42,{c1});"></div>
        </div>
      </div>
      <div class="bar-row" style="margin-top:12px;">
        <div class="bar-label-row">
          <span style="color:{c2};">{name2}</span>
          <span style="color:{c2};">{p2}</span>
        </div>
        <div class="bar-track">
          <div class="bar-fill" style="width:{p2};background:linear-gradient(90deg,#1e40af,{c2});"></div>
        </div>
      </div>
    </div>"""

def metric_tile(label, value, sub=""):
    sub_html = f'<div class="sub">{sub}</div>' if sub else ""
    return f"""
    <div class="metric-tile">
      <div class="label">{label}</div>
      <div class="value">{value}</div>
      {sub_html}
    </div>"""

def chip_html(value, suffix="", decimals=2):
    fmt = f"{value:+.{decimals}f}{suffix}"
    cls = "chip-pos" if value>0.001 else ("chip-neg" if value<-0.001 else "chip-neu")
    return f'<span class="chip {cls}">{fmt}</span>'

def get_agency_input(name, agency, key_pref):
    if agency == "MSCI":
        val = st.selectbox(f"{name} MSCI Rating",
            ["CCC","B","BB","BBB","A","AA","AAA"], index=3, key=f"{key_pref}_m")
    elif agency == "Refinitiv":
        val = st.number_input(f"{name} Score (0–5)", 0, 5, 3, key=f"{key_pref}_r")
    else:
        val = st.number_input(f"{name} Score", value=50.0, key=f"{key_pref}_s")
    return convert_to_100(val, agency)


# ──────────────────────────────────────────────────────────
# HERO
# ──────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-left">
    <h1>🌱 Ethos Invest</h1>
    <p>Build an optimal investment portfolio aligned with your financial risk tolerance and ESG values.</p>
    <div class="hero-pills">
      <span class="pill">2 assets</span>
      <span class="pill">4 ESG rating agencies</span>
      <span class="pill">ESG-constrained frontier</span>
      <span class="pill">Materiality assessment</span>
    </div>
  </div>
  <div class="hero-right">
    <div class="hero-stat-row">
      <div class="hero-stat">
        <div class="hero-stat-val">3</div>
        <div class="hero-stat-lbl">Portfolios<br>compared</div>
      </div>
      <div class="hero-stat">
        <div class="hero-stat-val">12</div>
        <div class="hero-stat-lbl">ESG topics<br>assessed</div>
      </div>
      <div class="hero-stat">
        <div class="hero-stat-val">1K</div>
        <div class="hero-stat-lbl">Frontier<br>points</div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────
# SECTION 1 · ASSETS & MARKET DATA
# ──────────────────────────────────────────────────────────
section_label("Assets &amp; Market Data")

asset_col1, asset_col2 = st.columns(2, gap="large")

with asset_col1:
    st.markdown('<div class="card"><div class="card-title">Asset 1</div>', unsafe_allow_html=True)
    na1, ag1_col = st.columns([1.2, 1])
    with na1:
        st.markdown('<div class="card-field-label">Company / Fund name</div>', unsafe_allow_html=True)
        asset1_name = st.text_input("a1name", "ExxonMobil", label_visibility="collapsed", key="asset1_name")
    with ag1_col:
        st.markdown('<div class="card-field-label">ESG Rating Agency</div>', unsafe_allow_html=True)
        agency1 = st.selectbox("a1ag", ["S&P","MSCI","Sustainalytics","Refinitiv"],
                               label_visibility="collapsed", key="ag1")
    r1_col, sd1_col = st.columns(2)
    with r1_col:
        st.markdown('<div class="card-field-label">Expected Return (%)</div>', unsafe_allow_html=True)
        r1 = st.number_input("a1r", value=12.0, step=0.5, label_visibility="collapsed", key="r1") / 100
    with sd1_col:
        st.markdown('<div class="card-field-label">Volatility (%)</div>', unsafe_allow_html=True)
        sd1 = st.number_input("a1sd", value=25.0, step=0.5, min_value=0.01,
                              label_visibility="collapsed", key="sd1") / 100
    st.markdown('</div>', unsafe_allow_html=True)

with asset_col2:
    st.markdown('<div class="card"><div class="card-title">Asset 2</div>', unsafe_allow_html=True)
    na2, ag2_col = st.columns([1.2, 1])
    with na2:
        st.markdown('<div class="card-field-label">Company / Fund name</div>', unsafe_allow_html=True)
        asset2_name = st.text_input("a2name", "Unilever", label_visibility="collapsed", key="asset2_name")
    with ag2_col:
        st.markdown('<div class="card-field-label">ESG Rating Agency</div>', unsafe_allow_html=True)
        agency2 = st.selectbox("a2ag", ["S&P","MSCI","Sustainalytics","Refinitiv"],
                               label_visibility="collapsed", key="ag2")
    r2_col, sd2_col = st.columns(2)
    with r2_col:
        st.markdown('<div class="card-field-label">Expected Return (%)</div>', unsafe_allow_html=True)
        r2 = st.number_input("a2r", value=8.0, step=0.5, label_visibility="collapsed", key="r2") / 100
    with sd2_col:
        st.markdown('<div class="card-field-label">Volatility (%)</div>', unsafe_allow_html=True)
        sd2 = st.number_input("a2sd", value=14.0, step=0.5, min_value=0.01,
                              label_visibility="collapsed", key="sd2") / 100
    st.markdown('</div>', unsafe_allow_html=True)

mkt_col1, mkt_col2 = st.columns(2, gap="large")
with mkt_col1:
    st.markdown('<div class="card"><div class="card-title">Correlation Coefficient (ρ)</div>', unsafe_allow_html=True)
    rho = st.slider("rho", -1.0, 1.0, 0.20, 0.01, label_visibility="collapsed", key="rho")
    st.markdown('<div class="card-subtitle">Controls how the two assets move together. Lower correlation = greater diversification benefit.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
with mkt_col2:
    st.markdown('<div class="card"><div class="card-title">Risk-Free Rate (%)</div>', unsafe_allow_html=True)
    r_free = st.number_input("rfr", value=2.0, step=0.1, label_visibility="collapsed", key="rfr") / 100
    st.markdown('<div class="card-subtitle">Used to calculate the Sharpe ratio and to draw the Capital Market Line on the frontier chart.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────
# SECTION 2 · RISK PREFERENCE
# ──────────────────────────────────────────────────────────
section_label("Risk Preference")

risk_col1, risk_col2 = st.columns([1.6, 1], gap="large")

with risk_col1:
    st.markdown('<div class="card"><div class="card-title">Determine your risk aversion (γ)</div>', unsafe_allow_html=True)

    gamma_mode = st.radio("gamma_mode", ["Enter γ directly", "Take the questionnaire"],
                          horizontal=True, label_visibility="collapsed", key="gamma_mode")

    if gamma_mode == "Enter γ directly":
        st.markdown('<div class="card-field-label">Gamma  (−10 = risk-loving · 0 = neutral · +10 = risk-averse)</div>', unsafe_allow_html=True)
        gamma = st.slider("gamma_direct", -10.0, 10.0, 3.0, 0.5, label_visibility="collapsed")
        glabel = ("Very Cautious" if gamma >= 6 else "Cautious" if gamma >= 2
                  else "Moderate" if gamma >= -1 else "Adventurous" if gamma >= -5
                  else "Very Adventurous")
    else:
        st.markdown('<div class="card-subtitle" style="margin-bottom:12px;">Answer all 5 questions honestly — there are no right or wrong answers.</div>', unsafe_allow_html=True)
        q1 = st.selectbox("Q1. Your general attitude to investment risk?",
            ["1 — Avoid risk wherever possible","2 — Prefer low-risk, steady options",
             "3 — Comfortable with moderate risk","4 — Willing to take risk for higher returns",
             "5 — Actively seek high-risk, high-reward"], key="q1")
        q2 = st.selectbox('Q2. "I prefer slow, steady growth over higher but uncertain returns."',
            ["1 — Strongly agree","2 — Tend to agree","3 — In between",
             "4 — Tend to disagree","5 — Strongly disagree"], key="q2")
        q3 = st.selectbox("Q3. Your portfolio drops 20% in three months. You:",
            ["1 — Sell everything immediately","2 — Sell some to reduce exposure",
             "3 — Do nothing and wait","4 — Review but stay the course",
             "5 — Buy more — great opportunity"], key="q3")
        q4 = st.selectbox("Q4. How much would you put in a high-risk, high-reward investment?",
            ["1 — Very little, if any","2 — Less than a quarter",
             "3 — Around half","4 — More than half","5 — All of it"], key="q4")
        q5 = st.selectbox('Q5. "I always prefer a small guaranteed return over a larger uncertain one."',
            ["1 — Strongly agree","2 — Tend to agree","3 — In between",
             "4 — Tend to disagree","5 — Strongly disagree"], key="q5")

        avg = (int(q1[0])+int(q2[0])+int(q3[0])+int(q4[0])+int(q5[0])) / 5
        if   avg <= 1.5: gamma, glabel =  8.0, "Very Cautious"
        elif avg <= 2.3: gamma, glabel =  4.0, "Cautious"
        elif avg <= 3.2: gamma, glabel =  0.0, "Moderate"
        elif avg <= 4.1: gamma, glabel = -4.0, "Adventurous"
        else:            gamma, glabel = -8.0, "Very Adventurous"

    st.markdown('</div>', unsafe_allow_html=True)

with risk_col2:
    st.markdown(f"""
    <div class="card" style="text-align:center;padding-top:24px;padding-bottom:24px;">
      <div class="card-title" style="text-align:center;">Risk Profile</div>
      <div style="font-size:36px;font-weight:700;color:#e7eaf0;letter-spacing:-0.04em;
                  margin:10px 0 6px;font-family:'JetBrains Mono',monospace;">{glabel}</div>
      <div style="font-family:'JetBrains Mono',monospace;font-size:20px;color:#52c98a;
                  margin-bottom:12px;">γ = {gamma:.1f}</div>
      <div class="card-subtitle" style="text-align:center;">
        {"High risk aversion — prioritises capital preservation." if gamma >= 4
         else "Moderate risk aversion — balances growth and safety." if gamma >= 0
         else "Low risk aversion — comfortable with significant volatility."}
      </div>
    </div>""", unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────
# SECTION 3 · ESG PREFERENCE
# ──────────────────────────────────────────────────────────
section_label("ESG Preference")

pref_col1, pref_col2 = st.columns([1.6, 1], gap="large")

with pref_col1:
    st.markdown('<div class="card"><div class="card-title">Discover your ESG preference</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-subtitle" style="margin-bottom:14px;">Answer four questions. The app infers a starting ESG weight (λ), then lets you fine-tune it.</div>', unsafe_allow_html=True)

    eq1 = st.selectbox(
        "Would you invest in a company with strong returns but weaker ESG performance?",
        ["1. No, never","2. Only with a large return premium","3. It depends","4. Usually yes","5. Yes, returns matter most"],
        key="esg_q1")
    eq2 = st.selectbox(
        "Which portfolio would you prefer?",
        ["1. 10% return, ESG 40","2. 9% return, ESG 55","3. 8.5% return, ESG 65",
         "4. 8% return, ESG 80","5. 7% return, ESG 90"], key="esg_q2")
    eq3 = st.selectbox(
        "How would you feel if ESG constraints reduced your return by ~2%?",
        ["1. Very uncomfortable","2. Uncomfortable","3. Neutral",
         "4. Comfortable","5. Very comfortable"], key="esg_q3")
    eq4 = st.selectbox(
        "Which statement best describes your investment philosophy?",
        ["1. I maximise returns","2. I lean toward returns","3. I want balance",
         "4. I lean toward sustainability","5. I prioritise sustainability"], key="esg_q4")

    avg_esg = (int(eq1[0])+int(eq2[0])+int(eq3[0])+int(eq4[0])) / 4
    if   avg_esg <= 1.5: inferred_lambda, pref_label, pref_note = 0.0,  "Return-focused",      "Very little willingness to sacrifice return for ESG."
    elif avg_esg <= 2.4: inferred_lambda, pref_label, pref_note = 0.25, "Light ESG preference", "Some ESG interest, but return remains the priority."
    elif avg_esg <= 3.4: inferred_lambda, pref_label, pref_note = 0.60, "Balanced investor",    "A measured willingness to trade some return for ESG alignment."
    elif avg_esg <= 4.2: inferred_lambda, pref_label, pref_note = 0.85, "ESG-led investor",     "Strong preference for sustainability even with some return trade-off."
    else:                inferred_lambda, pref_label, pref_note = 1.0,  "Impact-focused",       "Maximum ESG emphasis, even if returns are reduced."

    st.markdown('<div class="card-field-label" style="margin-top:16px;">Refine your ESG preference (λ)</div>', unsafe_allow_html=True)
    lambda_esg = st.slider("lambda_esg", 0.0, 1.0, float(inferred_lambda), 0.05,
                           label_visibility="collapsed", key="lambda_esg",
                           help="0 = no ESG sacrifice · 1 = maximum ESG priority")
    st.markdown(f"""
    <div class="info-box" style="margin-top:10px;">
      Based on your answers, we suggest λ = <strong>{inferred_lambda:.2f}</strong>
      (<em>{pref_label}</em>). Adjust the slider above if you'd like to override this.
    </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with pref_col2:
    st.markdown(f"""
    <div class="card" style="text-align:center;padding-top:24px;padding-bottom:24px;">
      <div class="card-title" style="text-align:center;">Preference Profile</div>
      {progress_ring_html(lambda_esg * 100, "ESG Weight (λ)", size=160)}
      <div class="profile-badge">
        <div class="pname">{pref_label}</div>
        <div class="pnote">{pref_note}</div>
      </div>
    </div>""", unsafe_allow_html=True)

st.markdown('<hr class="fancy-divider">', unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────
# SECTION 4 · ESG SCORES
# ──────────────────────────────────────────────────────────
section_label("ESG Scores")

esg_method = st.radio("esg_method",
    ["Overall ESG Score","Separate E, S, and G Pillars"],
    horizontal=True, label_visibility="collapsed", key="esg_method")

weights_ok = True
w_e = w_s = w_g = 33

if esg_method == "Separate E, S, and G Pillars":
    st.markdown('<div class="card"><div class="card-title">ESG Pillar Weights</div>', unsafe_allow_html=True)

    weight_method = st.radio("weight_method",
        ["Manual Entry","Materiality Assessment"],
        horizontal=True, label_visibility="collapsed", key="weight_method")

    if weight_method == "Materiality Assessment":
        TOPICS = {
            "Climate change & emissions":   "E",
            "Water & resource scarcity":    "E",
            "Deforestation & biodiversity": "E",
            "Pollution & waste":            "E",
            "Labour rights & fair pay":     "S",
            "Supply chain ethics":          "S",
            "Community impact":             "S",
            "Diversity & inclusion":        "S",
            "Board independence":           "G",
            "Executive pay":                "G",
            "Anti-corruption":              "G",
            "Transparency & reporting":     "G",
        }
        st.markdown('<div class="card-subtitle" style="margin-bottom:10px;">Select the <strong>4 ESG issues</strong> that matter most to you personally. Your choices will suggest pillar weights.</div>', unsafe_allow_html=True)
        selected = st.multiselect("mat", list(TOPICS.keys()),
                                  max_selections=4, label_visibility="collapsed", key="mat_topics")

        counts = {"E":0,"S":0,"G":0}
        for t in selected:
            counts[TOPICS[t]] += 1

        floor = 0.10
        raw   = {k: max(counts[k], floor) for k in counts}
        total = sum(raw.values())
        sug_e = round((raw["E"]/total)*100)
        sug_s = round((raw["S"]/total)*100)
        sug_g = 100 - sug_e - sug_s

        if len(selected) == 4:
            st.success(f"Suggested weights — E: {sug_e}% · S: {sug_s}% · G: {sug_g}%")
        else:
            st.caption(f"{4-len(selected)} more selection(s) needed to generate weights.")
            sug_e, sug_s, sug_g = 34, 33, 33
        st.markdown('<div class="card-subtitle">Review and adjust below if needed.</div>', unsafe_allow_html=True)
    else:
        sug_e, sug_s, sug_g = 34, 33, 33

    cw1, cw2, cw3 = st.columns(3, gap="small")
    with cw1:
        st.markdown('<div class="card-field-label">Environmental %</div>', unsafe_allow_html=True)
        w_e = st.number_input("we", 0, 100, sug_e, label_visibility="collapsed", key="we")
    with cw2:
        st.markdown('<div class="card-field-label">Social %</div>', unsafe_allow_html=True)
        w_s = st.number_input("ws", 0, 100, sug_s, label_visibility="collapsed", key="ws")
    with cw3:
        st.markdown('<div class="card-field-label">Governance %</div>', unsafe_allow_html=True)
        w_g = st.number_input("wg", 0, 100, sug_g, label_visibility="collapsed", key="wg")

    weights_ok = (w_e + w_s + w_g) == 100
    if not weights_ok:
        st.markdown(f'<div class="warn-box">Weights sum to {w_e+w_s+w_g}% — must equal 100%.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

esg_col1, esg_col2 = st.columns(2, gap="large")
with esg_col1:
    st.markdown(f'<div class="card"><div class="card-title">{asset1_name}</div>', unsafe_allow_html=True)
    if esg_method == "Overall ESG Score":
        esg1_100 = get_agency_input(asset1_name, agency1, "o1")
    else:
        e1 = get_agency_input(f"E", agency1, "p1e")
        s1 = get_agency_input(f"S", agency1, "p1s")
        g1 = get_agency_input(f"G", agency1, "p1g")
        esg1_100 = (w_e/100)*e1 + (w_s/100)*s1 + (w_g/100)*g1
    st.caption(f"Normalised ESG score: **{esg1_100:.1f} / 100**")
    st.markdown('</div>', unsafe_allow_html=True)

with esg_col2:
    st.markdown(f'<div class="card"><div class="card-title">{asset2_name}</div>', unsafe_allow_html=True)
    if esg_method == "Overall ESG Score":
        esg2_100 = get_agency_input(asset2_name, agency2, "o2")
    else:
        e2 = get_agency_input(f"E", agency2, "p2e")
        s2 = get_agency_input(f"S", agency2, "p2s")
        g2 = get_agency_input(f"G", agency2, "p2g")
        esg2_100 = (w_e/100)*e2 + (w_s/100)*s2 + (w_g/100)*g2
    st.caption(f"Normalised ESG score: **{esg2_100:.1f} / 100**")
    st.markdown('</div>', unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────
# CTA BUTTON
# ──────────────────────────────────────────────────────────
st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)
_, cta_col, _ = st.columns([1, 1.4, 1])
with cta_col:
    st.markdown('<div class="cta-wrap">', unsafe_allow_html=True)
    run = st.button("🚀  Calculate Portfolio", key="run")
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)

if not run:
    st.markdown("""
    <div class="info-box">
      Fill in all inputs above, then click <strong>Calculate Portfolio</strong> to see your results.
    </div>""", unsafe_allow_html=True)
    st.stop()

if not weights_ok:
    st.markdown("""
    <div class="warn-box">
      ESG pillar weights must sum to 100%. Please adjust them above before continuing.
    </div>""", unsafe_allow_html=True)
    st.stop()


# ──────────────────────────────────────────────────────────
# CALCULATIONS
# ──────────────────────────────────────────────────────────
esg_threshold = (min(esg1_100,esg2_100)
                 + lambda_esg*(max(esg1_100,esg2_100)-min(esg1_100,esg2_100)))

weights  = np.linspace(0,1,1000)
rets     = portfolio_return(weights,r1,r2)
vols     = portfolio_sd(weights,sd1,sd2,rho)
esgs     = portfolio_esg(weights,esg1_100,esg2_100)
sharpes  = np.where(vols>0,(rets-r_free)/vols,-np.inf)

idx_all  = int(np.argmax(sharpes))
eligible = np.where(esgs>=esg_threshold)[0]

if len(eligible)==0:
    st.error("No portfolios satisfy your ESG threshold. Try reducing your ESG preference (λ).")
    st.stop()

idx_esg  = eligible[int(np.argmax(sharpes[eligible]))]
w1_all   = weights[idx_all];  w1_esg  = weights[idx_esg]
ret_all  = rets[idx_all];     ret_esg = rets[idx_esg]
vol_all  = vols[idx_all];     vol_esg = vols[idx_esg]
esg_all  = esgs[idx_all];     esg_opt = esgs[idx_esg]
sh_all   = sharpes[idx_all];  sh_esg  = sharpes[idx_esg]

# Minimum variance
denom  = sd1**2+sd2**2-2*rho*sd1*sd2
w1_mv  = float(np.clip((sd2**2-rho*sd1*sd2)/denom if denom!=0 else 0.5,0,1))
ret_mv = portfolio_return(w1_mv,r1,r2)
vol_mv = portfolio_sd(w1_mv,sd1,sd2,rho)
esg_mv = portfolio_esg(w1_mv,esg1_100,esg2_100)
sh_mv  = (ret_mv-r_free)/vol_mv if vol_mv>0 else 0.0

d_ret = ret_esg-ret_all
d_sd  = vol_esg-vol_all
d_esg = esg_opt-esg_all


# ──────────────────────────────────────────────────────────
# ══ RESULTS ══════════════════════════════════════════════
# ──────────────────────────────────────────────────────────

# ── Thin results header band ──────────────────────────────
st.markdown("""
<div style="background:linear-gradient(90deg,rgba(82,201,138,0.10),rgba(59,130,246,0.06),transparent);
            border:1px solid rgba(82,201,138,0.13);border-radius:16px;
            padding:16px 24px;margin:24px 0 4px;display:flex;align-items:center;gap:12px;">
  <div style="font-size:22px;">📊</div>
  <div>
    <div style="font-size:15px;font-weight:700;color:#f0f4f8;letter-spacing:-0.02em;">Portfolio Results</div>
    <div style="font-size:12px;color:#8b93a3;margin-top:2px;">
      Based on your inputs — ESG-constrained, unconstrained, and minimum variance portfolios.
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────
# RESULT SECTION 1 · ESG OPTIMAL PORTFOLIO
# ──────────────────────────────────────────────────────────
section_label("ESG Optimal Portfolio")

col_alloc, col_ring, col_metrics = st.columns([2.4, 1.1, 2.4], gap="large")

with col_alloc:
    st.markdown(f"""
    <div class="card">
      <div class="card-title">Asset Allocation</div>
      {alloc_bar_html(w1_esg,1-w1_esg,asset1_name,asset2_name)}
    </div>""", unsafe_allow_html=True)

with col_ring:
    st.markdown(progress_ring_html(esg_opt,"Portfolio ESG",size=160), unsafe_allow_html=True)

with col_metrics:
    st.markdown(metric_tile("Expected Return", f"{ret_esg*100:.2f}%","Annualised"), unsafe_allow_html=True)
    st.markdown(metric_tile("Risk (Std Dev)",  f"{vol_esg*100:.2f}%","Annualised"), unsafe_allow_html=True)
    st.markdown(metric_tile("Sharpe Ratio",    f"{sh_esg:.4f}","Risk-adjusted return"), unsafe_allow_html=True)

st.markdown("<div style='height:6px;'></div>", unsafe_allow_html=True)
st.markdown('<hr class="fancy-divider">', unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────
# RESULT SECTION 2 · PORTFOLIO COMPARISON TABLE
# ──────────────────────────────────────────────────────────
section_label("Portfolio Comparison")

table_rows = [
    (f"{asset1_name} weight", f"{w1_esg*100:.2f}%",     f"{w1_all*100:.2f}%",     f"{w1_mv*100:.2f}%"),
    (f"{asset2_name} weight", f"{(1-w1_esg)*100:.2f}%", f"{(1-w1_all)*100:.2f}%", f"{(1-w1_mv)*100:.2f}%"),
    ("Expected return",        f"{ret_esg*100:.2f}%",    f"{ret_all*100:.2f}%",    f"{ret_mv*100:.2f}%"),
    ("Risk (Std Dev)",         f"{vol_esg*100:.2f}%",    f"{vol_all*100:.2f}%",    f"{vol_mv*100:.2f}%"),
    ("ESG score (0–100)",      f"{esg_opt:.2f}",         f"{esg_all:.2f}",         f"{esg_mv:.2f}"),
    ("Sharpe ratio",           f"{sh_esg:.4f}",          f"{sh_all:.4f}",          f"{sh_mv:.4f}"),
]

table_html = """
<div class="cmp-wrap">
<table class="cmp-table">
  <thead><tr>
    <th>Metric</th>
    <th class="col-esg">✅ ESG-Constrained</th>
    <th class="col-other">📈 Unconstrained</th>
    <th class="col-other">🛡️ Min Variance</th>
  </tr></thead><tbody>"""
for row in table_rows:
    table_html += f"<tr><td>{row[0]}</td><td class='col-esg'>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td></tr>"
table_html += "</tbody></table></div>"
st.markdown(table_html, unsafe_allow_html=True)

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

# ── Allocation breakdown bars ──────────────────────────────
section_label("Allocation Breakdown")

bar_col1, bar_col2, bar_col3 = st.columns(3, gap="large")
with bar_col1:
    st.markdown(alloc_card_html("✅ ESG Constrained", w1_esg,1-w1_esg,asset1_name,asset2_name), unsafe_allow_html=True)
with bar_col2:
    st.markdown(alloc_card_html("📈 Unconstrained",   w1_all,1-w1_all,asset1_name,asset2_name), unsafe_allow_html=True)
with bar_col3:
    st.markdown(alloc_card_html("🛡️ Min Variance",    w1_mv, 1-w1_mv, asset1_name,asset2_name), unsafe_allow_html=True)

st.markdown('<hr class="fancy-divider">', unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────
# RESULT SECTION 3 · IMPACT OF ESG CONSTRAINT
# ──────────────────────────────────────────────────────────
section_label("Impact of ESG Constraint")

ic1, ic2, ic3 = st.columns(3, gap="large")
for col, label, val, suffix, dec in [
    (ic1, "Return Change",  d_ret*100, " pp",  2),
    (ic2, "Risk Change",    d_sd*100,  " pp",  2),
    (ic3, "ESG Score Gain", d_esg,     " pts", 1),
]:
    with col:
        st.markdown(f"""
        <div class="card" style="text-align:center;padding:22px 18px;">
          <div class="card-title" style="text-align:center;">{label}</div>
          {chip_html(val, suffix, dec)}
          <div class="card-subtitle" style="text-align:center;margin-top:10px;">
            vs unconstrained portfolio
          </div>
        </div>""", unsafe_allow_html=True)

st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)

if idx_all == idx_esg:
    st.markdown("""
    <div class="info-box">
      The unconstrained optimal portfolio already meets your ESG threshold —
      applying the constraint has no material effect on the allocation.
    </div>""", unsafe_allow_html=True)
else:
    st.markdown(f"""
    <div class="info-box">
      Your ESG preference requires a minimum portfolio score of <strong>{esg_threshold:.2f}</strong>.
      The portfolio shifts weight toward the higher-rated asset to meet this.
      The tiles above show the exact cost (return / risk) and benefit (ESG score) of that tilt.
    </div>""", unsafe_allow_html=True)

st.markdown('<hr class="fancy-divider">', unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────
# RESULT SECTION 4 · CHARTS
# ──────────────────────────────────────────────────────────
section_label("Charts")

plt.rcParams.update({
    "font.family":"sans-serif",
    "axes.spines.top":False,"axes.spines.right":False,
    "axes.grid":True,"grid.alpha":0.22,"grid.linestyle":"--",
})

w_plot  = np.linspace(-0.5,1.5,500)
r_plot  = portfolio_return(w_plot,r1,r2)
v_plot  = portfolio_sd(w_plot,sd1,sd2,rho)
sd_max  = max(v_plot)*1.05
sd_rng  = np.linspace(0,sd_max,300)
cml_all = r_free+((ret_all-r_free)/vol_all)*sd_rng if vol_all>0 else np.zeros(300)
cml_esg = r_free+((ret_esg-r_free)/vol_esg)*sd_rng if vol_esg>0 else np.zeros(300)

chart_col1, chart_col2 = st.columns(2, gap="large")

with chart_col1:
    fig1,ax1 = plt.subplots(figsize=(6,5))
    fig1.patch.set_facecolor("#f5f8f5"); ax1.set_facecolor("#f5f8f5")
    ax1.plot(v_plot,r_plot,color="#94a3b8",lw=1.5,alpha=0.5,label="Full frontier")
    ax1.plot(sd_rng,cml_all,"--",color="#94a3b8",lw=1.5,label="CML (unconstrained)")
    ax1.plot(sd_rng,cml_esg,"--",color="#16a34a",lw=1.5,label="CML (ESG)")
    ax1.scatter(0,      r_free, marker="s",s=80, color="#0d1f0f",zorder=5,label="Risk-free")
    ax1.scatter(vol_all,ret_all,marker="*",s=240,color="#64748b",edgecolors="white",lw=0.8,zorder=6,label="Optimal (unconstrained)")
    ax1.scatter(vol_esg,ret_esg,marker="*",s=240,color="#16a34a",edgecolors="white",lw=0.8,zorder=7,label="Optimal (ESG)")
    ax1.scatter(vol_mv, ret_mv, marker="D",s=110,color="#3b82f6",edgecolors="white",lw=0.8,zorder=6,label="Min Variance")
    ax1.annotate("Unconstrained",(vol_all,ret_all),xytext=(-6,-16),textcoords="offset points",fontsize=8,color="#64748b")
    ax1.annotate("ESG optimal",  (vol_esg,ret_esg),xytext=(8, 6), textcoords="offset points",fontsize=8,color="#16a34a")
    ax1.annotate("Min Variance", (vol_mv, ret_mv), xytext=(8,-14),textcoords="offset points",fontsize=8,color="#3b82f6")
    ax1.set_xlim(0,max(v_plot)*1.02)
    ax1.xaxis.set_major_formatter(PercentFormatter(1.0))
    ax1.yaxis.set_major_formatter(PercentFormatter(1.0))
    ax1.set_xlabel("Risk (Standard Deviation)",fontsize=11)
    ax1.set_ylabel("Expected Return",fontsize=11)
    ax1.set_title("Efficient Frontier & Capital Market Lines",fontsize=13,fontweight="bold",color="#0d1f0f")
    ax1.legend(fontsize=7.5); plt.tight_layout()
    st.pyplot(fig1)
    st.caption("Stars mark the tangency (highest Sharpe) portfolio. Diamond marks minimum variance.")

with chart_col2:
    fig2,ax2 = plt.subplots(figsize=(6,5))
    fig2.patch.set_facecolor("#f5f8f5"); ax2.set_facecolor("#f5f8f5")
    ax2.plot(esgs,sharpes,color="#ef4444",lw=2.5,label="ESG–Sharpe frontier")
    ax2.axvline(esg_threshold,color="#f59e0b",lw=1.5,linestyle=":",label=f"ESG threshold ({esg_threshold:.1f})")
    ax2.scatter(esg_all,sh_all,marker="*",s=240,color="#64748b",edgecolors="white",lw=0.8,zorder=5,label="Optimal (unconstrained)")
    ax2.scatter(esg_opt,sh_esg,marker="*",s=240,color="#16a34a",edgecolors="white",lw=0.8,zorder=6,label="Optimal (ESG)")
    ax2.scatter(esg_mv, sh_mv, marker="D",s=110,color="#3b82f6",edgecolors="white",lw=0.8,zorder=5,label="Min Variance")
    ax2.annotate("Unconstrained",(esg_all,sh_all),xytext=(-6,-16),textcoords="offset points",fontsize=8,color="#64748b")
    ax2.annotate("ESG optimal",  (esg_opt,sh_esg),xytext=(8, 6), textcoords="offset points",fontsize=8,color="#16a34a")
    ax2.set_xlabel("Portfolio ESG Score (0–100)",fontsize=11)
    ax2.set_ylabel("Sharpe Ratio",fontsize=11)
    ax2.set_title("ESG–Sharpe Ratio Trade-off",fontsize=13,fontweight="bold",color="#0d1f0f")
    ax2.legend(fontsize=7.5); plt.tight_layout()
    st.pyplot(fig2)
    st.caption("Amber dotted line marks your minimum ESG threshold.")


# ──────────────────────────────────────────────────────────
# FOOTER
# ──────────────────────────────────────────────────────────
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center;font-size:12px;color:#3a4550;padding:20px 0;
            border-top:1px solid rgba(255,255,255,0.05);">
  <strong style="color:#52c98a;">Ethos Invest</strong> &nbsp;·&nbsp;
  Sustainable Finance Portfolio Tool &nbsp;·&nbsp;
  For illustrative purposes only — not financial advice.
</div>
""", unsafe_allow_html=True)
