import numpy as np

def divide_on_feature(X, feature_i, threshold):
	first, second = [], []
	mask = X[:, feature_i] >= threshold
	first = X[mask]
	second = X[~mask]
	return [first, second]