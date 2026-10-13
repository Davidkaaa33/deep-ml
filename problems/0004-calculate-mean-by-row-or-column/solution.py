def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	import numpy as np
	matrix = np.array(matrix)
	if mode == 'row':
		return matrix.mean(axis = 1)
	elif mode == 'column':
		return matrix.mean(axis = 0)