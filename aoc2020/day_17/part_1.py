from aoc2020 import *
from functools import reduce
from .space import Space


class Solution(SolutionABC):
    expected = 112

    def solve(self) -> any:
        space = Space(reduce(lambda a, b: a + b, [
            [((x, y, 0), s == '#') for x, s in enumerate(r)]
            for y, r in enumerate(self.resource_lines("input"))
        ]))
        return reduce(lambda a, b: space.simulate(), range(6), None)
