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