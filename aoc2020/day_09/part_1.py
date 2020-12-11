from collections import deque
from aoc2020 import *


class Solution(SolutionABC):
    expected = 127
    buffer = deque(maxlen=25)

    def is_valid(self, val):
        """We could get more elaborate here but it's only 25 elements in the buffer."""
        for i in range(len(self.buffer) - 1):
            for j in range(i+1, len(self.buffer)):
                if self.buffer[i] + self.buffer[j] == val:
                    return True
        return False

    def solve(self) -> any:
        if self.testing:
            self.buffer = deque(maxlen=5)

        for val in self.resource_lines("input", int):
            if len(self.buffer) == self.buffer.maxlen and not self.is_valid(val):
                return val
            self.buffer.appendleft(val)
        raise NoSolutionError()
