def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	import numpy as np
	matrix = np.array(matrix)

	if mode == 'row':
		return np.mean(matrix, axis = 1)
	return np.mean(matrix, axis = 0)