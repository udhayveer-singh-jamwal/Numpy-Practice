import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
elementwise = A * B
dot_product = np.dot(A, B)
matmul = A @ B
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Element-wise:\n", elementwise)
print("Dot Product:\n", dot_product)
print("Using @ operator:\n", matmul)
