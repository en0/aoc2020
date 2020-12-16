from aoc2020 import *


class Solution(SolutionABC):
    expected = 436

    def solve(self) -> any:
        return self.spoken_at(2020)

    def spoken_at(self, t):
        i, i_map = 0, {}
        for val in self.resource_lines("input", int):
            i += 1
            i_map[val] = i
        said = val
        del i_map[val]
        while i < t:
            say = i - i_map[said] if said in i_map else 0
            i_map[said] = i
            said, i = say, i + 1
        return said
