import numpy as np

original = np.array([1, 2, 3, 4, 5])

view_arr = original.view()
copy_arr = original.copy()

view_arr[0] = 100
copy_arr[1] = 200

print("Original Array:", original)
print("View Array:", view_arr)
print("Copy Array:", copy_arr)
print("View affects original:", original[0])
print("Copy does not affect original:", original[1])
