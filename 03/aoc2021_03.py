print("Part 1")
with open("input.txt", "r") as f:
    binary_numbers = f.read()

    binary_numbers = [line for line in binary_numbers.splitlines()]

    binary_gamma = ""
    binary_epsilon = ""
    for position in range(len(binary_numbers[0])):
        zeros = 0
        ones = 0
        for n in [num[position] for num in binary_numbers]:
            if n == "0":
                zeros += 1
            elif n == "1":
                ones += 1
            else:
                raise("Somthing is not ok!")

        if ones > zeros:
            binary_gamma += "1"
            binary_epsilon += "0"
        else:
            binary_gamma += "0"
            binary_epsilon += "1"

    decimal_gamma = int(binary_gamma, 2)
    decimal_epsilon = int(binary_epsilon, 2)

    print(f"gamma={decimal_gamma}({binary_gamma}), epsilon={decimal_epsilon}({binary_epsilon}) --> multiplied={decimal_epsilon*decimal_gamma}")
