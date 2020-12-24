from functools import reduce
from aoc2020 import *


class Solution(SolutionABC):
    expected = 5

    @classmethod
    def parse_food(cls, line):
        ing, alr = line.split(" (contains ")
        ing = ing.split(" ")
        alr = alr.rstrip(")").split(", ")
        return ing, alr

    def solve(self) -> any:
        all_ing = set()
        alr_dict = dict()
        ing_count = dict()
        for ing, alr in self.resource_lines("input", self.parse_food):
            for w in ing:
                ing_count.setdefault(w, 0)
                ing_count[w] += 1
            _ing = set(ing)
            for _alr in alr:
                if _alr in alr_dict:
                    alr_dict[_alr] &= _ing
                else:
                    alr_dict[_alr] = _ing.copy()
            all_ing |= _ing

        ret = 0
        for ing in all_ing - reduce(lambda a, b: a | b, alr_dict.values(), set()):
            ret += ing_count[ing]

        print(alr_dict)
        return ret
