from aoc2020 import *


class Solution(SolutionABC):

    expected = 241861950

    def solve(self) -> any:
        target = 2020
        values = list(self.resource_lines("input", int))
        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                for l in range(j + 1, len(values)):
                    if values[i] + values[j] + values[l] == target:
                        return values[i] * values[j] * values[l]

        raise NoSolutionError()
