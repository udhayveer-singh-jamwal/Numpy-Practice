import numpy as np

a = np.arange(10)
b = a.view()
c = a.copy()

a[0] = 999
print("Original:", a)
print("View:", b)
print("Copy:", c)
print("a is b:", a.base is None)
print("b base:", b.base is a)
