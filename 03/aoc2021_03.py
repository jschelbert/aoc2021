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

print("Part 2")
with open("input.txt", "r") as f:
    binary_numbers = f.read()

    binary_numbers = [line for line in binary_numbers.splitlines()]
    binary_numbers_oxygen = binary_numbers
    binary_numbers_co2 = binary_numbers

    binary_oxygen = ""
    binary_co2 = ""
    for position in range(len(binary_numbers[0])):
        zeros = 0
        ones = 0
        for n in [num[position] for num in binary_numbers_oxygen]:
            if n == "0":
                zeros += 1
            elif n == "1":
                ones += 1
            else:
                raise("Somthing is not ok!")

        if len(binary_numbers_oxygen) == 1:
            binary_oxygen += binary_numbers_oxygen[0][position]
        elif ones >= zeros:
            binary_oxygen += "1"
        else:
            binary_oxygen += "0"
        binary_numbers_oxygen = [num for num in binary_numbers_oxygen if num[position] == binary_oxygen[position]]

        # do the same thing for co2
        zeros = 0
        ones = 0
        for n in [num[position] for num in binary_numbers_co2]:
            if n == "0":
                zeros += 1
            elif n == "1":
                ones += 1
            else:
                print("error!")
                raise ("Somthing is not ok!")

        if len(binary_numbers_co2) == 1:
            binary_co2 += binary_numbers_co2[0][position]
        elif ones >= zeros:
            binary_co2 += "0"
        else:
            binary_co2 += "1"
        binary_numbers_co2 = [num for num in binary_numbers_co2 if num[position] == binary_co2[position]]


    decimal_oxygen = int(binary_oxygen, 2)
    decimal_co2 = int(binary_co2, 2)

    print(f"oxygen={decimal_oxygen}({binary_oxygen}), co2={decimal_co2}({binary_co2}) --> multiplied={decimal_oxygen*decimal_co2}")