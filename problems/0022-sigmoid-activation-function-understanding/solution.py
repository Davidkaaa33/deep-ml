import math

def sigmoid(z: float) -> float:
	result = 1 / (1 + math.exp(-z))
	round(result, 4)
	return result