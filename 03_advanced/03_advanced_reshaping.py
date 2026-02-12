import numpy as np

arr = np.arange(1, 13)
matrix = arr.reshape(3, 4)

print("Original:\n", matrix)
transposed = matrix.T
swapped = np.swapaxes(matrix, 0, 1)
print("Transposed:\n", transposed)
print("Swapped Axes:\n", swapped)
