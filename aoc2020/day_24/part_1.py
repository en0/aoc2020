from aoc2020 import *
from functools import reduce
from collections import Counter

from .path_parser import path_parser

move = {
    "ne": (lambda x, y, z: (x, y - 1, z + 1)),
    "sw": (lambda x, y, z: (x, y + 1, z - 1)),

    "nw": (lambda x, y, z: (x - 1, y, z + 1)),
    "se": (lambda x, y, z: (x + 1, y, z - 1)),

    "e":  (lambda x, y, z: (x + 1, y - 1, z)),
    "w":  (lambda x, y, z: (x - 1, y + 1, z)),
}


class Solution(SolutionABC):
    expected = 10

    @classmethod
    def parse_path(cls, path):
        return reduce(lambda a, b: move[b](*a), path_parser(path), (0, 0, 0))

    def load_black_tile(self):
        d = Counter([coord for coord in self.resource_lines("input", self.parse_path)])
        return {k: v for k, v in d.items() if v % 2 != 0}

    def solve(self) -> any:
        black_tiles = self.load_black_tile()
        return len(black_tiles)
