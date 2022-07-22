def parse_input(input):
    return int(input)


def step(scores, p1, p2):
    scores += str(int(scores[p1]) + int(scores[p2]))

    p1 = (p1 + 1 + int(scores[p1])) % len(scores)
    p2 = (p2 + 1 + int(scores[p2])) % len(scores)

    return scores, p1, p2


def part1(num_recipes):
    scores = "37"
    p1, p2 = 0, 1
    for _ in range(num_recipes + 15):
        scores, p1, p2 = step(scores, p1, p2)

    return scores[int(num_recipes) : int(num_recipes) + 10]


def part2(num_recipes):
    recipes = str(num_recipes)
    score = "37"
    elf1 = 0
    elf2 = 1
    while recipes not in score[-7:]:
        score += str(int(score[elf1]) + int(score[elf2]))
        elf1 = (elf1 + int(score[elf1]) + 1) % len(score)
        elf2 = (elf2 + int(score[elf2]) + 1) % len(score)

    return score.index(recipes)


def solve(input: str) -> str:
    num_recipes = parse_input(input)
    return f"Day14\nPart1: {part1(num_recipes)}\nPart2: {part2(num_recipes)}\n"
