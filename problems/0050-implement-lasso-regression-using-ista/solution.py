import numpy as np

def soft_threshold(w: np.ndarray, threshold: float) -> np.ndarray:
    return np.sign(w) * np.maximum(np.abs(w) - threshold, 0)

def l1_regularization_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float = 0.1, learning_rate: float = 0.01, max_iter: int = 1000, tol: float = 1e-4) -> tuple:
    n_samples, n_features = X.shape
    weights = np.zeros(n_features)
    bias = 0.0
    for i in range(max_iter):
        y_pred = X @ weights + bias
        errors = y_pred - y
        grad_w = (1 / n_samples) * (X.T @ errors)
        grad_b = np.mean(errors)
        weights_temp = weights - learning_rate * grad_w
        weights_new = soft_threshold(weights_temp, alpha * learning_rate)
        bias_new = bias - learning_rate * grad_b
        change = np.linalg.norm(weights_new - weights)
        weights = weights_new
        bias = bias_new
        if change < tol:
            break
    return weights, bias