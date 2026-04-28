import pandas as pd
import numpy as np
import joblib
import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CropSense AI",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&display=swap');

/* ── Reset & base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"] {
    background: #0b1a12 !important;
    font-family: 'DM Sans', sans-serif;
    color: #e8f0eb;
}

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(ellipse 80% 60% at 50% -10%, #1a4a2e55 0%, transparent 70%),
        radial-gradient(ellipse 40% 40% at 90% 80%, #0d3b2244 0%, transparent 60%),
        #0b1a12 !important;
}

/* Remove streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stToolbar"] { display: none; }
[data-testid="stDecoration"] { display: none; }
section[data-testid="stSidebar"] { display: none; }

/* ── Hero section ── */
.hero {
    text-align: center;
    padding: 3.5rem 1rem 2rem;
    position: relative;
}
.hero-eyebrow {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.75rem;
    font-weight: 500;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: #5dba7e;
    margin-bottom: 1rem;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
}
.hero-eyebrow::before,
.hero-eyebrow::after {
    content: '';
    display: block;
    width: 32px;
    height: 1px;
    background: #5dba7e88;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.8rem, 6vw, 5rem);
    font-weight: 900;
    line-height: 1.08;
    color: #f0f7f2;
    margin-bottom: 1rem;
    letter-spacing: -0.02em;
}
.hero-title span {
    color: #5dba7e;
    font-style: italic;
}
.hero-sub {
    font-size: 1rem;
    color: #8daa96;
    max-width: 480px;
    margin: 0 auto 2.5rem;
    line-height: 1.7;
    font-weight: 300;
}
.hero-divider {
    width: 60px;
    height: 2px;
    background: linear-gradient(90deg, transparent, #5dba7e, transparent);
    margin: 0 auto 2.8rem;
}

/* ── Card wrapper ── */
.form-card {
    background: linear-gradient(145deg, #122218ee, #0e1e14ee);
    border: 1px solid #1e3d28;
    border-radius: 20px;
    padding: 2.2rem 2rem;
    margin-bottom: 1.5rem;
    backdrop-filter: blur(8px);
    position: relative;
    overflow: hidden;
}
.form-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, #5dba7e66, transparent);
}
.section-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.68rem;
    font-weight: 500;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #5dba7e;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.6rem;
}
.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: #1e3d28;
}

/* ── Streamlit number inputs ── */
[data-testid="stNumberInput"] label {
    font-size: 0.78rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.04em !important;
    color: #7da888 !important;
    text-transform: uppercase !important;
    margin-bottom: 4px !important;
}
[data-testid="stNumberInput"] input {
    background: #0b1a12 !important;
    border: 1px solid #1e3d28 !important;
    border-radius: 10px !important;
    color: #e8f0eb !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1rem !important;
    padding: 0.6rem 0.9rem !important;
    transition: border-color 0.2s, box-shadow 0.2s;
}
[data-testid="stNumberInput"] input:focus {
    border-color: #5dba7e !important;
    box-shadow: 0 0 0 3px #5dba7e22 !important;
    outline: none !important;
}
[data-testid="stNumberInput"] button {
    background: #1a3325 !important;
    border-color: #1e3d28 !important;
    color: #5dba7e !important;
}

/* ── Submit button ── */
[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #5dba7e, #3a9960) !important;
    color: #0b1a12 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.04em !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.85rem 2.5rem !important;
    width: 100% !important;
    cursor: pointer !important;
    transition: transform 0.15s, box-shadow 0.15s !important;
    box-shadow: 0 4px 20px #5dba7e33 !important;
}
[data-testid="stButton"] > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px #5dba7e55 !important;
}
[data-testid="stButton"] > button:active {
    transform: translateY(0) !important;
}

