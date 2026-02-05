import numpy as np

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

scalar = 5
result_add = matrix + scalar
result_mul = matrix * scalar

print("Original Matrix:\n", matrix)
print("After Addition:\n", result_add)
print("After Multiplication:\n", result_mul)

row_vector = np.array([1, 2, 3])
broadcasted = matrix + row_vector
print("Broadcasted Result:\n", broadcasted)
