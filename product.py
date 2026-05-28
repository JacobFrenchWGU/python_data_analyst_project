import pandas as pd


def load_products():
    return pd.read_csv("data/products.csv")



def add_product():

    df = load_products()

    name = input("Product name: ")
    category = input("Category: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))

    new_row = {
        "product": name,
        "category": category,
        "price": price,
        "stock": stock
    }

    df.loc[len(df)] = new_row

    df.to_csv("data/products.csv", index=False)

    print("\nProduct added successfully!")



def remove_product():

    df = load_products()

    name = input("Product name to remove: ")

    df = df[df["product"].str.lower() != name.lower()]

    df.to_csv("data/products.csv", index=False)

    print("\nProduct removed successfully!")



def update_product():

    df = load_products()

    name = input("Product name to update: ")

    print("\nWhat do you want to update?")
    print("1. Price")
    print("2. Stock")

    choice = input("Choose: ")

    if choice == "1":

        new_price = float(input("New price: "))

        df.loc[
            df["product"].str.lower() == name.lower(),
            "price"
        ] = new_price

    elif choice == "2":

        new_stock = int(input("New stock: "))

        df.loc[
            df["product"].str.lower() == name.lower(),
            "stock"
        ] = new_stock

    else:
        print("Invalid choice")
        return

    df.to_csv("data/products.csv", index=False)

    print("\nProduct updated successfully!")