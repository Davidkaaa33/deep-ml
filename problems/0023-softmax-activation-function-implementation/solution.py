import math

def softmax(scores: list[float]) -> list[float]:
    maxi = max(scores)
    summ = sum(math.exp(i - maxi) for i in scores)
    res = []
    for i in scores:
        res.append(math.exp(i - maxi) / summ)
    return res
