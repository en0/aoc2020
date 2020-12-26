from aoc2020 import *
from datetime import datetime


class Solution(SolutionABC):
    expected = 149245887792

    def solve(self) -> any:
        cups = next(self.resource_lines("input", lambda l: [int(i) for i in l]))
        max_cup_value = max(cups)
        cups = cups + list(range(max_cup_value + 1, 1000000+1))
        max_cup_value = max(cups)
        # pretty sure this is a modulo math problem, not a algorithm problem.
        raise NoSolutionError()
