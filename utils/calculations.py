"""
calculations.py

Utility functions for financial calculations used in the
AI Financial Planner application.
"""


def calculate_budget(income, expenses):
    """
    Calculate total expenses, remaining balance,
    savings rate, and financial health status.

    Args:
        income (float): Monthly income
        expenses (dict): Dictionary containing expense categories

    Returns:
        dict: Budget calculation results
    """

    total_expenses = sum(expenses.values())
    balance = income - total_expenses

    # Prevent division by zero
    if income > 0:
        savings_rate = (balance / income) * 100
    else:
        savings_rate = 0

    # Determine financial health
    if savings_rate >= 30:
        health = "Excellent 🟢"
    elif savings_rate >= 20:
        health = "Good 🔵"
    elif savings_rate >= 10:
        health = "Average 🟡"
    elif balance >= 0:
        health = "Needs Improvement 🟠"
    else:
        health = "Overspending 🔴"

    return {
        "total_expenses": total_expenses,
        "balance": balance,
        "savings_rate": savings_rate,
        "financial_health": health,
    }
def expense_summary(df):
    """
    Returns summary statistics for expenses.
    """

    total = df["Amount"].sum()
    average = df["Amount"].mean()
    highest = df["Amount"].max()

    highest_category = (
        df.groupby("Category")["Amount"]
        .sum()
        .idxmax()
    )

    return {
        "total": total,
        "average": average,
        "highest": highest,
        "highest_category": highest_category,
    }