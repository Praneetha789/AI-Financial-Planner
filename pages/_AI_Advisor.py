import streamlit as st
import pandas as pd
from database.db import get_all_expenses

st.set_page_config(
    page_title="AI Advisor",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Financial Advisor")

# -----------------------------
# Load data
# -----------------------------
rows = get_all_expenses()

if not rows:
    st.info("No data available. Add expenses first.")
    st.stop()

df = pd.DataFrame(
    rows,
    columns=["Date", "Category", "Amount", "Description"]
)

total = df["Amount"].sum()

category_spending = df.groupby("Category")["Amount"].sum()

st.subheader("📊 Financial Overview")
st.metric("💸 Total Spending", f"₹{total:,.0f}")

st.divider()

# -----------------------------
# AI Logic (Rule Based)
# -----------------------------
st.subheader("🤖 AI Insights")

insights = []

# Overspending check
if total > 50000:
    insights.append("🚨 You are spending too much overall. Try reducing expenses.")

# Category analysis
highest_category = category_spending.idxmax()
highest_value = category_spending.max()

insights.append(f"🔥 Your highest spending category is **{highest_category}** (₹{highest_value:,.0f})")

# Food check
if "Food" in category_spending and category_spending["Food"] > total * 0.3:
    insights.append("🍔 Food expenses are too high (>30%). Try cooking at home more.")

# Shopping check
if "Shopping" in category_spending and category_spending["Shopping"] > total * 0.25:
    insights.append("🛍 Shopping is high. Avoid impulse purchases.")

# Savings hint
if total < 20000:
    insights.append("💰 Good spending control! Keep saving consistently.")

# -----------------------------
# Display insights
# -----------------------------
for i in insights:
    st.write(i)

# -----------------------------
# Extra summary
# -----------------------------
st.divider()

st.subheader("📌 Category Breakdown")
st.dataframe(category_spending)