import numpy as np

def get_random_subsets(X, y, n_subsets, replacements=True):
    n = len(X)
    subset_size = n if replacements else n // 2
    subsets = []
    for _ in range(n_subsets):
        indices = np.random.choice(n, subset_size, replace = replacements)
        X_subset = X[indices].tolist()
        y_subset = y[indices].tolist()
        subsets.append((X_subset, y_subset))
    return subsets