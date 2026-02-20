import numpy as np

sales = np.array([
    [1200, 1500, 1800],
    [1000, 1700, 1600],
    [2000, 2200, 2100],
    [900,  1100, 1300]
])

monthly_total = sales.sum(axis=1)
product_total = sales.sum(axis=0)
best_month = np.argmax(monthly_total)
best_product = np.argmax(product_total)
print("Sales Data:\n", sales)
print("Monthly Total:", monthly_total)
print("Product Total:", product_total)
print("Best Month Index:", best_month)
print("Best Product Index:", best_product)
