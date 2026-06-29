import streamlit as st

st.set_page_config(
    page_title="Investment Advisor",
    page_icon="📈",
    layout="wide"
)

# -----------------------------
# FIXED GLOBAL THEME
# -----------------------------
st.markdown(
    """
    <style>

    .stApp {
        background-color: #0b1220;
        color: #ffffff;
    }

    /* Force all text visible */
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
st.title("📈 Investment Advisor")
st.caption("Get smart investment suggestions based on your profile")

st.divider()

# -----------------------------
# INPUTS
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("🎂 Age", min_value=18, max_value=100, step=1)
    income = st.number_input("💰 Monthly Income (₹)", min_value=0.0, step=1000.0)

with col2:
    risk = st.selectbox(
        "⚖ Risk Level",
        ["Low", "Medium", "High"]
    )

    savings = st.number_input("💵 Monthly Savings (₹)", min_value=0.0, step=500.0)

st.divider()

# -----------------------------
# ADVISOR LOGIC
# -----------------------------
if st.button("🤖 Get Advice"):

    st.subheader("📊 Your Investment Plan")

    if risk == "Low":
        st.success("""
🟢 Safe Portfolio:

• Fixed Deposits (40%)
• Government Bonds (30%)
• Debt Mutual Funds (30%)

👉 Focus: Capital protection
""")

    elif risk == "Medium":
        st.info("""
🔵 Balanced Portfolio:

• Index Funds (40%)
• Hybrid Mutual Funds (30%)
• Fixed Deposits (30%)

👉 Focus: Growth + Safety
""")

    else:
        st.warning("""
🔴 Aggressive Portfolio:

• Stocks (50%)
• Index Funds (30%)
• Crypto / High risk assets (20%)

👉 Focus: High returns (high risk)
""")

    st.divider()

    # -----------------------------
    # SAVINGS CHECK
    # -----------------------------
    if income > 0 and savings < income * 0.2:
        st.error("⚠ Try increasing savings to at least 20% of income.")
    else:
        st.success("Great! You are maintaining a healthy savings rate 👍")