from aoc2020 import *


class Solution(SolutionABC):
    expected = 220

    def solve(self) -> any:
        last_value = 0
        deltas = {1: 0, 3: 1}
        for a in sorted(self.resource_lines("input", int)):
            deltas[a - last_value] += 1
            last_value = a
        return deltas[1] * deltas[3]
