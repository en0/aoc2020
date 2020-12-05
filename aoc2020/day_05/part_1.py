from aoc2020 import *


class Solution(SolutionABC):
    expected = 820
    c2n = lambda s, v: {'F': "0", 'B': "1", 'L': "0", 'R': "1"}[v]
    int = lambda s, v: int("".join(map(s.c2n, v)), 2)
    solve = lambda s: max(s.resource_lines("input", s.int))
