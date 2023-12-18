import pandas as pd
import numpy as np
from sklearn.metrics import (
    r2_score,
    mean_squared_error,
    roc_auc_score,
    f1_score,
    accuracy_score,
    recall_score,
    cohen_kappa_score,
)
from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    completeness_score,
)
from sklearn.metrics.cluster import rand_score


def metrics_class(y_test, y_pred):
    metrics = {
        "roc_auc": roc_auc_score(y_test, y_pred),
        "accuracy": accuracy_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "cohen_kappa": cohen_kappa_score(y_test, y_pred),
        "f1": f1_score(y_test, y_pred),
    }
    return metrics


def metrics_clast(data, data_y, model):
    try:
        y_pred = model.labels_
    except:
        y_pred = model.predict(data)
    print(
        "Внешние метрики:",
        f"rand_score: {rand_score(y_pred, data_y)}",
        f"adjusted_rand_score: {completeness_score(y_pred, data_y)}",
        "Внутренние метрики:",
        f"silhouette_score: {silhouette_score(data, y_pred)}",
        f"davies_bouldin_score: {davies_bouldin_score(data, y_pred)}",
        sep=f"\n",
    )
