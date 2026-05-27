import matplotlib.pyplot as plt



def sales_chart(df):

    result = df.groupby("product")["quantity"].sum()

    plt.figure(figsize=(8, 5))
    plt.bar(result.index, result.values)

    plt.title("Product Sales")
    plt.xlabel("Product")
    plt.ylabel("Quantity Sold")

    plt.show()