def part1(input: str) -> int:
    return sum(map(int, input.splitlines()))


def part2(input: str) -> int:
    adjustments = list(map(int, input.splitlines()))
    visited = set()
    freq = 0

    while True:
        for a in adjustments:
            freq = freq + a
            if freq in visited:
                return freq
            visited.add(freq)


def solve(input: str) -> str:
    return f"Day01\nPart1: {part1(input)}\nPart2: {part2(input)}\n"
