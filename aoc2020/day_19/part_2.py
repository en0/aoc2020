import re
from aoc2020 import *


class Solution(SolutionABC):
    expected = 12
    rules = None

    def get_resource_name(self, name: str) -> str:
        if self.testing and name == "input":
            return "test-input-2"
        return super().get_resource_name(name)

    def solve(self) -> any:
        with self.load_resource("input") as src:
            self.rules = {k: c for k, c in self.read_until(src, lambda x: x == "", self.parse_rule)}
            m = re.compile("^" + self.build_re(0) + "$")
            return sum([m.fullmatch(s) is not None for s in self.read_until(src)])

    def build_re(self, o):
        if o == 8:
            return "(" + self.build_re(42) + ")+"
        elif o == 11:
            r_42 = self.build_re(42)
            r_31 = self.build_re(31)
            return "(" + "|".join([f"({r_42 * i}{r_31 * i})" for i in range(1, 5)]) + ")"
        spec = self.rules[o]
        if isinstance(spec, str):
            return spec
        elif isinstance(spec, tuple):
            return "(" + "|".join(["".join([self.build_re(e) for e in s]) for s in spec]) + ")"

    @classmethod
    def parse_rule(cls, line):
        key, rules = line.split(": ")
        if '"' in rules:
            return int(key), rules.strip('"')
        elif '|' in rules:
            return int(key), tuple([int(_) for _ in x.split(" ")] for x in rules.split(' | '))
        else:
            return int(key), ([int(x) for x in rules.split(' ')],)
