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
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,300;0,14..32,400;0,14..32,500;0,14..32,600;0,14..32,700;1,14..32,400&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --bg: #0e1014;
    --panel: #13161c;
    --line: rgba(255,255,255,0.07);
    --text: #e7eaf0;
    --muted: #8b93a3;
    --green: #52c98a;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background: var(--bg);
    color: var(--text);
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(82,201,138,0.08), transparent 28%),
        radial-gradient(circle at top right, rgba(59,130,246,0.07), transparent 24%),
        linear-gradient(180deg, #0e1014 0%, #0d0f13 100%);
}

#MainMenu, footer, header { visibility: hidden; }

.block-container {
    padding-top: 1.2rem;
    padding-bottom: 2rem;
    max-width: 1400px;
}

.hero {
    background: linear-gradient(135deg, rgba(82,201,138,0.08), rgba(59,130,246,0.05));
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 22px;
    padding: 28px 28px 22px 28px;
    box-shadow: 0 12px 40px rgba(0,0,0,0.24);
}
.hero h1 {
    font-size: 2.1rem;
    letter-spacing: -0.04em;
    margin: 0;
    color: #f5f7fb;
}
.hero p {
    margin: 8px 0 0 0;
    color: var(--muted);
    font-size: 0.98rem;
    line-height: 1.5;
}
.hero-badge {
    display: inline-block;
    margin-top: 14px;
    padding: 5px 10px;
    border-radius: 999px;
    border: 1px solid rgba(82,201,138,0.22);
    background: rgba(82,201,138,0.08);
    color: #b6ead0;
    font-size: 11px;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}

.section-label {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.18em;
    color: var(--green);
    text-transform: uppercase;
    margin-top: 28px;
    margin-bottom: 12px;
    opacity: 0.88;
}

.card {
    background: linear-gradient(180deg, rgba(255,255,255,0.01), rgba(255,255,255,0));
    background-color: var(--panel);
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 18px 18px 16px 18px;
    margin-bottom: 12px;
    box-shadow: 0 1px 2px rgba(0,0,0,0.35), 0 18px 40px rgba(0,0,0,0.16);
}
.card-title {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--green);
    margin-bottom: 12px;
}
.card-subtitle {
    font-size: 12px;
    color: var(--muted);
    margin-top: 6px;
    margin-bottom: 10px;
}

.metric-tile {
    background: var(--panel);
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 18px 18px 16px 18px;
    box-shadow: 0 1px 2px rgba(0,0,0,0.35);
    position: relative;
    overflow: hidden;
}
.metric-tile::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #1f6b42, #52c98a, transparent);
}
.metric-tile .label {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #6f7786 !important;
    margin-bottom: 8px;
}
.metric-tile .value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 28px;
    font-weight: 600;
    color: var(--text) !important;
    letter-spacing: -0.03em;
}
.metric-tile .sub {
    font-size: 11px;
    color: #525a69 !important;
    margin-top: 6px;
    font-family: 'JetBrains Mono', monospace;
}

.bar-row { margin-bottom: 10px; }
.bar-label-row {
    display: flex;
    justify-content: space-between;
    font-size: 12px;
    font-weight: 500;
    margin-bottom: 6px;
    color: #97a0b0 !important;
    font-family: 'JetBrains Mono', monospace;
}
.bar-track {
    height: 6px;
    background: rgba(255,255,255,0.06);
    border-radius: 999px;
    overflow: hidden;
}
.bar-fill {
    height: 6px;
    border-radius: 999px;
    background: linear-gradient(90deg, #1f6b42, #52c98a);
}

.cmp-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 12px;
    font-family: 'JetBrains Mono', monospace;
    color: #c0c5d0 !important;
    overflow: hidden;
    border-radius: 16px;
}
.cmp-table th {
    background: rgba(255,255,255,0.02);
    color: #52c98a !important;
    padding: 12px 16px;
    text-align: left;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    border-bottom: 1px solid rgba(82,201,138,0.18);
}
.cmp-table td {
    padding: 11px 16px;
    border-bottom: 1px solid rgba(255,255,255,0.04);
    color: #c0c5d0 !important;
    background: transparent;
}
.cmp-table tr:nth-child(even) td { background: rgba(255,255,255,0.02); }
.cmp-table tr:hover td { background: rgba(82,201,138,0.04); }
.cmp-table tr:last-child td { border-bottom: none; }

