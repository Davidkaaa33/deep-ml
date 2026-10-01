import torch
import torch.nn.functional as F

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> tuple[list[float], float]:
    X = torch.tensor(features, dtype = torch.float32)
    w = torch.tensor(weights, dtype = torch.float32)
    y = torch.tensor(labels, dtype = torch.float32)

    z = X @ w + bias
    probabilities = torch.sigmoid(z)
    mse = torch.mean((probabilities - y)**2)
    probabilities = [round(x, 4) for x in probabilities.tolist()]
    mse = round(mse.item(), 4)
    return probabilities, mse