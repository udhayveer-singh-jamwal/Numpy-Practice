import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

total_sum = data.sum()
row_sum = data.sum(axis=1)
col_sum = data.sum(axis=0)

mean_val = data.mean()
max_val = data.max()
min_val = data.min()

print("Total Sum:", total_sum)
print("Row-wise Sum:", row_sum)
print("Column-wise Sum:", col_sum)
print("Mean:", mean_val)
print("Max:", max_val)
print("Min:", min_val)
