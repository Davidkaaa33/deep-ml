import numpy as np

def to_categorical(x, n_col=None):
	if n_col is None:
		n_col = np.max(x) + 1
	result = np.zeros((len(x), n_col))
	row_n = 0
	for num in x:
		result[row_n][num] = 1
		row_n += 1
	return result