import streamlit as st
import pandas as pd
import plotly.express as px

from database.db import get_all_expenses

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("💰 AI Financial Dashboard")

rows = get_all_expenses()

if not rows:
    st.warning("No data found. Add expenses first.")
    st.stop()

df = pd.DataFrame(
    rows,
    columns=["Date", "Category", "Amount", "Description"]
)

df["Date"] = pd.to_datetime(df["Date"])

# -----------------------------
# KPI SECTION (CLEAN UI)
# -----------------------------
total = df["Amount"].sum()
avg = df["Amount"].mean()
max_val = df["Amount"].max()
top_cat = df.groupby("Category")["Amount"].sum().idxmax()

col1, col2, col3, col4 = st.columns(4)

col1.metric("💸 Total Spent", f"₹{total:,.0f}")
col2.metric("📊 Avg Expense", f"₹{avg:,.0f}")
col3.metric("🔥 Highest Expense", f"₹{max_val:,.0f}")
col4.metric("🏆 Top Category", top_cat)

st.divider()

# -----------------------------
# CHART SECTION (PRO LEVEL UI)
# -----------------------------
left, right = st.columns(2)

with left:
    st.subheader("🥧 Spending Breakdown")

    fig1 = px.pie(
        df,
        names="Category",
        values="Amount",
        hole=0.4
    )
    st.plotly_chart(fig1, use_container_width=True)

with right:
    st.subheader("📈 Spending Trend")

    trend = df.groupby("Date")["Amount"].sum().reset_index()

    fig2 = px.line(
        trend,
        x="Date",
        y="Amount",
        markers=True
    )

    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# -----------------------------
# RECENT TRANSACTIONS (CLEAN TABLE)
# -----------------------------
st.subheader("🧾 Recent Transactions")

st.dataframe(
    df.sort_values("Date", ascending=False),
    use_container_width=True
)