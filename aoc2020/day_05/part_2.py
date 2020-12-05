from aoc2020 import *
from .part_1 import Solution as Part_1


class Solution(Part_1):
    expected = 120

    def solve(self) -> any:
        all_seats = set(self.resource_lines("input", self.int))
        for seat_id in all_seats:
            if seat_id + 1 not in all_seats:
                return seat_id + 1
        raise NoSolutionError()
