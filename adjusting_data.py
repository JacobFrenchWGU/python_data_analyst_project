import pandas as pd
def add_order(df):

    customer_name = input("Customer Name: ")
    state = input("State: ")
    product = input("Product: ")
    category = input("Category: ")

    quantity = int(input("Quantity: "))
    total_amount = float(input("Total Amount: "))
    order_date = input("Order Date (YYYY-MM-DD): ")

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


