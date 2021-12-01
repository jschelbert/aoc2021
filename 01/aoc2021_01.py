overall_increase = 0
temp_num = 1000000000

with open("input.txt", "r") as f:
    numbers = f.read()

    for line in numbers.splitlines():
        num = int(line)
        if num > temp_num:
            overall_increase += 1
        temp_num = num

    print(f"There were {overall_increase} increases")