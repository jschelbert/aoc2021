import numpy as np

print("Part 1")
my_data = np.loadtxt('input.txt', delimiter=',')
best_height = np.median(my_data)

print(f"{sum(abs(my_data - best_height))}")


print("Part 2")
best_height2 = np.floor(np.mean(my_data))

print(f"{sum([j for i in abs(my_data - best_height2) for j in range(1, int(i)+1)])} or {sum([j for i in abs(my_data - best_height2 - 1) for j in range(1, int(i)+1)])}")