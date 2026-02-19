import numpy as np

data = np.array([10, 12, 14, 15, 16, 100])
mean = data.mean()
std = data.std()
z_scores = (data - mean) / std
outliers = data[np.abs(z_scores) > 2]
print("Data:", data)
print("Z-scores:", z_scores)
print("Outliers:", outliers)
