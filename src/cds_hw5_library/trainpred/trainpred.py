from sklearn.linear_model import LogisticRegression
import numpy as np


model = LogisticRegression()

def train(x, y ):
    model.fit(x, y)
    return x, y


def pred(train, test):
    predictiontrain = train['predictions'] = np.squeeze(model.predict_proba(train)[:, 1])
    predictiontest = test['predictions'] = np.squeeze(model.predict_proba(test)[:, 1])
    return train, test, predictiontrain, predictiontest
