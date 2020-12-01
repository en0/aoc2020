from aoc2020 import *


class Solution(SolutionABC):

    expected = 241861950

    def solve(self) -> any:
        target = 2020
        values = sorted(self.resource_lines("input", int))
        for l in range(len(values)):
            i = l + 1
            j = len(values) - 1
            while i < j:
                actual = values[l] + values[i] + values[j]
                if actual == target:
                    return values[l] * values[i] * values[j]
                elif actual < target:
                    i += 1
                elif actual > target:
                    j -= 1

        raise NoSolutionError()
