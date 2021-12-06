
def count_lanternfish(lanternfish, days):
    cycle_counts = [0] * 9
    for cycle in lanternfish:
        cycle_counts[cycle] += 1

    for _ in range(days):
        new_cycle_counts = cycle_counts[1:] + cycle_counts[:1]
        new_cycle_counts[6] += cycle_counts[0]
        cycle_counts = new_cycle_counts
    return sum(cycle_counts)

with open("input.txt", "r") as f:
    fish_timer = f.read()
    fish_timer = [int(i) for i in fish_timer.split(",")]

    sol_part2 = count_lanternfish(fish_timer, 256)

    print("Part 1")
    max_day = 80
    #print(f"0: {fish_timer}")
    for day_timer in range(1, max_day+1):
        fish_timer_new = [i-1 for i in fish_timer]
        fish_timer_new = fish_timer_new + ([8] * fish_timer_new.count(-1))
        fish_timer = [i if i != -1 else 6 for i in fish_timer_new]
        #print(f"{day_timer}: {fish_timer}")

    print(len(fish_timer))

    print("Part 2")
    print(sol_part2)

