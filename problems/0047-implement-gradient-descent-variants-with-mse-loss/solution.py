import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):

    def batch_gradient_descent(X, y, weights, alpha, epochs):
        m, n = X.shape
        theta = weights.copy()
        for _ in range(epochs):
            predictions = X @ theta
            errors = predictions - y
            gradient = 2 * (X.T @ errors) / m
            theta -= gradient * alpha
        return theta

    def stochastic_gradient_descent(X, y, weights, alpha, epochs):
        m, n = X.shape
        theta = weights.copy()
        for _ in range(epochs):
            for i in range(m):
                xi = X[i]
                yi = y[i]
                prediction = xi @ theta
                error = prediction - yi
                gradient = 2 * xi.T * error 
                theta -= gradient * alpha
        return theta

    def mini_batch_gradient_descent(X, y, weights, alpha, epochs, batch_size):
        m, n = X.shape
        theta = weights.copy()
        for _ in range(epochs):
            for start in range(0, m, batch_size):
                end = start + batch_size
                X_batch = X[start : end]
                y_batch = y[start : end]
                predictions = X_batch @ theta
                errors = predictions - y_batch
                gradient = 2 * (X_batch.T @ errors) / len(X_batch)
                theta -= gradient * alpha
        return theta

    if method == 'batch':
        return batch_gradient_descent(X, y, weights, learning_rate, n_epochs)
    elif method == "stochastic":
        return stochastic_gradient_descent(X, y, weights, learning_rate, n_epochs)
    elif method == "mini_batch":
        return mini_batch_gradient_descent(X, y, weights, learning_rate, n_epochs,batch_size)