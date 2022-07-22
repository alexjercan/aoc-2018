import re
import heapq

from collections import defaultdict
from copy import deepcopy


def parse_input(input: str):
    edges = list(
        map(
            lambda line: re.findall(
                r"Step (\w) must be finished before step (\w) can begin.", line
            )[0],
            input.splitlines(),
        )
    )
    graph = defaultdict(list)

    for (edge_start, edge_end) in edges:
        graph[edge_start].append(edge_end)

    return graph


def get_all_vertices(graph: dict):
    keys = list(graph.keys())
    values = [v for vs in graph.values() for v in vs]
    return list(set(keys + values))


def has_incoming_edges(node: str, graph: dict):
    values = [v for vs in graph.values() for v in vs]
    return node in values


def part1(graph: dict):
    vertices = get_all_vertices(graph)
    result = []
    s = list([v for v in vertices if not has_incoming_edges(v, graph)])
    heapq.heapify(s)

    while s:
        node = heapq.heappop(s)
        result.append(node)
        children = list(graph[node])
        for child in children:
            graph[node].remove(child)
            if not has_incoming_edges(child, graph):
                heapq.heappush(s, child)

    if [v for vs in graph.values() for v in vs]:
        return "CYCLE DETECTED"

    return "".join(result)


def part2(graph):
    vertices = get_all_vertices(graph)
    result = []
    s = list([v for v in vertices if not has_incoming_edges(v, graph)])
    heapq.heapify(s)
    workers = dict()

    def can_add_worker():
        return len(workers.keys()) < 5

    def add_worker(node):
        workers[node] = ord(node) - ord("A") + 61

    def do_work():
        for key in workers:
            workers[key] -= 1

        keys_to_remove = []
        for key in workers:
            if workers[key] <= 0:
                keys_to_remove.append(key)

        for key in keys_to_remove:
            del workers[key]

        return keys_to_remove

    def done_work():
        return len(workers.keys()) == 0

    steps = 0
    while s or not done_work():
        while can_add_worker() and s:
            node = heapq.heappop(s)
            add_worker(node)

        finished_nodes = do_work()
        steps += 1

        for node in finished_nodes:
            result.append(node)
            children = list(graph[node])
            for child in children:
                graph[node].remove(child)
                if not has_incoming_edges(child, graph):
                    heapq.heappush(s, child)

    return steps


def solve(input: str) -> str:
    input = parse_input(input)
    graph = deepcopy(input)
    return f"Day07\nPart1: {part1(input)}\nPart2: {part2(graph)}\n"
