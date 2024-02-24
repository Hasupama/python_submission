# Program to multiply two matrices using nested loops

import numpy as np
@profile
def main():
    N = 250

    # NxN matrix
    X = np.random.randint(0, 100, size=(N, N))

    # Nx(N+1) matrix
    Y = np.random.randint(0, 100, size=(N, N + 1))

    # Nx(N+1)
    result = np.zeros(shape=(N, N + 1), dtype="int64")

    # iterate through rows of X
    for i in range(X.shape[0]):
        # iterate through columns of Y
        for j in range(Y.shape[1]):
            k = X[i, :] * Y[:, j]
            result[i, j] = k.sum()

    return result
main()