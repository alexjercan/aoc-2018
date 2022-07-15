import re

import numpy as np
import matplotlib.pyplot as plt

def parse_input(input):
  return np.array(list(map(lambda line: list(map(int, re.findall(r"position=<([ -]?\d+), ([ -]?\d+)> velocity=<([ -]?\d+), ([ -]?\d+)>", line)[0])), input.splitlines())))

def step_n(lights: np.ndarray, n):
  new_lights = lights.copy()

  new_lights[:, 0] += new_lights[:, 2] * n
  new_lights[:, 1] += new_lights[:, 3] * n

  return new_lights


def get_max_scatter_axis(lights, axis=0):
  return lights[:, axis].max() - lights[:, axis].min()


def display(lights):
  lights_set = set(list(map(tuple, lights[:, 0:2])))

  themap = ""
  for row in range(lights[:, 1].min(), lights[:, 1].max() + 1):
    for col in range(lights[:, 0].min(), lights[:, 0].max() + 1):
      themap += "#" if (col, row) in lights_set else "."
    themap += "\n"
  
  return themap


def solve(input: str) -> str:
  lights = parse_input(input)
  min_val, min_i = get_max_scatter_axis(lights, 0) + get_max_scatter_axis(lights, 1), None
  for i in range(20_000):
    lights_aux = step_n(lights, i)
    scatter_value = get_max_scatter_axis(lights_aux, 0) + get_max_scatter_axis(lights_aux, 1)
    if scatter_value < min_val:
      min_val = scatter_value
      min_i = i

  lights = step_n(lights, min_i)

  return f"Day10\nPart1:\n{display(lights)}Part2: {min_i}\n"