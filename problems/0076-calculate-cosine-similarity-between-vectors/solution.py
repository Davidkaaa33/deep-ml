import numpy as np

def cosine_similarity(v1, v2):
	return (v1 @ v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))