def reacts(a, b):
    return a != b and a.upper() == b.upper()


def do_reaction(polymer):
    buf = []
    for c in polymer:
        if buf and reacts(c, buf[-1]):
            buf.pop()
        else:
            buf.append(c)
    return len(buf)


def part1(polymer: str):
    return do_reaction(polymer)


def part2(polymer):
    agents = set([c.lower() for c in polymer])
    return min(
        [do_reaction(polymer.replace(a, "").replace(a.upper(), "")) for a in agents]
    )


def solve(input: str) -> str:
    input = input.strip()

    return f"Day05\nPart1: {part1(input)}\nPart2: {part2(input)}\n"
