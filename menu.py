from analysis import (
    top_customers,
    total_sales,
    sales_by_state,
    best_selling_products,
    category_performance,
    top_customers,
    search_customer,
)

from visualization import sales_chart



def show_menu(df):

    while True:

        print("\n===== DATA ANALYSIS MENU =====")
        print("1. Total Sales")
        print("2. Sales By State")
        print("3. Best Selling Products")
        print("4. Category Performance")
        print("5. Top Customers")
        print("6. Search Customer")
        print("7. Product Sales Chart")
        print("8. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            total_sales(df)

        elif choice == "2":
            sales_by_state(df)
        elif choice == "3":
            best_selling_products(df)

        elif choice == "4":
            category_performance(df)

        elif choice == "5":
            top_customers(df)

        elif choice == "6":
            search_customer(df)

        elif choice == "7":
            sales_chart(df)

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

