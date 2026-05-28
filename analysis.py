from turtle import pd
import pandas as pd

def total_sales(df):
    total = df["total_amount"].sum()
    print(f"\nTotal Sales: ${total:.2f}")



def sales_by_state(df):
    result = df.groupby("state")["total_amount"].sum()

    print("\nSales By State")
    print(result)



def best_selling_products(df):
    result = df.groupby("product")["quantity"].sum()

    print("\nBest Selling Products")
    print(result.sort_values(ascending=False))



def category_performance(df):
    result = df.groupby("category")["total_amount"].sum()

    print("\nCategory Performance")
    print(result)

def top_customers(df):
    result = df.groupby("customer_name")["total_amount"].sum()

    print("\nTop Customers")
    print(result.sort_values(ascending=False))
def search_customer(df):

    name = input("Enter customer name: ")

    result = df[df["customer_name"].str.lower() == name.lower()]

    if result.empty:
        print("\nCustomer not found.")

    else:
        print("\nCustomer Orders")
        print(result)
def search_customer(df):

    name = input("Enter customer name: ")

    result = df[df["customer_name"].str.lower() == name.lower()]

    if result.empty:
        print("\nCustomer not found.")

    else:
        print("\nCustomer Orders")
        print(result)

    df = df.dropna()
    df = df.drop_duplicates()
    df["order_date"] = pd.to_datetime(df["order_date"])
    
def avg_order_value(df):
    print(df["total_amount"].mean())

def top_3_customers(df):
    result = df.groupby("customer_name")["total_amount"].sum()
    print(result.sort_values(ascending=False).head(3))

def monthly_sales(df):
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["month"] = df["order_date"].dt.to_period("M")
    print(df.groupby("month")["total_amount"].sum())

def export_summary(df):

    summary = {
        "Total Revenue": [df["total_amount"].sum()],
        "Average Order Value": [df["total_amount"].mean()],
        "Total Orders": [len(df)],
        "Top State": [
            df.groupby("state")["total_amount"].sum().idxmax()
        ],
        "Top Product": [
            df.groupby("product")["quantity"].sum().idxmax()
        ]
    }

    summary_df = pd.DataFrame(summary)

    summary_df.to_csv("summary_report.csv", index=False)

    print("\nSummary report exported!")

