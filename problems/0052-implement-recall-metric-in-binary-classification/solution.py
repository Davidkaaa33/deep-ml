import numpy as np

def recall(y_true, y_pred):
    tp, fn = 0, 0
    for i1, i2 in zip(y_true, y_pred):
        if i1 and i2:
            tp += 1
        elif not i2 and i1:
            fn += 1
    return tp / (tp + fn) if (tp + fn) != 0 else 0