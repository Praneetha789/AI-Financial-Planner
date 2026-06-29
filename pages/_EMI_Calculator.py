import streamlit as st
import math

st.set_page_config(
    page_title="EMI Calculator",
    page_icon="🏦",
    layout="wide"
)

# -----------------------------
# FIXED GLOBAL THEME (NO TEXT LOSS)
# -----------------------------
st.markdown(
    """
    <style>

    .stApp {
        background-color: #0b1220;
        color: #ffffff;
    }

    /* Force ALL text visible */
    html, body, [class*="css"]  {
        color: #ffffff !important;
    }

    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: #ffffff !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0f172a;
    }

    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    /* Metrics */
    div[data-testid="metric-container"] {
        background-color: #111827;
        padding: 12px;
        border-radius: 10px;
        color: white !important;
    }

    /* Inputs */
    input {
        color: black !important;
    }

    /* Button */
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        height: 45px;
        width: 100%;
    }

    .stButton>button:hover {
        background-color: #1d4ed8;
        color: white;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# HEADER
# -----------------------------
st.title("🏦 EMI Calculator")
st.caption("Calculate your monthly loan EMI instantly")

st.divider()

# -----------------------------
# INPUTS
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    principal = st.number_input(
        "💰 Loan Amount (₹)",
        min_value=0.0,
        step=1000.0
    )

    rate = st.number_input(
        "📈 Interest Rate (% per year)",
        min_value=0.0,
        step=0.1
    )

with col2:
    tenure = st.number_input(
        "📅 Tenure (years)",
        min_value=0.0,
        step=1.0
    )

st.divider()

# -----------------------------
# CALCULATION
# -----------------------------
if st.button("📊 Calculate EMI"):

    if principal <= 0 or rate <= 0 or tenure <= 0:
        st.error("⚠ Please enter valid values")
        st.stop()

    monthly_rate = rate / (12 * 100)
    months = tenure * 12

    emi = (
        principal
        * monthly_rate
        * math.pow(1 + monthly_rate, months)
        / (math.pow(1 + monthly_rate, months) - 1)
    )

    total_payment = emi * months
    total_interest = total_payment - principal

    # -----------------------------
    # RESULTS
    # -----------------------------
    st.subheader("📋 EMI Summary")

    c1, c2, c3 = st.columns(3)

    c1.metric("💸 Monthly EMI", f"₹{emi:,.0f}")
    c2.metric("💰 Total Payment", f"₹{total_payment:,.0f}")
    c3.metric("📉 Total Interest", f"₹{total_interest:,.0f}")

    st.divider()

    # -----------------------------
    # TIP
    # -----------------------------
    st.success("💡 Tip: Making partial prepayments reduces interest significantly")