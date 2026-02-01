import numpy as np

arr = np.array([1, 2, 3, 4])
arr_float = np.array([1, 2, 3], dtype=float)

print(arr.dtype)
print(arr_float.dtype)
new_arr = arr.astype(float)
print(new_arr)
