def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	import numpy as np
	a = np.array(a)
	b = np.array(b)
	if a.shape[1] != b.shape[0]:
		return -1
	return (a @ b).tolist()
