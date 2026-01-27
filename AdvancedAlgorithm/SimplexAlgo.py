import numpy as np

def simplex(c, A, b):
    m, n = A.shape
    table = np.zeros((m + 1, n + m + 1))
    table[:m, :n] = A
    table[:m, n:n + m] = np.eye(m)
    table[:m, -1] = b
    table[-1, :n] = -c

    while np.any(table[-1, :-1] < 0):
        col = np.argmin(table[-1, :-1])
        ratios = table[:-1, -1] / table[:-1, col]
        row = np.argmin(ratios)
        pivot = table[row, col]
        table[row, :] /= pivot
        for i in range(m + 1):
            if i != row:
                table[i, :] -= table[i, col] * table[row, :]

    return table[-1, -1]

c = np.array(list(map(float, input("coeff ").split())))
A = np.array(list(map(float, input().split()))).reshape(2, 2)
b = np.array(list(map(float, input().split())))

print("Max simplex of Z:", simplex(c, A, b))
