from aoc2020 import *


class Solution(SolutionABC):

    expected = 514579

    def solve(self) -> any:
        target = 2020
        values = sorted(self.resource_lines("input", int))
        i, j = 0, len(values) - 1
        while i < j:
            actual = values[i] + values[j]
            if actual == target:
                return values[i] * values[j]
            elif actual < target:
                i += 1
            elif actual > target:
                j -= 1
        raise NoSolutionError()
