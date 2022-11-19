import pandas as pd

def dummies(data, columns):
    return pd.get_dummies(data, columns = columns, drop_first = True)


def binary(data):
  data = [0 if x == 'M' else 1 for x in data]
  return data
