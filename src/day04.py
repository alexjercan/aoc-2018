import re

from datetime import datetime
from typing import List, Tuple

FALLS_ASLEEP = "falls asleep"
WAKES_UP = "wakes up"


class NightEntry:
    def __init__(self, guard_id: int, timestamps: List[Tuple[datetime, str]]):
        self.guard_id = guard_id
        self.timestamps = timestamps

        self.minutes = [0 for _ in range(60)]
        for i in range(0, len(self.timestamps), 2):
            start = self.timestamps[i][0]
            end = self.timestamps[i+1][0]
            for j in range(start.minute, end.minute):
                self.minutes[j] += 1


def parse_input(input: str):
    def parse_entry(entry: str):
        if entry == FALLS_ASLEEP or entry == WAKES_UP:
            return entry
        return int(re.findall(r".*#(\d+).*", entry)[0])

    def to_date_entry(entry: str):
        date_time_obj = datetime.strptime(entry, '%Y-%m-%d %H:%M')
        return date_time_obj

    expr = r"^\[(.*?)\]\W+(.*?)$"
    entries = list(map(lambda line: re.findall(
        expr, line)[0], input.splitlines()))
    entries = list(
        map(lambda tup: (to_date_entry(tup[0]), parse_entry(tup[1])), entries))
    entries = sorted(entries, key=lambda tup: tup[0])

    gid = None
    timestamps = []
    night_entries = []
    for entry in entries:
        if isinstance(entry[1], int):
            if gid is not None:
                night_entries.append(NightEntry(gid, timestamps))
            gid = entry[1]
            timestamps = []
        else:
            timestamps.append(entry)

    return night_entries


def part1(entries: List[NightEntry]):
    schedule = dict()

    for entry in entries:
        guard_id = entry.guard_id
        minutes = entry.minutes

        if guard_id in schedule:
            for i, minute in enumerate(minutes):
                schedule[guard_id][i] += minute
        else:
            schedule[guard_id] = list(minutes)

    max_sleep = 0
    max_guard = None
    for guard_id in schedule:
        sleep = sum(schedule[guard_id])
        if sleep > max_sleep:
            max_sleep = sleep
            max_guard = guard_id

    max_sleep = 0
    max_minute = None
    for i, minute in enumerate(schedule[max_guard]):
        if minute > max_sleep:
            max_sleep = minute
            max_minute = i

    return max_minute * max_guard


def part2(entries: List[NightEntry]):
    schedule = dict()

    for entry in entries:
        guard_id = entry.guard_id
        minutes = entry.minutes

        if guard_id in schedule:
            for i, minute in enumerate(minutes):
                schedule[guard_id][i] += minute
        else:
            schedule[guard_id] = list(minutes)

    max_sleep = 0
    max_minute = None
    max_guard = None
    for guard_id in schedule:
        for i, minute in enumerate(schedule[guard_id]):
            if minute > max_sleep:
                max_sleep = minute
                max_minute = i
                max_guard = guard_id

    return max_minute * max_guard


def solve(input: str) -> str:
    input = parse_input(input)
    return f"Day04\nPart1: {part1(input)}\nPart2: {part2(input)}\n"
