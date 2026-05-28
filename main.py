from data_loader import load_data
from menu import show_menu
from database import create_database



def main():
    create_database()
    df = load_data()

    show_menu(df)



if __name__ == "__main__":
    main()