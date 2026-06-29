import sqlite3

DATABASE_NAME = "database/finance.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expense_date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_expense(expense_date, category, amount, description):
    create_tables()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO expenses
        (expense_date, category, amount, description)
        VALUES (?, ?, ?, ?)
    """, (
        str(expense_date),
        category,
        amount,
        description
    ))

    conn.commit()
    conn.close()


def get_all_expenses():
    create_tables()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            expense_date,
            category,
            amount,
            description
        FROM expenses
        ORDER BY expense_date DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_all_expenses():
    create_tables()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses")

    conn.commit()
    conn.close()