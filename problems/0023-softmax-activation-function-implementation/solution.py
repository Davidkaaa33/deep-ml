import math
def softmax(scores: list[float]) -> list[float]:
    c = max(scores)
    sum_e = sum(math.exp(i - c) for i in scores)
    return [math.exp(i - c) / sum_e for i in scores]