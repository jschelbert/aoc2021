print("Part 1")
with open("input.txt", "r") as f:
    numbers = f.read()

    counter_1478 = 0
    for line in numbers.splitlines():
        firstpart, secondpart = line.split(" | ")
        digits_scrambled = secondpart.split()
        counter_1478 += len([i for i in digits_scrambled if len(i) in [2, 3, 4, 7]])

    print(f"{counter_1478}")

print("Part 2")

with open("input.txt", "r") as f:
    numbers = f.read()

    overall_sum = 0

    for line in numbers.splitlines():
        firstpart, secondpart = line.split(" | ")

        mapping = {}

        digits_scrambled = firstpart.split()

        while len(mapping) < 10:
            for digit in digits_scrambled:
                # trivial mapping:
                if len(digit) == 2 and 1 not in mapping:
                    mapping[1] = "".join(sorted(digit))
                    continue
                if len(digit) == 3 and 7 not in mapping:
                    mapping[7] = "".join(sorted(digit))
                    continue
                if len(digit) == 4 and 4 not in mapping:
                    mapping[4] = "".join(sorted(digit))
                    continue
                if len(digit) == 7 and 8 not in mapping:
                    mapping[8] = "".join(sorted(digit))
                    continue

                if 1 not in mapping or 4 not in mapping:
                    continue

                # 2 or 3 or 5
                if len(digit) == 5 and len(set(digit).intersection(mapping[1])) == 2:
                    mapping[3] = "".join(sorted(digit))
                    continue
                if len(digit) == 5 and len(set(digit).intersection(mapping[4])) == 3:
                    mapping[5] = "".join(sorted(digit))
                    continue
                if len(digit) == 5 and len(set(digit).intersection(mapping[4])) == 2:
                    mapping[2] = "".join(sorted(digit))
                    continue

                # 6 or 9 or 0
                if len(digit) == 6 and len(set(digit).intersection(mapping[1])) == 1:
                    mapping[6] = "".join(sorted(digit))
                    continue
                if len(digit) == 6 and len(set(digit).intersection(mapping[4])) == 4:
                    mapping[9] = "".join(sorted(digit))
                    continue
                if len(digit) == 6 and len(set(digit).intersection(mapping[4])) == 3:
                    mapping[0] = "".join(sorted(digit))
                    continue
        mapping_reversed = {v: k for k, v in mapping.items()}

        current_scrambled_number = 0
        multiplier = 1000
        for number in secondpart.split():
            current_scrambled_number += multiplier * mapping_reversed["".join(sorted(number))]
            multiplier *= 0.1

        overall_sum += current_scrambled_number
    print(f"{overall_sum}")
