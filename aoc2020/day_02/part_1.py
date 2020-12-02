from aoc2020 import *


def check_pw(line: str):
    policy, pw = line.split(': ', 2)
    limits, letter = policy.split(' ')
    lower, upper = limits.split('-')
    return 1 if int(lower) <= pw.count(letter) <= int(upper) else 0


class Solution(SolutionABC):
    """ How many passwords are valid according to their policies? """

    expected = 2

    def solve(self) -> any:
        return sum(self.resource_lines("input", check_pw))
