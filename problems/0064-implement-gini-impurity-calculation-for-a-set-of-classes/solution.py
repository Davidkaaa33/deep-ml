
import numpy as np

def gini_impurity(y):
	u = set(y)
	val = 1
	for c in u:
		val -= (y.count(c)/len(y))**2
	return round(val,3)