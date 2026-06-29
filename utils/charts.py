import plotly.express as px


def expense_pie_chart(df):
    fig = px.pie(
        df,
        values="Amount",
        names="Category",
        hole=0.45,
        title="Expense Distribution"
    )
    return fig


def daily_expense_chart(df):
    daily = (
        df.groupby("Date", as_index=False)["Amount"]
        .sum()
        .sort_values("Date")
    )

    fig = px.line(
        daily,
        x="Date",
        y="Amount",
        markers=True,
        title="Daily Expense Trend"
    )

    return fig