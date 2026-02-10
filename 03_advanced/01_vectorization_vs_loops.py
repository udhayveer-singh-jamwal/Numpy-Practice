import numpy as np
import time

data = np.arange(1, 1_000_001)

# Python loop
start = time.time()
s = 0
for i in data:
    s += i * 2
print("Loop Sum:", s)
print("Loop Time:", time.time() - start)

# NumPy vectorization
start = time.time()
result = np.sum(data * 2)
print("Vectorized Sum:", result)
print("Vectorized Time:", time.time() - start)
