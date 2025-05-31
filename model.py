"""
needed for pylint. trains the model.
"""

import pickle
import pandas as pd
#import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#from sklearn.preprocessing import StandardScaler

#just putting all of this into functions, since that i can only use pytest
#through calling functions
def get_data(csv_file):
    return pd.read_csv(csv_file)

def tt_split(dataframe):
    x = dataframe[["Hours"]]
    y = dataframe["Scores"]

    return train_test_split(x, y, test_size=0.2, random_state=42)


df = get_data("dataset.csv")
x_tr, x_te, y_tr, y_te = tt_split(df)

model = LinearRegression()

model.fit(x_tr, y_tr)

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

