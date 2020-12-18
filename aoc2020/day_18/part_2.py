from aoc2020 import *
from collections import deque


class Solution(SolutionABC):
    expected = 693891

    def solve(self) -> any:
        return sum(self.resource_lines("input", self.evaluate))

    @classmethod
    def evaluate(cls, line) -> int:
        stack = deque()
        terms = []
        for i in range(len(line)):
            c = line[i]
            if c == "(":
                stack.append(i + 1)
            elif c == ")":
                j = stack.pop()
                if not stack:
                    terms.append(cls.evaluate(line[j:i]))
            elif not stack and c == '+':
                terms.append(c)
            elif not stack and c == '*':
                terms.append(c)
            elif not stack and c != ' ':
                terms.append(int(c))
        while "+" in terms:
            i = terms.index("+")
            a, b = terms[i-1], terms[i+1]
            terms = terms[:i-1] + [a + b] + terms[i+2:]
        while "*" in terms:
            i = terms.index("*")
            a, b = terms[i-1], terms[i+1]
            terms = terms[:i-1] + [a * b] + terms[i+2:]
        return terms[0]
