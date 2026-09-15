import numpy as np

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonal_sum =sum(matrix1[i][i] for i in range(len(matrix1)))

print("대각합:", diagonal_sum)

matrix2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("대각합:", np.trace(matrix2))