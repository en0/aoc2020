from aoc2020 import *
from collections import deque


class Solution(SolutionABC):
    expected = 26 + 437 + 12240 + 13632

    def solve(self) -> any:
        return sum(self.resource_lines("input", self.evaluate))

    @classmethod
    def evaluate(cls, line) -> int:
        stack = deque()
        terms = deque()
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
        op = lambda a, b: a + b
        ret = int(terms.popleft())
        for term in terms:
            if term == '+':
                op = lambda a, b: a + b
            elif term == "*":
                op = lambda a, b: a * b
            else:
                ret = op(ret, term)
        return ret
