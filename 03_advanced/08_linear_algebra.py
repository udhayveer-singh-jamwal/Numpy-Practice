import numpy as np

matrix = np.array([
    [4, 2],
    [3, 1]
])

det = np.linalg.det(matrix)
inv = np.linalg.inv(matrix)
eig_values, eig_vectors = np.linalg.eig(matrix)
print("Matrix:\n", matrix)
print("Determinant:", det)
print("Inverse:\n", inv)
print("Eigenvalues:", eig_values)
print("Eigenvectors:\n", eig_vectors)
