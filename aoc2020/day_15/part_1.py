from aoc2020 import *
from collections import deque
from typing import Dict, Deque


class Solution(SolutionABC):
    expected = 436
    spoken_map: Dict[int, Deque[int]] = {}
    last_spoken: int = None
    spoken_len: int = 0

    def solve(self) -> any:
        return self.spoken_at(2020)

    def spoken_at(self, t):
        self.spoken_len = len([self.speak(_) for _ in self.resource_lines("input", int)])
        while self.spoken_len < t:
            self.turn()
        return self.last_spoken

    def turn(self):
        indices = self.spoken_map[self.last_spoken]
        if len(indices) > 1:
            self.speak(indices[-1] - indices[-2])
        else:
            self.speak(0)

    def speak(self, val):
        self.spoken_len += 1
        self.last_spoken = val
        self.spoken_map.setdefault(val, deque(maxlen=2)).append(self.spoken_len)
