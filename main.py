from data_loader import load_data
from menu import show_menu



def main():

    df = load_data()

    show_menu(df)



if __name__ == "__main__":
    main()