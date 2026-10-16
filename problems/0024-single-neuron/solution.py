import math
import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	features, labels, bias, weights = np.array(features), np.array(labels), np.array(bias), np.array(weights)
	a = features @ weights + bias
	probabilities = 1 / (1 + np.exp(-a))
	mse = np.mean((probabilities - labels)**2)
	return probabilities.round(4).tolist(), round(float(mse), 4)