import streamlit as st
import pandas as pd
import plotly.express as px

from utils.calculations import calculate_budget

st.set_page_config(page_title="Budget Planner", page_icon="📊", layout="wide")

st.title("📊 Budget Planner")
st.write("Track your monthly income and expenses to understand your financial health.")

st.divider()

# -----------------------------
# User Input
# -----------------------------

col1, col2 = st.columns(2)

with col1:
    income = st.number_input(
        "💵 Monthly Income (₹)",
        min_value=0.0,
        step=1000.0,
    )

    rent = st.number_input(
        "🏠 Rent",
        min_value=0.0,
        step=500.0,
    )

    food = st.number_input(
        "🍽 Food",
        min_value=0.0,
        step=500.0,
    )

    transport = st.number_input(
        "🚗 Transport",
        min_value=0.0,
        step=500.0,
    )

with col2:
    utilities = st.number_input(
        "💡 Utilities",
        min_value=0.0,
        step=500.0,
    )

    entertainment = st.number_input(
        "🎬 Entertainment",
        min_value=0.0,
        step=500.0,
    )

    other = st.number_input(
        "📦 Other Expenses",
        min_value=0.0,
        step=500.0,
    )

st.divider()

if st.button("📈 Calculate Budget", use_container_width=True):

    expenses = {
        "Rent": rent,
        "Food": food,
        "Transport": transport,
        "Utilities": utilities,
        "Entertainment": entertainment,
        "Other": other,
    }

    result = calculate_budget(income, expenses)

    st.header("📋 Budget Summary")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "💸 Total Expenses",
        f"₹{result['total_expenses']:,.2f}"
    )

    c2.metric(
        "💰 Remaining Balance",
        f"₹{result['balance']:,.2f}"
    )

    c3.metric(
        "📈 Savings Rate",
        f"{result['savings_rate']:.1f}%"
    )

    c4.metric(
        "⭐ Financial Health",
        result["financial_health"]
    )

    st.divider()

    # Progress Bar
    progress = min(max(result["savings_rate"] / 100, 0), 1)

    st.subheader("Financial Health Score")
    st.progress(progress)

    st.write(f"Current Savings Rate: **{result['savings_rate']:.1f}%**")

    st.divider()

    # Expense Chart
    df = pd.DataFrame({
        "Category": list(expenses.keys()),
        "Amount": list(expenses.values())
    })

    fig = px.pie(
        df,
        values="Amount",
        names="Category",
        hole=0.45,
        title="Expense Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("💡 Personalized Financial Tips")

    if result["savings_rate"] >= 30:
        st.success("""
🎉 Excellent!

• Keep investing regularly.
• Build an emergency fund.
• Consider SIPs or index funds.
""")

    elif result["savings_rate"] >= 20:
        st.info("""
👍 Good!

• Try increasing savings by 5%.
• Reduce unnecessary spending.
""")

    elif result["savings_rate"] >= 10:
        st.warning("""
⚠ Average

• Reduce entertainment expenses.
• Track every expense.
• Set a monthly savings goal.
""")

    else:
        st.error("""
🚨 Overspending!

• Review your monthly expenses.
• Cut unnecessary purchases.
• Increase your savings gradually.
""")