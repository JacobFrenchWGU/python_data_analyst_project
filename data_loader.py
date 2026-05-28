import pandas as pd
def load_data():
    df = pd.read_csv('data/orders.csv')
    df = df.dropna()
    df = df.drop_duplicates()
    df["order_date"] = pd.to_datetime(df["order_date"])
    return df
