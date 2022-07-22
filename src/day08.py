from copy import copy


def parse_input(input: str):
    return list(map(int, input.strip().split(" ")))


def get_license(numbers):
    if not numbers:
        return 0

    num_children = numbers.pop(0)
    num_metadata = numbers.pop(0)

    partial_license = 0
    for _ in range(num_children):
        partial_license += get_license(numbers)

    for _ in range(num_metadata):
        partial_license += numbers.pop(0)

    return partial_license


def part1(numbers):
    return get_license(numbers)


def get_value_node(numbers):
    if not numbers:
        return 0

    num_children = numbers.pop(0)
    num_metadata = numbers.pop(0)

    if num_children == 0:
        value = 0
        for _ in range(num_metadata):
            value += numbers.pop(0)

        return value

    values = []
    for _ in range(num_children):
        values.append(get_value_node(numbers))

    value = 0
    for _ in range(num_metadata):
        idx = numbers.pop(0) - 1
        if idx < len(values):
            value += values[idx]

    return value


def part2(numbers):
    return get_value_node(numbers)


def solve(input: str) -> str:
    input = parse_input(input)
    numbers = copy(input)
    return f"Day08\nPart1: {part1(input)}\nPart2: {part2(numbers)}\n"
