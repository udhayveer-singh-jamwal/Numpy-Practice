import numpy as np

data = np.array([10, 12, 14, 15, 16, 100])
mean = data.mean()
std = data.std()
z_scores = (data - mean) / std
print("Z-scores:", z_scores)

