import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

indexes = [0, 2, 4]
selected = arr[indexes]
arr[[1, 3]] = 100

print("Original:", arr)
print("Indexes:", indexes)
print("Selected:", selected)
print("Modified:", arr)
