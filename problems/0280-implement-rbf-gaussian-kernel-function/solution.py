import numpy as np

def rbf_kernel(X1: np.ndarray, X2: np.ndarray, gamma: float) -> np.ndarray:
    res = []
    for x1 in X1:
        row = []
        for x2 in X2:
            distance = np.sum((x1 - x2) ** 2)
            value = np.exp(-gamma * distance)
            row.append(value)
        res.append(row)
    return res