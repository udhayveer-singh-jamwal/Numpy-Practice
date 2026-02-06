import numpy as np

sales = np.array([1200, 1500, 800, 2000, 1700, 900])

total_sales = sales.sum()
average_sales = sales.mean()
highest_sale = sales.max()
lowest_sale = sales.min()
above_avg = sales[sales > average_sales]

print("Sales Data:", sales)
print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Highest Sale:", highest_sale)
print("Lowest Sale:", lowest_sale)
print("Above Average Sales:", above_avg)
sales[sales < 1000] += 300
print("Updated Sales:", sales)
