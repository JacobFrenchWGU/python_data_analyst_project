import matplotlib.pyplot as plt
import pandas as pd


def sales_chart(df):

    result = df.groupby("product")["quantity"].sum()

    plt.figure(figsize=(8, 5))
    plt.bar(result.index, result.values)

    plt.title("Product Sales")
    plt.xlabel("Product")
    plt.ylabel("Quantity Sold")

    plt.show()

def category_pie(df):
    df.groupby("category")["total_amount"].sum().plot(kind="pie", autopct="%1.1f%%")

def sales_trend(df):
    df["order_date"] = pd.to_datetime(df["order_date"])
    df.groupby("order_date")["total_amount"].sum().plot(kind="line")

