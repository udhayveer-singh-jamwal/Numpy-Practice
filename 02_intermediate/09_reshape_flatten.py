import numpy as np

arr = np.arange(1, 13)

matrix = arr.reshape(3, 4)
flat1 = matrix.flatten()
flat2 = matrix.ravel()
print("Original Array:", arr)
print("Reshaped Matrix:\n", matrix)
print("Flatten:", flat1)
print("Ravel:", flat2)

matrix[0, 0] = 100
print("\nAfter change")
print("Matrix:\n", matrix)
print("Flatten:", flat1)
print("Ravel:", flat2)

