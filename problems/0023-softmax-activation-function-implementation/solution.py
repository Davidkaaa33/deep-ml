import math

def softmax(scores: list[float]) -> list[float]:
    maxi = max(scores)
    exp_scores = [math.exp(i - maxi) for i in scores]
    summ = sum(exp_scores)

    return [x / summ for x in exp_scores]
