import numpy as np

scores = np.array([32, 45, 67, 89, 95, 28])

updated = np.where(scores < 40, 40, scores)
limited = np.clip(updated, 40, 90)
print("Original Scores:", scores)
print("After Pass Rule:", updated)
print("After Clipping:", limited)
