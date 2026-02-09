import numpy as np

data = np.array([12, 15, 20, 22, 25, 30, 30, 35])

mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
variance = np.var(data)

print("Data:", data)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Variance:", variance)
outliers = data[data > mean + std_dev]
print("Outliers:", outliers)
