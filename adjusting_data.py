import pandas as pd
def get_product_info(product_name):

    products_df = pd.read_csv("data/products.csv")

    product_info = products_df[
        products_df["product"].str.lower() == product_name.lower()
    ]

    if product_info.empty:
        return None

    return product_info.iloc[0].to_dict()

def add_order(df):

    customer_name = input("Customer Name: ")
    state = input("State: ")
    product = input("Product: ")
    order_date = input("Order Date (YYYY-MM-DD): ")

    product_info = get_product_info(product)

    if product_info is None:
        print("\nERROR: Product not found in product list!")
        return
    print(f"\nAvailable stock for {product}: {product_info['stock']}")
    
    category = product_info["category"]
    price = product_info["price"]

    quantity = int(input("Quantity: "))

    while quantity <= 0:
        print("\nQuantity must be greater than 0")
        print(f"Available stock for {product}: {product_info['stock']}")
        quantity = int(input("Quantity: "))


    while quantity > product_info["stock"]:
        print("\nNot enough stock available!")
        print(f"Available stock for {product}: {product_info['stock']}")
        quantity = int(input("Quantity: "))


    total_amount = price * quantity

    # Optional: reduce stock
    products = pd.read_csv("data/products.csv")
    products.loc[
        products["product"].str.lower() == product.lower(),
        "stock"
    ] -= quantity

    products.to_csv("data/products.csv", index=False)

    new_row = {
        "customer_name": customer_name,
        "state": state,
        "product": product,
        "category": category,
        "quantity": quantity,
        "total_amount": total_amount,
        "order_date": order_date
    }

    df.loc[len(df)] = new_row

    df.to_csv("data/orders.csv", index=False)

    print("\nOrder added successfully!")


def remove_customer(df):

    customer = input("Enter customer name to remove: ")

    df = df[
        df["customer_name"].str.lower() != customer.lower()
    ]

    df.to_csv("data/orders.csv", index=False)

    print("\nCustomer removed successfully!")

    return df



def update_order(df):

    customer = input("Enter customer name: ")

    print("\nWhat do you want to update?")
    print("1. Product")
    print("2. Quantity")
    print("3. Total Amount")
    print("4. State")

    choice = input("Choose option: ")

    if choice == "1":

        new_product = input("Enter new product: ")

        df.loc[
            df["customer_name"].str.lower() == customer.lower(),
            "product"
        ] = new_product

    elif choice == "2":

        new_quantity = int(
            input("Enter new quantity: ")
        )

        df.loc[
            df["customer_name"].str.lower() == customer.lower(),
            "quantity"
        ] = new_quantity

    elif choice == "3":

        new_total = float(
            input("Enter new total amount: ")
        )

        df.loc[
            df["customer_name"].str.lower() == customer.lower(),
            "total_amount"
        ] = new_total

    elif choice == "4":

        new_state = input("Enter new state: ")

        df.loc[
            df["customer_name"].str.lower() == customer.lower(),
            "state"
        ] = new_state

    else:
        print("Invalid option.")
        return

    df.to_csv("data/orders.csv", index=False)

    print("\nOrder updated successfully!")


