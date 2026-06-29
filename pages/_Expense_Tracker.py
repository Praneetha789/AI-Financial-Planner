import streamlit as st
import pandas as pd
from datetime import date

from utils.calculations import expense_summary
from utils.charts import expense_pie_chart, daily_expense_chart
from database.db import (
    add_expense,
    get_all_expenses,
    delete_all_expenses,
)

st.set_page_config(
    page_title="Expense Tracker",
    page_icon="🧾",
    layout="wide",
)

st.title("🧾 Expense Tracker")
st.write("Track and analyze your daily expenses.")

# -------------------------
# Expense Form
# -------------------------

with st.form("expense_form"):

    col1, col2 = st.columns(2)

    with col1:
        expense_date = st.date_input(
            "Date",
            value=date.today()
        )

        category = st.selectbox(
            "Category",
            [
                "Food",
                "Transport",
                "Shopping",
                "Bills",
                "Entertainment",
                "Health",
                "Education",
                "Other",
            ],
        )

    with col2:
        amount = st.number_input(
            "Amount (₹)",
            min_value=0.0,
            step=10.0,
        )

        description = st.text_input("Description")

    submitted = st.form_submit_button("➕ Add Expense")

    if submitted:

        add_expense(
            expense_date,
            category,
            amount,
            description,
        )

        st.success("Expense added successfully!")

        st.rerun()

st.divider()

# -------------------------
# Load Expenses from Database
# -------------------------

rows = get_all_expenses()

if rows:

    df = pd.DataFrame(
        rows,
        columns=[
            "Date",
            "Category",
            "Amount",
            "Description",
        ],
    )

    # -------------------------
    # Search
    # -------------------------

    search = st.text_input("🔍 Search Description")

    if search:
        df = df[
            df["Description"].str.contains(
                search,
                case=False,
                na=False,
            )
        ]

    # -------------------------
    # Category Filter
    # -------------------------

    categories = ["All"] + sorted(df["Category"].unique())

    selected = st.selectbox(
        "Filter by Category",
        categories,
    )

    if selected != "All":
        df = df[df["Category"] == selected]

    # -------------------------
    # Summary Cards
    # -------------------------

    if not df.empty:

        summary = expense_summary(df)

        st.divider()

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "💸 Total",
            f"₹{summary['total']:,.2f}",
        )

        c2.metric(
            "📊 Average",
            f"₹{summary['average']:,.2f}",
        )

        c3.metric(
            "🔥 Highest Expense",
            f"₹{summary['highest']:,.2f}",
        )

        c4.metric(
            "🏆 Top Category",
            summary["highest_category"],
        )

        st.divider()

        # -------------------------
        # Charts
        # -------------------------

        left, right = st.columns(2)

        with left:
            pie = expense_pie_chart(df)
            st.plotly_chart(
                pie,
                use_container_width=True,
            )

        with right:
            line = daily_expense_chart(df)
            st.plotly_chart(
                line,
                use_container_width=True,
            )

        st.divider()

        # -------------------------
        # Expense Table
        # -------------------------

        st.subheader("📋 Expense History")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
        )

        # -------------------------
        # Delete All
        # -------------------------

        if st.button("🗑 Clear All Expenses"):

            delete_all_expenses()

            st.success("All expenses deleted!")

            st.rerun()

    else:
        st.warning("No matching expenses found.")

else:

    st.info("No expenses added yet.")