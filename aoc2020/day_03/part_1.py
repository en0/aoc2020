from aoc2020 import *


class Solution(SolutionABC):

    expected = 7

    def solve(self) -> any:
        x, rt, rows = 0, 0, self.resource_lines("input")
        try:
            # Discard the first row
            next(rows)
            while True:
                row = next(rows)
                x = (x + 3) % len(row)
                if row[x] == '#':
                    rt += 1
        except StopIteration:
            return rt
