import numpy as np

data = np.array([10, 20, 30, 40, 50])

min_val = data.min()
max_val = data.max()
normalized = (data - min_val) / (max_val - min_val)
mean = data.mean()
std = data.std()
standardized = (data - mean) / std
print("Original:", data)
print("Normalized:", normalized)
print("Standardized:", standardized)

