from aoc2020 import *
from functools import reduce


class Solution(SolutionABC):

    expected = 336

    def solve(self) -> any:
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        track = {t: (t[0], t[1], 0) for t in slopes}
        for current_y, row in enumerate(self.resource_lines("input")):
            for slope, (x, y, rt) in track.items():
                if y != current_y:
                    continue
                rt += 1 if row[x] == '#' else 0
                x = (x + slope[0]) % len(row)
                y += slope[1]
                track[slope] = (x, y, rt)
        return reduce(lambda a, b: a*b, map(lambda a: a[2], track.values()))
