import numpy as np

marks = np.array([78, 45, 90, 67, 88, 52])

sorted_marks = np.sort(marks)
sorted_desc = np.sort(marks)[::-1]
sorted_index = np.argsort(marks)
print("Original:", marks)
print("Sorted Asc:", sorted_marks)
print("Sorted Desc:", sorted_desc)
print("Sorted Index:", sorted_index)
value = 88
index = np.where(marks == value)
print(f"Index of {value}:", index[0])
