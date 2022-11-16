import pandas as pd

def dummies(data, columns):
    return pd.get_dummies(data, columns = columns, drop_first = True)
