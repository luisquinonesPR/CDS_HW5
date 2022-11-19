from sklearn.model_selection import train_test_split

def split_data(data):
    y = data.diabetes_mellitus
    X = data.drop("diabetes_mellitus", axis = 1)
    return train_test_split(X, y, random_state=99)
