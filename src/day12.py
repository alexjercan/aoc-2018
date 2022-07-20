import re


def parse_input(input: str):
  lines = input.splitlines()
  initial_state = lines[0].split(": ")[1]

  rules = dict()
  for line in lines[2:]:
    (x, y) = re.findall(r"([#\.]+) => ([#\.])", line)[0]
    rules[x] = y

  return initial_state, rules


def indices(lst, element):
  result = []
  offset = -1
  while True:
    try:
      offset = lst.index(element, offset+1)
    except ValueError:
      return result
    result.append(offset)


def count_num_index(current_state, rules, num_gens):
  for _ in range(num_gens):
    current_state = "..." + current_state + "..."
    aux_state = ""
    for i in range(len(current_state) - 4):
      aux_state += rules.get(current_state[i:i+5], ".")
    
    current_state = aux_state

  return sum(map(lambda idx: idx - num_gens, indices(list(current_state), "#")))


def part1(input):
  current_state, rules = input
  return count_num_index(current_state, rules, 20)


def part2(input):
  current_state, rules = input
  
  return count_num_index(current_state, rules, 200) + (50_000_000_000 - 200) * 63


def solve(input: str) -> str:
  input = parse_input(input)
  return f"Day12\nPart1: {part1(input)}\nPart2: {part2(input)}\n"