import numpy as np

def shuffle_data(X, y, seed=None):
	rng = np.random.RandomState(seed)
	indices = rng.permutation(len(X))
	X_shuffled = X[indices]
	y_shuffled = y[indices]

	return X_shuffled, y_shuffled
