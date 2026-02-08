import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

h_stack = np.hstack((a, b))
v_stack = np.vstack((a, b))
print("Array A:", a)
print("Array B:", b)
print("Horizontal Stack:", h_stack)
print("Vertical Stack:\n", v_stack)

split_arr = np.array_split(h_stack, 3)
print("Split Arrays:", split_arr)
