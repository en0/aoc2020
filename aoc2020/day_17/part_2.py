from aoc2020 import *
from functools import reduce
from .space_4d import Space4d


class Solution(SolutionABC):
    expected = 848

    def solve(self) -> any:
        space = Space4d(reduce(lambda a, b: a + b, [
            [((x, y, 0, 0), s == '#') for x, s in enumerate(r)]
            for y, r in enumerate(self.resource_lines("input"))
        ]))
        return reduce(lambda a, b: space.simulate(), range(6), None)
