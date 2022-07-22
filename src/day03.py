import re

from collections import defaultdict


def part1(input: str) -> int:
    def entry_to_points(entry: str) -> list:
        expr = r"^#\d+\W+@\W+(\d+),(\d+):\W+(\d+)x(\d+)$"
        [x, y, w, h] = list(map(int, re.findall(expr, entry)[0]))
        result = []
        for i in range(w):
            for j in range(h):
                result.append((x + i, y + j))

        return result

    counter = defaultdict(int)
    for entry in input.splitlines():
        for point in entry_to_points(entry):
            counter[point] += 1

    return len(list(filter(lambda x: x > 1, counter.values())))


def part2(input: str) -> int:
    def entry_to_rect(entry: str) -> list:
        expr = r"^#(\d+)\W+@\W+(\d+),(\d+):\W+(\d+)x(\d+)$"
        return tuple(map(int, re.findall(expr, entry)[0]))

    def intersects(r1, r2):
        _, x1, y1, w1, h1 = r1
        _, x2, y2, w2, h2 = r2

        return not (x1 + w1 < x2 or x1 > x2 + w2 or y1 > y2 + h2 or y1 + h1 < y2)

    rects = list(map(entry_to_rect, input.splitlines()))
    for i, r1 in enumerate(rects):
        ok = True
        for j, r2 in enumerate(rects):
            if i == j:
                continue
            if intersects(r1, r2):
                ok = False
                break

        if ok:
            return r1[0]

    return -1


def solve(input: str) -> str:
    return f"Day03\nPart1: {part1(input)}\nPart2: {part2(input)}\n"