.chip {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 700;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 0.02em;
}
.chip-pos { background: rgba(82,201,138,0.12); color: #52c98a !important; border: 1px solid rgba(82,201,138,0.2); }
.chip-neg { background: rgba(224,90,90,0.12); color: #e05a5a !important; border: 1px solid rgba(224,90,90,0.2); }
.chip-neu { background: rgba(255,255,255,0.05); color: #7a8090 !important; border: 1px solid rgba(255,255,255,0.08); }

hr.fancy-divider {
    border: none;
    height: 1px;
    background: rgba(255,255,255,0.07);
    margin: 26px 0;
}

.info-box {
    background: rgba(82,201,138,0.06);
    border: 1px solid rgba(82,201,138,0.15);
    border-left: 3px solid #52c98a;
    padding: 13px 16px;
    border-radius: 0 12px 12px 0;
    color: #b9e7ce !important;
    font-size: 13px;
    margin: 10px 0;
}
.warn-box {
    background: rgba(220,170,60,0.06);
    border: 1px solid rgba(220,170,60,0.15);
    border-left: 3px solid #dcaa3c;
    padding: 13px 16px;
    border-radius: 0 12px 12px 0;
    color: #e5c57b !important;
    font-size: 13px;
    margin: 10px 0;
}

.stButton > button {
    background: linear-gradient(135deg, #1a5c38 0%, #217a4a 100%) !important;
    border: 1px solid rgba(82,201,138,0.18) !important;
    border-radius: 14px !important;
    color: #e6f7ee !important;
    font-weight: 700 !important;
    letter-spacing: 0.04em;
    padding: 0.75rem 1rem !important;
    width: 100%;
    box-shadow: 0 8px 24px rgba(33,122,74,0.18);
    transition: all 0.2s ease;
}
.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 12px 26px rgba(33,122,74,0.26);
    background: linear-gradient(135deg, #1f6e43 0%, #268f56 100%) !important;
}

[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input,
[data-baseweb="select"] > div,
[data-baseweb="textarea"] textarea {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 12px !important;
    color: #eef2f7 !important;
}
[data-testid="stTextInput"] input:focus,
[data-testid="stNumberInput"] input:focus,
[data-baseweb="select"]:focus-within,
[data-baseweb="textarea"]:focus-within {
    border-color: rgba(82,201,138,0.34) !important;
    box-shadow: 0 0 0 1px rgba(82,201,138,0.16) !important;
}

.helper-line {
    font-size: 12px;
    color: var(--muted);
    line-height: 1.5;
}
</style>
""",
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────────────────
# CORE LOGIC (UNCHANGED)
# ──────────────────────────────────────────────────────────
def portfolio_return(w1, r1, r2):
    return w1 * r1 + (1 - w1) * r2


def portfolio_sd(w1, sd1, sd2, rho):
    return np.sqrt(w1**2 * sd1**2 + (1-w1)**2 * sd2**2 + 2*rho*w1*(1-w1)*sd1*sd2)


def portfolio_esg(w1, esg1, esg2):
    return w1 * esg1 + (1 - w1) * esg2


def convert_to_100(score, agency):
    agency = agency.lower()
    try:
        if agency == "sustainalytics":
            s = float(score)
            return max(0.0, min(100.0, 100 - (s / 50) * 100)) if s < 50 else 0.0
        elif agency == "msci":
            msci_map = {"ccc": 0.0, "b": 16.7, "bb": 33.4, "bbb": 50.1,
                        "a": 66.8, "aa": 83.5, "aaa": 100.0}
            return msci_map.get(str(score).strip().lower(), 0.0)
        elif agency == "refinitiv":
            r_map = {0: 0.0, 1: 10.0, 2: 25.0, 3: 50.0, 4: 75.0, 5: 95.0}
            return r_map.get(int(float(score)), 0.0)
        elif agency == "s&p":
            return max(0.0, min(100.0, float(score)))
    except Exception:
        return 0.0
    return 0.0


# ──────────────────────────────────────────────────────────
# UI HELPERS
# ──────────────────────────────────────────────────────────
def esg_hex(score: float) -> str:
    score = max(0.0, min(100.0, score))
    if score <= 50:
        t = score / 50.0
        r = 239; g = int(68 + t * (180 - 68)); b = int(68 + t * (8 - 68))
    else:
        t = (score - 50.0) / 50.0
        r = int(234 + t * (34 - 234))
        g = int(180 + t * (197 - 180))
        b = int(8 + t * (94 - 8))
    return f"#{r:02x}{g:02x}{b:02x}"


def progress_ring_html(score: float, subtitle: str = "ESG Score") -> str:
    col = esg_hex(score)
    R = 52
    circ = 2 * np.pi * R
    dash = (score / 100) * circ
    gap = circ - dash
    return f"""
    <div style="display:flex;flex-direction:column;align-items:center;gap:6px;padding:8px 0;">
      <svg width="154" height="154" viewBox="0 0 120 120">
        <circle cx="60" cy="60" r="{R}" fill="none" stroke="{col}33" stroke-width="13"/>
        <circle cx="60" cy="60" r="{R}" fill="none" stroke="{col}" stroke-width="13"
                stroke-dasharray="{dash:.2f} {gap:.2f}" stroke-linecap="round"
                transform="rotate(-90 60 60)"/>
        <text x="60" y="55" text-anchor="middle" font-family="Inter,sans-serif"
              font-size="22" font-weight="700" fill="{col}">{score:.1f}</text>
        <text x="60" y="71" text-anchor="middle" font-family="Inter,sans-serif"
              font-size="11" fill="#94a3b8">/ 100</text>
      </svg>
      <span style="font-size:12px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#8ea593;">{subtitle}</span>
    </div>"""


def alloc_bar_html(w1, w2, name1, name2):
    c1, c2 = "#2e7d36", "#3b82f6"
    p1 = f"{w1*100:.1f}%"; p2 = f"{w2*100:.1f}%"
    return f"""
    <div class="bar-row">
      <div class="bar-label-row">
        <span style="color:{c1};">{name1}</span>
        <span style="color:{c1};">{p1}</span>
      </div>
      <div class="bar-track">
        <div class="bar-fill" style="width:{p1};background:{c1};"></div>
      </div>
    </div>
    <div class="bar-row" style="margin-top:12px;">
      <div class="bar-label-row">
        <span style="color:{c2};">{name2}</span>
        <span style="color:{c2};">{p2}</span>
      </div>
      <div class="bar-track">
        <div class="bar-fill" style="width:{p2};background:{c2};"></div>
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
    cls = "chip-pos" if value > 0.001 else ("chip-neg" if value < -0.001 else "chip-neu")
    return f'<span class="chip {cls}">{fmt}</span>'


def get_agency_input(name, agency, key_pref):
    if agency == "MSCI":
        val = st.selectbox(
            f"{name} MSCI Rating",
            ["CCC", "B", "BB", "BBB", "A", "AA", "AAA"],
            index=3,
            key=f"{key_pref}_m",
        )
    elif agency == "Refinitiv":
        val = st.number_input(f"{name} Score (0–5)", 0, 5, 3, key=f"{key_pref}_r")
    else:
        val = st.number_input(f"{name} Score", value=50.0, key=f"{key_pref}_s")
    return convert_to_100(val, agency)


def asset_card(asset_label, name_key, ret_key, sd_key, agency_key, default_name, default_ret, default_sd):
    c1, c2 = st.columns([1.15, 1])
    with c1:
        name = st.text_input(asset_label + " name", default_name, key=name_key, label_visibility="collapsed")
    with c2:
        agency = st.selectbox(
            asset_label + " rating agency",
            ["S&P", "MSCI", "Sustainalytics", "Refinitiv"],
            key=agency_key,
            label_visibility="collapsed",
        )
    c3, c4 = st.columns(2)
    with c3:
        ret = st.number_input(f"{asset_label} return %", value=default_ret, key=ret_key, label_visibility="collapsed") / 100
    with c4:
        sd = st.number_input(f"{asset_label} volatility %", value=default_sd, key=sd_key, label_visibility="collapsed") / 100
    st.caption("Return % · Volatility % · Rating agency")
    return name, ret, sd, agency


# ──────────────────────────────────────────────────────────
# HEADER
# ──────────────────────────────────────────────────────────
st.markdown(
    """
<div class="hero">
  <h1>🌱 Ethos Invest Portfolio Analysis Tool</h1>
  <p>Compare investments based on financial performance, risk, and ESG alignment. The interface below keeps the original structure, but presents it in a cleaner, more premium layout.</p>
  <div class="hero-badge">Premium ESG portfolio interface</div>
</div>
""",
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────────────────
# SECTION 1 · ASSETS & MARKET DATA
# ──────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Assets & Market Data</div>', unsafe_allow_html=True)
asset_col1, asset_col2 = st.columns(2, gap="large")

with asset_col1:
    st.markdown('<div class="card"><div class="card-title">Asset 1</div>', unsafe_allow_html=True)
    asset1_name, r1, sd1, agency1 = asset_card("Asset 1", "asset1_name", "r1", "sd1", "ag1", "Apple", 8.0, 15.0)
    st.markdown('</div>', unsafe_allow_html=True)

with asset_col2:
    st.markdown('<div class="card"><div class="card-title">Asset 2</div>', unsafe_allow_html=True)
    asset2_name, r2, sd2, agency2 = asset_card("Asset 2", "asset2_name", "r2", "sd2", "ag2", "Microsoft", 10.0, 20.0)
    st.markdown('</div>', unsafe_allow_html=True)

market_col1, market_col2 = st.columns(2, gap="large")
with market_col1:
    st.markdown('<div class="card"><div class="card-title">Market Correlation</div>', unsafe_allow_html=True)
    rho = st.slider("Correlation Coefficient (ρ)", -1.0, 1.0, 0.2, 0.01, label_visibility="collapsed")
    st.markdown('<div class="card-subtitle">Controls diversification between the two assets.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
with market_col2:
    st.markdown('<div class="card"><div class="card-title">Risk-Free Rate</div>', unsafe_allow_html=True)
    r_free = st.number_input("Risk-free Rate %", value=2.0, label_visibility="collapsed") / 100
    st.markdown('<div class="card-subtitle">Used in the Sharpe ratio and capital market line.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────
# SECTION 2 · ESG PREFERENCE
# ──────────────────────────────────────────────────────────
st.markdown('<div class="section-label">ESG Preference</div>', unsafe_allow_html=True)

pref_col1, pref_col2 = st.columns([1.35, 1], gap="large")
with pref_col1:
    st.markdown('<div class="card"><div class="card-title">Discover your ESG preference</div>', unsafe_allow_html=True)
    st.markdown('<div class="helper-line">Answer a few concrete questions first. The app will infer a starting ESG preference, then let you refine it.</div>', unsafe_allow_html=True)

    q1 = st.selectbox(
        "Would you invest in a company with strong returns but weaker environmental impact?",
        ["1. No, never", "2. Only with a large return premium", "3. It depends", "4. Usually yes", "5. Yes, returns matter most"],
        key="esg_q1",
    )
    q2 = st.selectbox(
        "Which portfolio would you prefer?",
        ["1. 10% return, ESG 40", "2. 9% return, ESG 55", "3. 8.5% return, ESG 65", "4. 8% return, ESG 80", "5. 7% return, ESG 90"],
        key="esg_q2",
    )
    q3 = st.selectbox(
        "How would you feel if ESG constraints reduced return by around 2%?",
        ["1. Very uncomfortable", "2. Uncomfortable", "3. Neutral", "4. Comfortable", "5. Very comfortable"],
        key="esg_q3",
    )
    q4 = st.selectbox(
        "Which statement best describes you?",
        ["1. I maximise returns", "2. I lean toward returns", "3. I want balance", "4. I lean toward sustainability", "5. I prioritise sustainability"],
        key="esg_q4",
    )

    q_scores = [int(q[0]) for q in [q1, q2, q3, q4]]
    avg_score = sum(q_scores) / len(q_scores)
    if avg_score <= 1.5:
        inferred_lambda, pref_label = 0.0, "Return-focused"
        pref_note = "Very little willingness to sacrifice return for ESG."
    elif avg_score <= 2.4:
        inferred_lambda, pref_label = 0.25, "Light ESG preference"
        pref_note = "Some ESG interest, but return remains the priority."
    elif avg_score <= 3.4:
        inferred_lambda, pref_label = 0.60, "Balanced ESG investor"
        pref_note = "A measured willingness to trade some return for ESG alignment."
    elif avg_score <= 4.2:
        inferred_lambda, pref_label = 0.85, "ESG-led investor"
        pref_note = "Strong preference for sustainability even with some return trade-off."
    else:
        inferred_lambda, pref_label = 1.0, "Impact-focused investor"
        pref_note = "Maximum ESG emphasis, even if returns are reduced."

    refine_col1, refine_col2 = st.columns([1.1, 0.9], gap="medium")
    with refine_col1:
        lambda_esg = st.slider(
            "Refine your ESG preference",
            0.0,
            1.0,
            float(inferred_lambda),
            0.05,
            help="0 = no ESG sacrifice, 1 = maximum ESG priority",
            key="lambda_esg",
        )
    with refine_col2:
        st.markdown(
            f"""
            <div style="padding-top:8px;">
                <div style="font-size:10px;letter-spacing:0.16em;text-transform:uppercase;color:#52c98a;font-weight:700;margin-bottom:6px;">Inferred profile</div>
                <div style="font-size:18px;font-weight:700;color:#eef2f7;margin-bottom:6px;">{pref_label}</div>
                <div style="font-size:12px;color:#9ca3af;line-height:1.5;">{pref_note}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        f"""
        <div style="margin-top:10px;" class="info-box">
            Based on your answers, the app starts from an ESG preference of <strong>{inferred_lambda:.2f}</strong> and lets you fine-tune it above.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

with pref_col2:
    st.markdown('<div class="card"><div class="card-title">Preference summary</div>', unsafe_allow_html=True)
    st.markdown(progress_ring_html(lambda_esg * 100, "ESG Preference"), unsafe_allow_html=True)
    st.markdown(f"<div class='helper-line' style='text-align:center;'>Current preference strength: <strong>{lambda_esg:.2f}</strong><br>Higher values place more weight on ESG alignment.</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="fancy-divider">', unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────
# SECTION 3 · ESG SCORES
# ──────────────────────────────────────────────────────────
st.markdown('<div class="section-label">ESG Scores</div>', unsafe_allow_html=True)

esg_method = st.radio(
    "How would you like to enter ESG data?",
    ["Overall ESG Score", "Separate E, S, and G Pillars"],
    horizontal=True,
    key="esg_method",
)

weights_ok = True
w_e = w_s = w_g = 33

if esg_method == "Separate E, S, and G Pillars":
    st.markdown('<div class="card"><div class="card-title">Pillar weights</div>', unsafe_allow_html=True)

    weight_method = st.radio(
        "How would you like to set pillar weights?",
        ["Manual Entry", "Materiality Assessment"],
        horizontal=True,
        key="weight_method",
    )

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

        selected = st.multiselect(
            "Select up to 4 ESG issues that matter most to you",
            list(TOPICS.keys()),
            max_selections=4,
            key="mat_topics",
        )

        counts = {"E": 0, "S": 0, "G": 0}
        for topic in selected:
            counts[TOPICS[topic]] += 1

        floor = 0.10
        raw = {k: max(counts[k], floor) for k in counts}
        total = sum(raw.values())
        sug_e = round((raw["E"] / total) * 100)
        sug_s = round((raw["S"] / total) * 100)
        sug_g = 100 - sug_e - sug_s

        if len(selected) == 4:
            st.success(f"Suggested weights — E: {sug_e}% · S: {sug_s}% · G: {sug_g}%")
        else:
            st.caption(f"{4 - len(selected)} more selection(s) needed.")
            sug_e, sug_s, sug_g = 34, 33, 33

        st.markdown('<div class="card-subtitle">Review and adjust the suggested weights below.</div>', unsafe_allow_html=True)
    else:
        sug_e, sug_s, sug_g = 34, 33, 33

    cw1, cw2, cw3 = st.columns(3, gap="small")
    with cw1:
        w_e = st.number_input("E %", 0, 100, sug_e, key="we")
    with cw2:
        w_s = st.number_input("S %", 0, 100, sug_s, key="ws")
    with cw3:
        w_g = st.number_input("G %", 0, 100, sug_g, key="wg")

    weights_ok = (w_e + w_s + w_g) == 100
    if not weights_ok:
        st.warning(f"Weights sum to {w_e+w_s+w_g}% — must equal 100%.")

    st.markdown('</div>', unsafe_allow_html=True)

esg_col1, esg_col2 = st.columns(2, gap="large")
with esg_col1:
    st.markdown(f'<div class="card"><div class="card-title">{asset1_name}</div>', unsafe_allow_html=True)
    if esg_method == "Overall ESG Score":
        esg1_100 = get_agency_input(asset1_name, agency1, "o1")
    else:
        e1 = get_agency_input(f"{asset1_name} E", agency1, "p1e")
        s1 = get_agency_input(f"{asset1_name} S", agency1, "p1s")
        g1 = get_agency_input(f"{asset1_name} G", agency1, "p1g")
        esg1_100 = (w_e / 100) * e1 + (w_s / 100) * s1 + (w_g / 100) * g1
    st.caption(f"Normalised: **{esg1_100:.1f} / 100**")
    st.markdown('</div>', unsafe_allow_html=True)

with esg_col2:
    st.markdown(f'<div class="card"><div class="card-title">{asset2_name}</div>', unsafe_allow_html=True)
    if esg_method == "Overall ESG Score":
        esg2_100 = get_agency_input(asset2_name, agency2, "o2")
    else:
        e2 = get_agency_input(f"{asset2_name} E", agency2, "p2e")
        s2 = get_agency_input(f"{asset2_name} S", agency2, "p2s")
        g2 = get_agency_input(f"{asset2_name} G", agency2, "p2g")
        esg2_100 = (w_e / 100) * e2 + (w_s / 100) * s2 + (w_g / 100) * g2
    st.caption(f"Normalised: **{esg2_100:.1f} / 100**")
    st.markdown('</div>', unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────
# ACTION BUTTON
# ──────────────────────────────────────────────────────────
st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
run_col1, run_col2, run_col3 = st.columns([1, 1.2, 1])
with run_col2:
    run = st.button("Calculate Portfolio ›", key="run")

if not run:
    st.markdown(
        """
        <div class="info-box">
          Fill in the inputs above, refine the ESG preference, then click <strong>Calculate Portfolio</strong> to see the results.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.stop()

if not weights_ok:
    st.markdown(
        """
        <div class="warn-box">
          ESG pillar weights must sum to 100%. Please adjust them above.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.stop()

# ──────────────────────────────────────────────────────────
# CALCULATIONS
# ──────────────────────────────────────────────────────────
esg_threshold = min(esg1_100, esg2_100) + lambda_esg * (max(esg1_100, esg2_100) - min(esg1_100, esg2_100))

weights = np.linspace(0, 1, 1000)
rets = portfolio_return(weights, r1, r2)
vols = portfolio_sd(weights, sd1, sd2, rho)
esgs = portfolio_esg(weights, esg1_100, esg2_100)
sharpes = (rets - r_free) / vols

idx_all = np.argmax(sharpes)
eligible = np.where(esgs >= esg_threshold)[0]

if len(eligible) == 0:
    st.error("No portfolios satisfy the ESG threshold. Try reducing your ESG preference.")
    st.stop()

idx_esg = eligible[np.argmax(sharpes[eligible])]

w1_all = weights[idx_all]; w1_esg = weights[idx_esg]
ret_all = rets[idx_all]; ret_esg = rets[idx_esg]
vol_all = vols[idx_all]; vol_esg = vols[idx_esg]
esg_all = esgs[idx_all]; esg_opt = esgs[idx_esg]
sh_all = sharpes[idx_all]; sh_esg = sharpes[idx_esg]

d_ret = ret_esg - ret_all
d_sd = vol_esg - vol_all
d_esg = esg_opt - esg_all

w1_mv = (sd2**2 - rho * sd1 * sd2) / (sd1**2 + sd2**2 - 2 * rho * sd1 * sd2)
w1_mv = float(np.clip(w1_mv, 0, 1))
ret_mv = portfolio_return(w1_mv, r1, r2)
vol_mv = portfolio_sd(w1_mv, sd1, sd2, rho)
esg_mv = portfolio_esg(w1_mv, esg1_100, esg2_100)
sh_mv = (ret_mv - r_free) / vol_mv if vol_mv > 0 else 0

# ──────────────────────────────────────────────────────────
# SECTION 1 · ESG OPTIMAL PORTFOLIO
# ──────────────────────────────────────────────────────────
st.markdown('<div class="section-label">ESG Optimal Portfolio</div>', unsafe_allow_html=True)

col_alloc, col_ring, col_metrics = st.columns([2.4, 1.1, 2.4], gap="large")

with col_alloc:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">Asset Allocation</div>
        {alloc_bar_html(w1_esg, 1 - w1_esg, asset1_name, asset2_name)}
    </div>
    """, unsafe_allow_html=True)

with col_ring:
    st.markdown(progress_ring_html(esg_opt, "Portfolio ESG"), unsafe_allow_html=True)

with col_metrics:
    st.markdown(metric_tile("Expected Return", f"{ret_esg*100:.2f}%", "Annualised"), unsafe_allow_html=True)
    st.markdown(metric_tile("Risk (Std Dev)", f"{vol_esg*100:.2f}%", "Annualised"), unsafe_allow_html=True)
    st.markdown(metric_tile("Sharpe Ratio", f"{sh_esg:.4f}", "Risk-adjusted return"), unsafe_allow_html=True)

st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
st.markdown('<hr class="fancy-divider">', unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────
# SECTION 2 · PORTFOLIO COMPARISON TABLE
# ──────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Portfolio Comparison</div>', unsafe_allow_html=True)

table_rows = [
    (f"{asset1_name} weight", f"{w1_esg*100:.2f}%", f"{w1_all*100:.2f}%", f"{w1_mv*100:.2f}%"),
    (f"{asset2_name} weight", f"{(1-w1_esg)*100:.2f}%", f"{(1-w1_all)*100:.2f}%", f"{(1-w1_mv)*100:.2f}%"),
    ("Expected return", f"{ret_esg*100:.2f}%", f"{ret_all*100:.2f}%", f"{ret_mv*100:.2f}%"),
    ("Risk (Std Dev)", f"{vol_esg*100:.2f}%", f"{vol_all*100:.2f}%", f"{vol_mv*100:.2f}%"),
    ("ESG score (0–100)", f"{esg_opt:.2f}", f"{esg_all:.2f}", f"{esg_mv:.2f}"),
    ("Sharpe ratio", f"{sh_esg:.4f}", f"{sh_all:.4f}", f"{sh_mv:.4f}"),
]

table_html = """
<table class="cmp-table">
  <thead><tr>
    <th>Metric</th>
    <th>✅ ESG-Constrained</th>
    <th>📈 Unconstrained</th>
    <th>🛡️ Min Variance</th>
  </tr></thead>
  <tbody>
"""
for r in table_rows:
    table_html += f"<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td></tr>"
table_html += "</tbody></table>"
st.markdown(table_html, unsafe_allow_html=True)

st.markdown('<div class="section-label">Allocation Breakdown</div>', unsafe_allow_html=True)
bar_col1, bar_col2, bar_col3 = st.columns(3, gap="large")

def alloc_card_html(title, w1, w2, name1, name2):
    c1, c2 = "#52c98a", "#3b82f6"
    p1 = f"{w1*100:.1f}%"
    p2 = f"{w2*100:.1f}%"
    return f"""
    <div class="card">
      <div class="card-title">{title}</div>
      <div class="bar-row">
        <div class="bar-label-row">
          <span style="color:{c1};">{name1}</span>
          <span style="color:{c1};font-family:'JetBrains Mono',monospace;">{p1}</span>
        </div>
        <div class="bar-track">
          <div class="bar-fill" style="width:{p1};background:linear-gradient(90deg,#1f6b42,{c1});"></div>
        </div>
      </div>
      <div class="bar-row" style="margin-top:12px;">
        <div class="bar-label-row">
          <span style="color:{c2};">{name2}</span>
          <span style="color:{c2};font-family:'JetBrains Mono',monospace;">{p2}</span>
        </div>
        <div class="bar-track">
          <div class="bar-fill" style="width:{p2};background:linear-gradient(90deg,#1e40af,{c2});"></div>
        </div>
      </div>
    </div>"""

with bar_col1:
    st.markdown(alloc_card_html("ESG Constrained", w1_esg, 1-w1_esg, asset1_name, asset2_name), unsafe_allow_html=True)
with bar_col2:
    st.markdown(alloc_card_html("Unconstrained", w1_all, 1-w1_all, asset1_name, asset2_name), unsafe_allow_html=True)
with bar_col3:
    st.markdown(alloc_card_html("Min Variance", w1_mv, 1-w1_mv, asset1_name, asset2_name), unsafe_allow_html=True)

st.markdown('<hr class="fancy-divider">', unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────
# SECTION 3 · IMPACT OF ESG CONSTRAINT
# ──────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Impact of ESG Constraint</div>', unsafe_allow_html=True)

ic1, ic2, ic3 = st.columns(3, gap="large")
with ic1:
    st.markdown(f"""
    <div class="card" style="text-align:center;">
      <div class="card-title" style="text-align:center;margin-bottom:8px;">Return change</div>
      {chip_html(d_ret * 100, " pp")}
      <div class="card-subtitle" style="text-align:center;margin-top:8px;">vs unconstrained</div>
    </div>""", unsafe_allow_html=True)
with ic2:
    st.markdown(f"""
    <div class="card" style="text-align:center;">
      <div class="card-title" style="text-align:center;margin-bottom:8px;">Risk change</div>
      {chip_html(d_sd * 100, " pp")}
      <div class="card-subtitle" style="text-align:center;margin-top:8px;">vs unconstrained</div>
    </div>""", unsafe_allow_html=True)
with ic3:
    st.markdown(f"""
    <div class="card" style="text-align:center;">
      <div class="card-title" style="text-align:center;margin-bottom:8px;">ESG score gain</div>
      {chip_html(d_esg, " pts", decimals=1)}
      <div class="card-subtitle" style="text-align:center;margin-top:8px;">vs unconstrained</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if idx_all == idx_esg:
    st.markdown(
        """
        <div class="info-box">
          The unconstrained optimal portfolio already meets your ESG threshold — applying the constraint has no material effect on the allocation.
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        f"""
        <div class="info-box">
          Your ESG preference requires a minimum portfolio score of <strong>{esg_threshold:.2f}</strong>.
          The portfolio was adjusted to meet this, shifting weight toward the higher-rated asset.
          The chips above show the cost (return / risk) and benefit (ESG score) of that tilt.
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<hr class="fancy-divider">', unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────
# SECTION 4 · CHARTS
# ──────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Charts</div>', unsafe_allow_html=True)

plt.rcParams.update({
    "font.family": "sans-serif",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.25,
    "grid.linestyle": "--",
})

w_plot = np.linspace(-0.5, 1.5, 500)
r_plot = portfolio_return(w_plot, r1, r2)
v_plot = portfolio_sd(w_plot, sd1, sd2, rho)

sd_max = max(v_plot) * 1.05
sd_range = np.linspace(0, sd_max, 300)
cml_all = r_free + ((ret_all - r_free) / vol_all) * sd_range
cml_esg = r_free + ((ret_esg - r_free) / vol_esg) * sd_range

chart_col1, chart_col2 = st.columns(2, gap="large")

with chart_col1:
    fig1, ax1 = plt.subplots(figsize=(6, 5))
    fig1.patch.set_facecolor("#f7faf7")
    ax1.set_facecolor("#f7faf7")

    ax1.plot(v_plot, r_plot, color="#94a3b8", lw=1.5, alpha=0.5, label="Full frontier")
    ax1.plot(sd_range, cml_all, "--", color="#94a3b8", lw=1.5, label="CML (unconstrained)")
    ax1.plot(sd_range, cml_esg, "--", color="#16a34a", lw=1.5, label="CML (ESG)")
    ax1.scatter(0, r_free, marker="s", s=80, color="#0d1f0f", zorder=5, label="Risk-free asset")
    ax1.scatter(vol_all, ret_all, marker="*", s=220, color="#64748b", edgecolors="white", linewidths=0.8, zorder=6, label="Optimal (unconstrained)")
    ax1.scatter(vol_esg, ret_esg, marker="*", s=220, color="#16a34a", edgecolors="white", linewidths=0.8, zorder=7, label="Optimal (ESG)")

    ax1.annotate("Unconstrained", (vol_all, ret_all), xytext=(-6, -16), textcoords="offset points", fontsize=8, color="#64748b")
    ax1.annotate("ESG optimal", (vol_esg, ret_esg), xytext=(8, 6), textcoords="offset points", fontsize=8, color="#16a34a")

    ax1.set_xlim(0, max(v_plot) * 1.02)
    ax1.xaxis.set_major_formatter(PercentFormatter(1.0))
    ax1.yaxis.set_major_formatter(PercentFormatter(1.0))
    ax1.set_xlabel("Risk (Standard Deviation)", fontsize=11)
    ax1.set_ylabel("Expected Return", fontsize=11)
    ax1.set_title("Efficient Frontier & Capital Market Lines", fontsize=13, fontweight="bold", color="#0d1f0f")
    ax1.legend(fontsize=7.5)
    plt.tight_layout()
    st.pyplot(fig1)
    st.caption("Stars mark the tangency (highest Sharpe) portfolio for each case.")

with chart_col2:
    fig2, ax2 = plt.subplots(figsize=(6, 5))
    fig2.patch.set_facecolor("#f7faf7")
    ax2.set_facecolor("#f7faf7")

    ax2.plot(esgs, sharpes, color="#ef4444", lw=2.5, label="ESG–Sharpe frontier")
    ax2.axvline(esg_threshold, color="#f59e0b", lw=1.5, linestyle=":", label=f"ESG threshold ({esg_threshold:.1f})")
    ax2.scatter(esg_all, sh_all, marker="*", s=220, color="#64748b", edgecolors="white", linewidths=0.8, zorder=5, label="Optimal (unconstrained)")
    ax2.scatter(esg_opt, sh_esg, marker="*", s=220, color="#16a34a", edgecolors="white", linewidths=0.8, zorder=6, label="Optimal (ESG)")

    ax2.annotate("Unconstrained", (esg_all, sh_all), xytext=(-6, -16), textcoords="offset points", fontsize=8, color="#64748b")
    ax2.annotate("ESG optimal", (esg_opt, sh_esg), xytext=(8, 6), textcoords="offset points", fontsize=8, color="#16a34a")

    ax2.set_xlabel("Portfolio ESG Score (0–100)", fontsize=11)
    ax2.set_ylabel("Sharpe Ratio", fontsize=11)
    ax2.set_title("ESG–Sharpe Ratio Trade-off", fontsize=13, fontweight="bold", color="#0d1f0f")
    ax2.legend(fontsize=7.5)
    plt.tight_layout()
    st.pyplot(fig2)
    st.caption("Amber dotted line marks your minimum ESG threshold.")

# ──────────────────────────────────────────────────────────
# FOOTER
# ──────────────────────────────────────────────────────────
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    """
<div style="text-align:center;font-size:12px;color:#94a3b8;padding:16px 0;">
  Ethos Invest · Sustainable Finance Portfolio Tool · For illustrative purposes only — not financial advice.
</div>
""",
    unsafe_allow_html=True,
)
