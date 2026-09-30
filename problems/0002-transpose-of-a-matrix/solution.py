def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    import numpy as np
    a = np.array(a)
    return a.T