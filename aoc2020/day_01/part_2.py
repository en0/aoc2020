from aoc2020 import *
from .part_1 import Solution as Part1


class Solution(Part1):
    expected = 241861950

    def solve(self) -> any:
        return self.find_sum_of_3(2020, list(self.resource_lines("input", int)))

    def find_sum_of_3(self, target, data):
        for n in data:
            x = self.find_sum(target-n, data)
            if x is not None:
                return x * n
        return None
