
import numpy as np

def r_squared(y_true, y_pred):
	y_mean = np.mean(y_true)
	ssr = np.sum((y_true - y_pred)**2)
	sst = np.sum((y_true - y_mean)**2)
	return 1 - ssr/sst
