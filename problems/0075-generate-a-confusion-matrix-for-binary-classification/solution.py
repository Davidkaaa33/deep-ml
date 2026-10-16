
from collections import Counter

def confusion_matrix(data):
	counts = Counter(tuple(pair) for pair in data)
	return [[counts[(1, 1)], counts[(1, 0)]], [counts[(0, 1)], counts[(0, 0)]]]