from aoc2020 import *
from collections import deque


class Solution(SolutionABC):
    expected = 2

    def solve(self) -> any:
        with self.load_resource("input") as src:
            rules = {k: c for k, c in self.read_until(src, lambda s: s == "", self.parse_rule)}
            return sum([
                rules["0"](rules, s) and len(s) == 0
                for s in self.read_until(src, xfrm=lambda s: deque(s))])

    @classmethod
    def parse_rule(cls, line):

        def match_exactly(d, r):
            return r == d.popleft() if d else False

        def match_seq(xs, d, seq):
            return all([xs[k](xs, d) for k in seq])

        def match_or(xs, d, seq_a, seq_b):
            da = d.copy()
            ra = match_seq(xs, da, seq_a)
            if ra:
                [d.popleft() for _ in range(len(d) - len(da))]
                return True
            return match_seq(xs, d, seq_b)

        key, rules = line.split(": ")
        if "|" in rules:
            _a, _b = rules.split(" | ")
            return key, (lambda xs, d, a=_a.split(' '), b=_b.split(' '): match_or(xs, d, a, b))
        elif '"' in rules:
            return key, (lambda xs, d, a=rules.strip('"'): match_exactly(d, a))
        else:
            return key, (lambda xs, d, a=rules.split(' '): match_seq(xs, d, a))
