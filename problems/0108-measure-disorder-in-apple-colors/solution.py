def disorder(apples: list) -> float:
	u = set(apples)
	val = 1
	for c in u:
		val -= (apples.count(c) / len(apples))**2
	return val