import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.model_selection import cross_val_score

def report(y_test, y_pred):
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    data = [r2, mae, rmse]

    idx = ['R2 Score', 'MAE', 'RMSE']
    results = pd.DataFrame(index=idx, data = data, columns=['Value'])
    results.index.name = 'Metric'
    display(results)

    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred)
    plt.plot(y_test, y_test, 'r')
    plt.xlabel('Y test')
    plt.ylabel('Model Prediction')
    plt.show()


def cv_scores(model, X_train, y_train, scoring='r2', cv=10):
    scores = cross_val_score(model, X_train, y_train.ravel(), scoring=scoring, cv = cv)

    cv_results = pd.DataFrame(np.round(np.append(scores, scores.mean()), 5), columns=['Scores'])

    idx = 'Split ' + (cv_results.index[:-1] + 1).astype('str')
    idx = np.append(idx, 'CV Score')
    cv_results.index = idx

    display(cv_results)

    plt.figure(figsize=(10, 5))
    plt.plot(cv_results[:-1])
    plt.show()
    

