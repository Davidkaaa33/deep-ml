import math
import numpy as np

def rmse(y_true, y_pred):
	if y_true.size == 0 or y_pred.size == 0 or y_pred.shape != y_true.shape:
		raise ValueError('Invalid input')
	errors = np.sum((y_true - y_pred)**2) / y_true.size
	return round(math.sqrt(errors), 3)


