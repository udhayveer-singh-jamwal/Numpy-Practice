import numpy as np

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])

add = arr1 + arr2
sub = arr1 - arr2
mul = arr1 * arr2
div = arr1 / arr2

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)

# Combined operation
result = (arr1 * 2) + (arr2 ** 2)
print("Final Result:", result)
