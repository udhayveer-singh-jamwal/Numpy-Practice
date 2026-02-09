import numpy as np

expenses = np.array([12000, 15000, 10000, 18000, 16000, 14000])
total = expenses.sum()
avg = expenses.mean()
max_exp = expenses.max()
min_exp = expenses.min()
above_avg = expenses[expenses > avg]

print("Monthly Expenses:", expenses)
print("Total Expense:", total)
print("Average Expense:", avg)
print("Highest Expense:", max_exp)
print("Lowest Expense:", min_exp)
print("Above Average Months:", above_avg)
expenses[expenses < avg] += 2000
print("Adjusted Expenses:", expenses)
