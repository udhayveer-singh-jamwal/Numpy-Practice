import numpy as np

np.random.seed(42)

random_data = np.random.randint(50, 100, size=100)

mean = random_data.mean()
std = random_data.std()

print("Random Data Sample:", random_data[:10])
print("Mean:", mean)
print("Std Dev:", std)
