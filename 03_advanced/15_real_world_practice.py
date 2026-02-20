import numpy as np

sales = np.array([
    [1200, 1500, 1800],
    [1000, 1700, 1600],
    [2000, 2200, 2100],
    [900,  1100, 1300]
])

monthly_total = sales.sum(axis=1)
product_total = sales.sum(axis=0)

print("Sales Data:\n", sales)
print("Monthly Total:", monthly_total)
