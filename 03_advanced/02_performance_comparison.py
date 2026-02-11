import numpy as np
import time

py_list = list(range(1_000_000))
np_array = np.array(py_list)

start = time.time()
py_result = [x * 5 for x in py_list]
print("Python List Time:", time.time() - start)

start = time.time()
np_result = np_array * 5
print("NumPy Array Time:", time.time() - start)
