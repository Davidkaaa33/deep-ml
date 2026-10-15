import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    def find_mode(data):
        a = {}
        for c in data:
            a[c] = a.get(c, 0) + 1
        return max(a, key = a.get)

    meann = np.mean(data)
    mediann = np.median(data)
    variencee = np.var(data)
    stddev = np.std(data)
    modee = find_mode(data)
    q25 = np.quantile(data, 0.25)
    q50 = np.quantile(data, 0.50)
    q75 = np.quantile(data, 0.75)
    inq = q75-q25

    return {'mean' : meann, 'median' : mediann, 'mode' : modee, 'variance' : variencee, 'standard_deviation' : stddev, '25th_percentile' : q25, '50th_percentile' : q50, '75th_percentile' : q75, 'interquartile_range' : inq}



