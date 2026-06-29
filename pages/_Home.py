import streamlit as st
from database.db import create_tables

create_tables()

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

# -----------------------------
# HERO SECTION
# -----------------------------
st.markdown(
    """
    <div style='text-align:center; padding:20px'>
        <h1>💰 AI Financial Planner</h1>
        <h4 style='color:gray;'>
            Track Expenses • Plan Budget • Grow Savings • Get AI Insights
        </h4>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# INTRO SECTION
# -----------------------------
st.subheader("👋 Welcome!")

st.write(
    "This application helps you manage your personal finances in a smart way. "
    "You can track expenses, plan budgets, set savings goals, and get AI-powered insights."
)

st.divider()

# -----------------------------
# FEATURE HIGHLIGHTS
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.success("📊 Expense Tracking\n\nRecord and analyze your daily spending easily.")

with col2:
    st.info("💰 Budget Planning\n\nPlan monthly budgets and avoid overspending.")

with col3:
    st.warning("🤖 AI Insights\n\nGet intelligent suggestions to improve your finances.")

st.divider()

# -----------------------------
# QUICK STATS
# -----------------------------
st.subheader("⚡ App Highlights")

c1, c2, c3, c4 = st.columns(4)

c1.metric("📱 Easy UI", "Simple")
c2.metric("📊 Analytics", "Real-time")
c3.metric("🤖 AI Advice", "Smart")
c4.metric("💰 Savings", "Improved")

st.divider()

# -----------------------------
# FOOTER
# -----------------------------
st.info(
    "👈 Use sidebar navigation: Dashboard | Expense Tracker | Budget Planner | Savings Goal | AI Advisor"
)