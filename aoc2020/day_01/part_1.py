from aoc2020 import *


class Solution(SolutionABC):
    expected = 514579

    def solve(self) -> any:
        return self.find_sum(2020, self.resource_lines("input", int))

    @classmethod
    def find_sum(cls, target, data) -> any:
        members = set()
        for n in data:
            if target - n in members:
                return (target - n) * n
            members.add(n)
        return None
