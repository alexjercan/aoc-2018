from collections import Counter


def part1(input: str) -> int:
    box_ids = list(map(Counter, input.splitlines()))

    twos, threes = 0, 0
    for box_id in box_ids:
        ids = box_id.values()
        twos += int(2 in ids)
        threes += int(3 in ids)

    return twos * threes


def part2(input: str) -> str:
    def similar(str1: str, str2: str) -> int:
        found = -1
        for i, (c1, c2) in enumerate(zip(str1, str2)):
            if c1 != c2 and found != -1:
                return -1
            elif c1 != c2:
                found = i
        return found

    strings = input.splitlines()
    for i1 in range(len(strings)):
        for i2 in range(i1 + 1, len(strings)):
            i = similar(strings[i1], strings[i2])
            if i != -1:
                return strings[i1][:i] + strings[i1][i + 1 :]

    return ""


def solve(input: str) -> str:
    return f"Day02\nPart1: {part1(input)}\nPart2: {part2(input)}\n"
