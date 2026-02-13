import numpy as np

scores = np.array([35, 67, 88, 45, 90, 30, 76])

mask = (scores >= 50) & (scores <= 80)
filtered = scores[mask]

print("Scores:", scores)
print("Mask:", mask)
print("Filtered:", filtered)

