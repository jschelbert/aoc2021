overall_increase = 0
temp_num = 1000000000

print("Part 1")
with open("input.txt", "r") as f:
    numbers = f.read()

    for line in numbers.splitlines():
        num = int(line)
        if num > temp_num:
            overall_increase += 1
        temp_num = num

    print(f"There were {overall_increase} increases")


overall_increase = 0
temp_num = 1000000000

print("Part 2")
with open("input.txt", "r") as f:
    numbers = f.read()
    numbers = [int(line) for line in numbers.splitlines()]
    sliding_window = [sum(numbers[i:i+3]) for i in range(0, len(numbers)-2)]
    for num in sliding_window:
        if num > temp_num:
            overall_increase += 1
        temp_num = num
    print(f"There were {overall_increase} increases")