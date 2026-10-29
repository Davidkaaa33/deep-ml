import numpy as np
from typing import Tuple

def find_best_split(X: np.ndarray, y: np.ndarray) -> Tuple[int, float]:
    def gini(labels):
        if len(labels) == 0:
            return 0
        p = np.mean(labels)
        return 2 * p * (1 - p)
    
    n, d = X.shape
    best_imp = float('inf')
    best_feature = None
    best_thr = None
    for j in range(d):
        for threshold in    np.unique(X[:, j]):
            mask = X[:, j] <= threshold
            left = y[mask]
            right = y[~mask]
            if len(left) == 0 or len(right) == 0:
                continue
            impurity = (len(left) / n * gini(left) + len(right) / n * gini(right))
            if impurity < best_imp:
                best_imp = impurity
                best_feature = j
                best_thr = threshold
    return best_feature, best_thr