import re

from collections import deque, defaultdict


def parse_input(input):
  return tuple(map(int, re.findall(r"(\d+) players; last marble is worth (\d+) points", input)[0]))

def play_game(num_players, last_marble):
  circle = deque([0])
  scores = defaultdict(int)

  for marble in range(1, last_marble + 1):
    if marble % 23 == 0:
      circle.rotate(7)
      scores[marble % num_players] += marble + circle.pop()
      circle.rotate(-1)
    else:
      circle.rotate(-1)
      circle.append(marble)

  return max(scores.values()) if scores else 0


def part1(input):
  return play_game(*input)


def part2(input):
  num_players, last_marble = input
  return play_game(num_players, last_marble * 100)


def solve(input: str) -> str:
  input = parse_input(input)
  return f"Day09\nPart1: {part1(input)}\nPart2: {part2(input)}\n"