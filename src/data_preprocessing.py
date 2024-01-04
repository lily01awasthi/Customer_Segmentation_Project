import pandas as pd


def load_and_preprocess_data():
    # path to CSV dataset
    data_path = 'data/Online Retail.csv'

    # load the data
    df = pd.read_csv(data_path)

    # clean data
    #df = data_cleaning(df)

    # Preprocess the data ( normalization, feature engineering )
    #df = preprocess_data(df)

    return df


def data_cleaning(data):
    return data


def preprocess_data(data):
    return data

