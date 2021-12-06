
distance = 0
depth = 0
aim = 0


with open("input.txt", "r") as f:
    orders = f.read()

    for line in orders.splitlines():
        command, number = line.split()

        number = int(number)

        if command == "forward":
            distance += number
            depth += aim * number
        elif command == "down":
            aim += number
        elif command == "up":
            aim -= number
        else:
            raise("cannot read command")

    print(f"depth={depth}, distance={distance} --> Multiplied={depth * distance}")