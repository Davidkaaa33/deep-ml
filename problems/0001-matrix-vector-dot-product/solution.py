def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	res = []
	for row in a:
		summ = 0
		if len(row) != len(b):
			return -1
		for row_element, vector_element in zip(row, b):
			summ += row_element * vector_element
		res.append(summ)
	return res