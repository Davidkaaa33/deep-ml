import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    indices = np.arange(n_samples)
    if shuffle:
        np.random.shuffle(indices)
    base_size = n_samples // k
    remainder = n_samples % k
    fold_size = [base_size] * k
    for i in range(remainder):
        fold_size[i] += 1
    folds = []
    start = 0
    for size in fold_size:
        end = start + size
        fold = indices[start:end]
        folds.append(fold)
        start = end
    splits = []
    for i in range(k):
        test_indices = folds[i].tolist()
        train_indices = []
        for j in range(k):
            if j != i:
                train_indices.extend(folds[j].tolist())
        splits.append((train_indices, test_indices))
    return splits