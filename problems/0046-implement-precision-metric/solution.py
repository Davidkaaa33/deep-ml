import numpy as np
def precision(y_true, y_pred):
	tp, fp = 0, 0
	for i1, i2 in zip(y_true, y_pred):
		if i1 and i2:
			tp += 1
		elif not i1 and i2:
			fp += 1
	return tp / (tp + fp) if (tp + fp) != 0 else 0