/* ── Result card ── */
.result-card {
    background: linear-gradient(135deg, #152e1e, #0e2218);
    border: 1px solid #2a5e3a;
    border-radius: 20px;
    padding: 2.5rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    animation: fadeIn 0.5s ease;
}
.result-card::after {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse 60% 50% at 50% 100%, #5dba7e0d, transparent);
    pointer-events: none;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
}
.result-emoji {
    font-size: 3.5rem;
    margin-bottom: 0.8rem;
    display: block;
    filter: drop-shadow(0 4px 16px #5dba7e44);
}
.result-label {
    font-size: 0.7rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #5dba7e;
    margin-bottom: 0.4rem;
    font-weight: 500;
}
.result-crop {
    font-family: 'Playfair Display', serif;
    font-size: 2.6rem;
    font-weight: 900;
    color: #f0f7f2;
    letter-spacing: -0.01em;
    line-height: 1.15;
}
.result-note {
    margin-top: 0.8rem;
    font-size: 0.85rem;
    color: #6a9474;
    font-weight: 300;
}

/* ── Metrics row ── */
.metrics-row {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.5rem;
    flex-wrap: wrap;
}
.metric-pill {
    flex: 1 1 100px;
    background: #122218;
    border: 1px solid #1e3d28;
    border-radius: 12px;
    padding: 0.9rem 1rem;
    text-align: center;
}
.metric-pill .val {
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    font-weight: 700;
    color: #5dba7e;
    line-height: 1;
}
.metric-pill .key {
    font-size: 0.65rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #5a7a63;
    margin-top: 4px;
    font-weight: 500;
}

/* ── Footer ── */
.footer {
    text-align: center;
    padding: 2rem 1rem 3rem;
    font-size: 0.75rem;
    color: #3a5a44;
    letter-spacing: 0.05em;
}
</style>
""", unsafe_allow_html=True)

# ── Load model ────────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    return joblib.load("Crop_Recommendation.pkl")

try:
    loaded_model = load_model()
    model_loaded = True
except Exception:
    model_loaded = False

# ── Decode dict ───────────────────────────────────────────────────────────────
decode_dict = {
    0: "Rice", 1: "Maize", 2: "Jute", 3: "Cotton", 4: "Coconut",
    5: "Papaya", 6: "Orange", 7: "Apple", 8: "Muskmelon", 9: "Watermelon",
    10: "Grapes", 11: "Mango", 12: "Banana", 13: "Pomegranate", 14: "Lentil",
    15: "Blackgram", 16: "Mungbean", 17: "Mothbeans", 18: "Pigeonpeas",
    19: "Kidneybeans", 20: "Chickpea", 21: "Coffee",
}

crop_emoji = {
    "Rice": "🌾", "Maize": "🌽", "Jute": "🌿", "Cotton": "🤍", "Coconut": "🥥",
    "Papaya": "🍈", "Orange": "🍊", "Apple": "🍎", "Muskmelon": "🍈",
    "Watermelon": "🍉", "Grapes": "🍇", "Mango": "🥭", "Banana": "🍌",
    "Pomegranate": "🍎", "Lentil": "🫘", "Blackgram": "🫘", "Mungbean": "🫘",
    "Mothbeans": "🫘", "Pigeonpeas": "🫘", "Kidneybeans": "🫘",
    "Chickpea": "🫘", "Coffee": "☕",
}

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-eyebrow">AI-powered agronomy</div>
    <h1 class="hero-title">Grow the <span>right crop</span>,<br>at the right time.</h1>
    <p class="hero-sub">Enter your soil and climate parameters below. Our model will recommend the ideal crop for your land.</p>
    <div class="hero-divider"></div>
</div>
""", unsafe_allow_html=True)

# ── Layout: 2 columns ─────────────────────────────────────────────────────────
col_left, col_right = st.columns([1.1, 1], gap="large")

with col_left:
    # Soil nutrients
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">🧪 Soil Nutrients</div>', unsafe_allow_html=True)
    n1, n2, n3 = st.columns(3)
    with n1:
        N = st.number_input("Nitrogen (N)", min_value=0.0, max_value=200.0,
                            value=50.0, step=1.0, format="%.1f")
    with n2:
        P = st.number_input("Phosphorus (P)", min_value=0.0, max_value=200.0,
                            value=40.0, step=1.0, format="%.1f")
    with n3:
        K = st.number_input("Potassium (K)", min_value=0.0, max_value=200.0,
                            value=40.0, step=1.0, format="%.1f")
    st.markdown('</div>', unsafe_allow_html=True)

    # Climate conditions
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">🌤 Climate Conditions</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        temperature = st.number_input("Temperature (°C)", min_value=-10.0, max_value=55.0,
                                      value=25.0, step=0.5, format="%.1f")
        ph = st.number_input("pH Level", min_value=0.0, max_value=14.0,
                             value=6.5, step=0.1, format="%.1f")
    with c2:
        humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0,
                                   value=70.0, step=1.0, format="%.1f")
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0,
                                   value=150.0, step=5.0, format="%.1f")
    st.markdown('</div>', unsafe_allow_html=True)

    # Submit
    predict_clicked = st.button("🌱  Recommend a Crop", use_container_width=True)

with col_right:
    # Input summary pills
    st.markdown(f"""
    <div class="form-card" style="margin-bottom:1.5rem;">
        <div class="section-label">📊 Input Summary</div>
        <div class="metrics-row">
            <div class="metric-pill"><div class="val">{N:.0f}</div><div class="key">Nitrogen</div></div>
            <div class="metric-pill"><div class="val">{P:.0f}</div><div class="key">Phosphorus</div></div>
            <div class="metric-pill"><div class="val">{K:.0f}</div><div class="key">Potassium</div></div>
        </div>
        <div class="metrics-row">
            <div class="metric-pill"><div class="val">{temperature:.1f}°</div><div class="key">Temp</div></div>
            <div class="metric-pill"><div class="val">{humidity:.0f}%</div><div class="key">Humidity</div></div>
            <div class="metric-pill"><div class="val">{ph:.1f}</div><div class="key">pH</div></div>
            <div class="metric-pill"><div class="val">{rainfall:.0f}</div><div class="key">Rain mm</div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Result
    if predict_clicked:
        if not model_loaded:
            st.error("⚠️ Model file not found. Place `Crop_Recommendation.pkl` in the app directory.")
        else:
            X_new = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            predicted_value = loaded_model.predict(X_new)[0]
            predicted_name = decode_dict.get(predicted_value, str(predicted_value))
            emoji = crop_emoji.get(predicted_name, "🌱")

            st.markdown(f"""
            <div class="result-card">
                <span class="result-emoji">{emoji}</span>
                <div class="result-label">Recommended Crop</div>
                <div class="result-crop">{predicted_name}</div>
                <p class="result-note">Based on your soil and climate profile,<br>this crop is your best match.</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="form-card" style="text-align:center; padding:3rem 2rem; border-style:dashed;">
            <div style="font-size:2.5rem; margin-bottom:1rem; opacity:.4;">🌿</div>
            <div style="font-size:0.8rem; letter-spacing:0.1em; text-transform:uppercase;
                        color:#3a5a44; font-weight:500;">
                Your recommendation<br>will appear here
            </div>
        </div>
        """, unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    CropSense AI · Powered by Machine Learning · Helping farmers grow smarter
</div>
""", unsafe_allow_html=True)