import sqlite3
import pandas as pd


def create_database():

    # CONNECT TO DATABASE
    conn = sqlite3.connect("sales.db")

    # LOAD CSV
    df = pd.read_csv("data/orders.csv")

    # SAVE TO DATABASE
    df.to_sql("orders", conn, if_exists="replace", index=False)

    conn.close()

    print("Database created successfully!")


def run_query():

    conn = sqlite3.connect("sales.db")

    print("\nSQL QUERY OPTIONS")
    print("1. Total Revenue")
    print("2. Top Customers")
    print("3. Sales By State")

    choice = input("\nChoose query: ")

    if choice == "1":

        query = '''
        SELECT SUM(total_amount) AS total_revenue
        FROM orders
        '''

    elif choice == "2":

        query = '''
        SELECT customer_name,
            SUM(total_amount) AS total_spent
        FROM orders
        GROUP BY customer_name
        ORDER BY total_spent DESC
        '''

    elif choice == "3":

        query = '''
        SELECT state,
            SUM(total_amount) AS revenue
        FROM orders
        GROUP BY state
        ORDER BY revenue DESC
        '''

    else:
        print("Invalid choice.")
        conn.close()
        return

    result = pd.read_sql_query(query, conn)

    print("\nQUERY RESULT")
    print(result)

    conn.close()