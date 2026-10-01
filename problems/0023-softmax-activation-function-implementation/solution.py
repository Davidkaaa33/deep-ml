import torch
import torch.nn.functional as F

def softmax(scores: list[float]) -> list[float]:
  x = torch.tensor(scores, dtype = torch.float32)
  shifted = x - torch.max(x)
  exp_x = torch.exp(shifted)
  return (exp_x / torch.sum(exp_x)).tolist()