import numpy as np

marks = np.array([45, 78, 88, 32, 90, 67, 40])
passed = marks[marks >= 50]
failed = marks[marks < 50]
print("All Marks:", marks)
print("Passed Students:", passed)
print("Failed Students:", failed)
marks[marks < 50] = 50
print("Updated Marks:", marks)
