from aoc2020 import *

from .part_1 import Solution as Part1


class Solution(SolutionABC):
    expected = 62

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._p1 = Part1(*args, **kwargs)

    def solve(self) -> any:
        target = self._p1.solve()
        message = list(self.resource_lines("input", int))
        message_len = len(message)
        for i in range(message_len):
            low, high, rt = message[i], message[i], message[i]
            for j in range(i + 1, message_len):
                low, high = min(low, message[j]), max(high, message[j])
                rt += message[j]
                if rt == target:
                    return low + high
                elif rt > target:
                    break
        return 0
