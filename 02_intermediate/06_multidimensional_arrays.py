import numpy as np

arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arr_3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("2D Array:\n", arr_2d)
print("Shape:", arr_2d.shape)
print("Element [1,2]:", arr_2d[1, 2])

print("\n3D Array:\n", arr_3d)
print("Shape:", arr_3d.shape)
print("Element [1,0,1]:", arr_3d[1, 0, 1])
