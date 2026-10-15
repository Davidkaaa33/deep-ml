import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	X, y = np.array(X), np.array(y)
	return np.linalg.inv(X.T @ X) @ X.T @ y