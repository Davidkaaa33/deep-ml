import math

def normal_pdf(x, mean, std_dev):
	val = 1 / (math.sqrt(2 * math.pi * std_dev ** 2)) * math.exp((-1) * (x - mean) ** 2 / (2 * std_dev ** 2))
	return round(val,5)