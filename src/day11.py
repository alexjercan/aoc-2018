import numpy as np


def parse_input(input):
    return int(input)


def part1(serial_number):
    def power_level(x, y):
        rack_id = x + 11
        column_number = y + 1
        return (rack_id * column_number + serial_number) * rack_id // 100 % 10 - 5

    grid = np.fromfunction(power_level, (300, 300))

    k = 3
    windows = sum(
        grid[x : x - k + 1 or None, y : y - k + 1 or None]
        for x in range(k)
        for y in range(k)
    )
    maximum = int(windows.max())
    location = np.where(windows == maximum)

    return f"{location[0][0] + 1},{location[1][0] + 1}"


def part2(serial_number):
    def power_level(x, y):
        rack_id = x + 11
        column_number = y + 1
        return (rack_id * column_number + serial_number) * rack_id // 100 % 10 - 5

    grid = np.fromfunction(power_level, (300, 300))

    max_value = 0
    max_location = None
    max_k = None
    for k in range(3, 300):
        windows = sum(
            grid[x : x - k + 1 or None, y : y - k + 1 or None]
            for x in range(k)
            for y in range(k)
        )
        maximum = int(windows.max())
        location = np.where(windows == maximum)
        if maximum > max_value:
            max_value = maximum
            max_location = location
            max_k = k

    return f"{max_location[0][0] + 1},{max_location[1][0] + 1},{max_k}"


def solve(input: str) -> str:
    serial_number = parse_input(input)
    return f"Day11\nPart1: {part1(serial_number)}\nPart2: {part2(serial_number)}\n"
