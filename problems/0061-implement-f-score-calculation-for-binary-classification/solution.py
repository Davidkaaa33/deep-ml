import numpy as np

def f_score(y_true, y_pred, beta):
	tp, fp, fn = 0, 0, 0
	for i1, i2 in zip(y_true, y_pred):
		if i1 and i2:
			tp +=1
		elif not i1 and i2:
			fp += 1
		elif i1 and not i2:
			fn += 1
	precision = tp / (tp + fp) if (tp + fp)!= 0 else 0
	recall = tp / (tp + fn) if (tp + fn)!= 0 else 0
	return round((1 + beta**2) * precision * recall / (beta ** 2 * precision + recall), 3)
