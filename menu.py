from analysis import (
    top_customers,
    total_sales,
    sales_by_state,
    best_selling_products,
    category_performance,
    top_customers,
    search_customer,
    avg_order_value,
)

from visualization import sales_chart, category_pie, sales_trend



def show_menu(df):

    while True:

        print("\n===== DATA ANALYSIS MENU =====")
        print("1. Total Sales")
        print("2. Sales By State")
        print("3. Best Selling Products")
        print("4. Category Performance")
        print("5. Top Customers")
        print("6. Average Order Value")
        print("7. Search Customer")
        print("8. Product Sales Chart")
        print("12. Exit")
        print("9. Product Sales Chart")
        print("10. Category Sales Pie Chart")
        print("11. Sales Trend Line Chart")
        print("12. Exit")

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
            avg_order_value(df)
        
        elif choice == "7":
            search_customer(df)

        elif choice == "8":
            sales_chart(df)

        elif choice == "9":
            sales_chart(df)

        elif choice == "10":
            category_pie(df)

        elif choice == "11":
            sales_trend(df)

        elif choice == "12":
            print("Goodbye!")
            break



        else:
            print("Invalid choice. Please try again.")

