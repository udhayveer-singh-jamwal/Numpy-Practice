import numpy as np

x = np.array([10, 20, 30, 40, 50])
y = np.array([15, 25, 35, 45, 60])
cov_matrix = np.cov(x, y)
print("Covariance Matrix:\n", cov_matrix)

