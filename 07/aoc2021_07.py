import numpy as np

print("Part 1")
my_data = np.loadtxt('input.txt', delimiter=',')
best_height = np.median(my_data)

print(f"{sum(abs(my_data - best_height))}")
