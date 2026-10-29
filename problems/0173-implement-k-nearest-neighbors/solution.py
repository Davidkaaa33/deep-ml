import numpy as np

def k_nearest_neighbors(points, query_point, k):

    dists = {d1 : np.linalg.norm(np.array(d1) - np.array(query_point)) for d1 in points}
    dists = sorted(dists, key = lambda x : dists[x])
    return dists[:k]