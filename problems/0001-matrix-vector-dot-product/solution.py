import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	a = np.array(a)
	b = np.array(b)
	if len(a[0]) == len(b):
		return a @ b
	return -1