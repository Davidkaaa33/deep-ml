import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    m = X.shape[0]
    w = np.zeros(X.shape[1])
    for i in range(iterations):
        grad = (1 / m) * (X.T @ (X @ w - y))
        w -= alpha * grad
    return w
    