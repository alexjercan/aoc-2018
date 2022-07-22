import numpy as np

from scipy.spatial import distance


def parse_input(input: str):
    return np.array(
        list(map(lambda line: list(map(int, line.split(", "))), input.splitlines()))
    )


def part1(points):
    xmin, ymin = points.min(axis=0) - 1
    xmax, ymax = points.max(axis=0) + 2

    xgrid, ygrid = np.meshgrid(np.arange(xmin, xmax), np.arange(xmin, xmax))
    targets = np.dstack([xgrid, ygrid]).reshape(-1, 2)

    cityblock = distance.cdist(points, targets, metric="cityblock")

    closest_origin = np.argmin(cityblock, axis=0)

    min_distances = np.min(cityblock, axis=0)
    competing_locations_filter = (cityblock == min_distances).sum(axis=0) > 1

    closest_origin[competing_locations_filter] = len(points) + 1
    closest_origin = closest_origin.reshape(xgrid.shape)
    infinite_ids = np.unique(
        np.vstack(
            [
                closest_origin[0],
                closest_origin[-1],
                closest_origin[:, 0],
                closest_origin[:, -1],
            ]
        )
    )
    closest_origin[np.isin(closest_origin, infinite_ids)] = len(points) + 1

    return np.max(np.bincount(closest_origin.ravel())[:-1])


def part2(points):
    xmin, ymin = points.min(axis=0) - 1
    xmax, ymax = points.max(axis=0) + 2

    xgrid, ygrid = np.meshgrid(np.arange(xmin, xmax), np.arange(xmin, xmax))
    targets = np.dstack([xgrid, ygrid]).reshape(-1, 2)

    cityblock = distance.cdist(points, targets, metric="cityblock")

    origin_distances = cityblock.sum(axis=0)

    region = np.where(origin_distances < 10000, 1, 0)

    return region.sum()


def solve(input: str) -> str:
    input = parse_input(input)
    return f"Day06\nPart1: {part1(input)}\nPart2: {part2(input)}\n"
