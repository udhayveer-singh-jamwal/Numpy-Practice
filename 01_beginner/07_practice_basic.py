import numpy as np

nums = np.array([10, 20, 30, 40, 50])

print("Sum:", nums.sum())
print("Max:", nums.max())
print("Min:", nums.min())
print("Mean:", nums.mean())
even = nums[nums % 2 == 0]
print("Even numbers:", even)
