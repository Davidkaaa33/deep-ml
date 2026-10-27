
import numpy as np

def stratified_kfold_indices(y, n_splits):
    y = np.asarray(y)
    n = len(y)

    # Step 1: Create empty folds
    folds = [[] for _ in range(n_splits)]

    # Step 2: Split each class separately
    for c in np.unique(y):
        class_indices = np.where(y == c)[0]

        # Divide class indices into balanced groups
        class_folds = np.array_split(class_indices, n_splits)

        # Add each group to its corresponding fold
        for i in range(n_splits):
            folds[i].extend(class_folds[i].tolist())

    # Step 3: Create train/test splits
    splits = []

    for i in range(n_splits):
        test_indices = sorted(folds[i])

        train_indices = sorted(
            set(range(n)) - set(test_indices)
        )

        splits.append([train_indices, test_indices])

    return splits
