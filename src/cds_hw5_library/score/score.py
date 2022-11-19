from sklearn.metrics import roc_auc_score
import scikitplot as skplt
import matplotlib.pyplot as plt

def score(predictiontrain, y_train, predictiontest, y_test):
    score_train = roc_auc_score(y_train, predictiontrain)
    score_test = roc_auc_score(y_test, predictiontest)
    return score_train, score_test



