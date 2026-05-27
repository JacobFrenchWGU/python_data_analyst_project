import pandas as pd
def load_data():
    df = pd.read_csv('data/orders.csv')
    return df
