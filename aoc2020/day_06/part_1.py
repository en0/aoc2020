from aoc2020 import *


class Solution(SolutionABC):
    expected = 11
    c2i = lambda s, c: ord(c) - ord('a')

    def solve(self) -> any:
        rt, yes_answers = 0, [0] * 26
        for line in self.resource_lines("input"):
            if line == "":
                rt += sum(yes_answers)
                yes_answers = [0] * 26
            else:
                for c in line:
                    yes_answers[self.c2i(c)] = 1
        return rt + sum(yes_answers)
