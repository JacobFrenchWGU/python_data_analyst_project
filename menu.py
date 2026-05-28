from analysis import (
    top_customers,
    total_sales,
    sales_by_state,
    best_selling_products,
    category_performance,
    top_customers,
    search_customer,
    avg_order_value,
    export_summary,
)

from visualization import sales_chart, category_pie, sales_trend

from database import run_query

from adjusting_data import add_order, remove_customer, update_order

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
        print("9. Product Sales Chart")
        print("10. Category Sales Pie Chart")
        print("11. Sales Trend Line Chart")
        print("12. Run SQL Query")
        print("13. Export Summary")
        print("14. Adjusting Order")
        print("15. Exit")

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
            run_query()

        elif choice == "13":
            export_summary(df)
        
        elif choice == "14":
            print("\nADJUSTING ORDERS")
            print("1. Add Order")
            print("2. Remove Customer")
            print("3. Update Order")

            adjust_choice = input("Choose option: ")

            if adjust_choice == "1":
                add_order(df)

            elif adjust_choice == "2":
                remove_customer(df)

            elif adjust_choice == "3":
                update_order(df)

            else:
                print("Invalid option.")

        elif choice == "14":
            print("Goodbye!")
            break



        else:
            print("Invalid choice. Please try again.")

