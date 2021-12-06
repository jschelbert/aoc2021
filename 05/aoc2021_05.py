


print("Part 1")
with open("input.txt", "r") as f:
    lines = f.read().splitlines()

    line_segments = []
    for line in lines:
        point1, point2 = line.split(' -> ')
        x1, y1 = map(int, point1.split(','))
        x2, y2 = map(int, point2.split(','))
        line_segments.append(((x1, y1), (x2, y2)))

    coordinate_frequencies = {}
    for (x1, y1), (x2, y2) in line_segments:
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                coordinate_frequencies[(x1, i)] = coordinate_frequencies.get((x1, i), 0) + 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                coordinate_frequencies[(i, y1)] = coordinate_frequencies.get((i, y1), 0) + 1

    print(sum(frequency > 1 for frequency in coordinate_frequencies.values()))


print("Part 2")

def sign(x):
    return (x > 0) - (x < 0)

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

    line_segments = []
    for line in lines:
        point1, point2 = line.split(' -> ')
        x1, y1 = map(int, point1.split(','))
        x2, y2 = map(int, point2.split(','))
        line_segments.append(((x1, y1), (x2, y2)))

    coordinate_frequencies = {}
    for (x1, y1), (x2, y2) in line_segments:
        x_inc, y_inc = sign(x2 - x1), sign(y2 - y1)
        while (x1, y1) != (x2 + x_inc, y2 + y_inc):
            coordinate_frequencies[(x1, y1)] = coordinate_frequencies.get((x1, y1), 0) + 1
            x1 += x_inc
            y1 += y_inc

    print(sum(frequency > 1 for frequency in coordinate_frequencies.values()))