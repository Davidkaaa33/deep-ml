import numpy as np
import math
def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
	pred = X @ weights + bias
    probabilities = 1 / (1 + np.exp(-pred))
    return (probabilities >= 0.5).astype(int)