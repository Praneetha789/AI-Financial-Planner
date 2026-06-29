import streamlit as st
from database.db import create_tables

create_tables()

st.set_page_config(
    page_title="AI Financial Planner",
    page_icon="💰",
    layout="wide"
)

# -----------------------------
# HERO SECTION
# -----------------------------
st.markdown("""
<style>
.hero {
    padding: 2rem;
    border-radius: 15px;
    background: linear-gradient(135deg, #1f1f2e, #2c2c54);
    color: white;
    text-align: center;
}
.title {
    font-size: 42px;
    font-weight: bold;
}
.subtitle {
    font-size: 18px;
    opacity: 0.8;
}
.card {
    padding: 20px;
    border-radius: 12px;
    background-color: #111827;
    color: white;
}
</style>

<div class="hero">
    <div class="title">💰 AI Financial Planner</div>
    <div class="subtitle">
        Smart budgeting • Expense tracking • AI insights • Financial growth
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")

# -----------------------------
# FEATURE CARDS
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    📊 <b>Track Expenses</b><br>
    Monitor your daily spending in real-time.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    💰 <b>Smart Budgeting</b><br>
    Plan and control your monthly finances.
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    🤖 <b>AI Insights</b><br>
    Get intelligent financial advice.
    </div>
    """, unsafe_allow_html=True)

st.write("")

# -----------------------------
# FOOTER INFO
# -----------------------------
st.info("👈 Use the sidebar to navigate through the app")