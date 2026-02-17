import numpy as np

data = np.random.normal(loc=50, scale=10, size=1000)
hist, bins = np.histogram(data, bins=10)
print("Histogram counts:", hist)
print("Bin edges:", bins)
print("Max Value:", data.max())
print("Min Value:", data.min())
print("Mean:", data.mean())

