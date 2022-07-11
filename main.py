import sys
import argparse

import src.day01 as day01
import src.day02 as day02
import src.day03 as day03
import src.day04 as day04
import src.day05 as day05
import src.day06 as day06
import src.day07 as day07
import src.day08 as day08
import src.day09 as day09
import src.day10 as day10
import src.day11 as day11
import src.day12 as day12
import src.day13 as day13
import src.day14 as day14
import src.day15 as day15
import src.day16 as day16
import src.day17 as day17
import src.day18 as day18
import src.day19 as day19
import src.day20 as day20
import src.day21 as day21
import src.day22 as day22
import src.day23 as day23
import src.day24 as day24
import src.day25 as day25


def solve(day, input):
    if day == 1:
        return day01.solve(input)
    if day == 2:
        return day02.solve(input)
    if day == 3:
        return day03.solve(input)
    if day == 4:
        return day04.solve(input)
    if day == 5:
        return day05.solve(input)
    if day == 6:
        return day06.solve(input)
    if day == 7:
        return day07.solve(input)
    if day == 8:
        return day08.solve(input)
    if day == 9:
        return day09.solve(input)
    if day == 10:
        return day10.solve(input)
    if day == 11:
        return day11.solve(input)
    if day == 12:
        return day12.solve(input)
    if day == 13:
        return day13.solve(input)
    if day == 14:
        return day14.solve(input)
    if day == 15:
        return day15.solve(input)
    if day == 16:
        return day16.solve(input)
    if day == 17:
        return day17.solve(input)
    if day == 18:
        return day18.solve(input)
    if day == 19:
        return day19.solve(input)
    if day == 20:
        return day20.solve(input)
    if day == 21:
        return day21.solve(input)
    if day == 22:
        return day22.solve(input)
    if day == 23:
        return day23.solve(input)
    if day == 24:
        return day24.solve(input)
    if day == 25:
        return day25.solve(input)


def main():
    parser = argparse.ArgumentParser(description="Aoc 2018")
    parser.add_argument("day", type=int)
    args = parser.parse_args()

    input = sys.stdin.read()
    print(solve(args.day, input))


if __name__ == "__main__":
    main()
