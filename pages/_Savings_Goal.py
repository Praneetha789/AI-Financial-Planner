import streamlit as st
from database.db import get_all_expenses

st.set_page_config(
    page_title="Savings Goal",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Savings Goal Tracker")

# -----------------------------
# Load expenses
# -----------------------------
rows = get_all_expenses()

if not rows:
    st.info("No expenses found. Add expenses first.")
    st.stop()

total_expenses = sum(row[2] for row in rows)

# -----------------------------
# User input
# -----------------------------
goal = st.number_input(
    "Enter your Savings Goal (₹)",
    min_value=1000,
    step=1000
)

# -----------------------------
# Calculations
# -----------------------------
income_assumption = total_expenses * 2  # simple assumption for now
savings = income_assumption - total_expenses

progress = 0
if goal > 0:
    progress = (savings / goal) * 100
    progress = min(progress, 100)

# -----------------------------
# Display
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("💸 Total Expenses", f"₹{total_expenses:,.0f}")
col2.metric("💰 Estimated Savings", f"₹{savings:,.0f}")
col3.metric("📊 Progress", f"{progress:.1f}%")

st.progress(progress / 100)

# -----------------------------
# Status
# -----------------------------
if progress >= 100:
    st.success("🎉 Goal achieved! Great job!")
elif progress >= 70:
    st.info("🔥 You are close to your goal!")
elif progress >= 40:
    st.warning("⚠️ You are halfway there.")
else:
    st.error("🚨 You need to save more!")