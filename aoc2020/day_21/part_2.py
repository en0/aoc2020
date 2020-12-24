from functools import reduce
from aoc2020 import *
from collections import deque


class Solution(SolutionABC):

    expected = "mxmxvkd,sqjhc,fvjkl"

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

        used = set()
        dangerous_ing = list()
        q = deque(sorted(alr_dict.items(), key=lambda e: len(e[1]), reverse=True))
        while q:
            name, lst = q.pop()
            lst = lst - used
            #lst = [l for l in lst if l not in used]
            if len(lst) == 1:
                used.add(list(lst)[0])
                dangerous_ing.append((name, list(lst)[0]))
                continue
            q.appendleft((name, lst))

        return ",".join([v for k, v in sorted(dangerous_ing, key=lambda x: x[0])])
