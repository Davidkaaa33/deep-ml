import numpy as np

def soft_threshold(w: np.ndarray, threshold: float) -> np.ndarray:
    return np.sign(w) * np.maximum(np.abs(w) - threshold, 0)

def l1_regularization_gradient_descent(X : np.ndarray, y : np.ndarray, alpha: float = 0.1, learning_rate: float = 0.01, max_iter: int = 1000):
    n_samples, n_features = X.shape
    weights = np.zeros(n_features)
    bias = 0.0

    for _ in range(max_iter):
        predictions = X @ weights + bias
        errors = predictions - y
        grad_w = (X.T @ errors) / n_samples
        grad_b = np.mean(errors)
        weights -= learning_rate * grad_w
        bias -= learning_rate * grad_b

        weights = soft_threshold(weights, learning_rate * alpha)
    return weights, bias
