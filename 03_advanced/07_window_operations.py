import numpy as np

data = np.array([10, 20, 30, 40, 50, 60, 70])
window = 3
moving_avg = []
for i in range(len(data) - window + 1):
    avg = data[i:i+window].mean()
    moving_avg.append(avg)

print("Data:", data)
print("Moving Average:", moving_avg)
