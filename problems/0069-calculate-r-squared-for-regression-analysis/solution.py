
import numpy as np

def r_squared(y_true, y_pred):
	mean_y = np.mean(y_true)
	ss_res = np.sum((y_true - y_pred) ** 2)
	ss_tot = np.sum((y_true - mean_y) ** 2)
	r2 = 1 - ss_res / ss_tot
	return r2