def nan_destroyer(X, y, subset):

    X = X.dropna(subset=subset)

    y = y[y.index.isin(X.index)]

    return X, y


def fill_nan(X, cols):
    for i in cols:
        X[i] = X[i].fillna(X[i].mean())
    return X
