import math
import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):

	features = np.array(features)
	labels = np.array(labels)
	weights = np.array(weights)
	z = np.dot(features, weights) + bias
	probabilities = [round(1 / (1 + math.exp(-x)), 4) for x in z]
	mse = round((1 / len(probabilities)) * sum((probabilities[i] - labels[i])**2 for i in range(len(probabilities))), 4)
	return probabilities, mse