from aoc2020 import *


class Solution(SolutionABC):
    expected = 295

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.calc_departure = lambda a, b: a // b * b + b
        self.load_schedules = lambda r: self.expand_schedules(*list(self.resource_lines(r)))
        self.expand_schedules = lambda avail, bids: sorted(map(lambda b: (
            self.calc_departure(int(avail), int(b)),
            int(avail),
            int(b),
        ), filter(lambda b: b != "x", bids.split(","))), key=lambda s: s[0])

    def solve(self) -> any:
        return next(map(lambda e: (e[0] - e[1]) * e[2], self.load_schedules("input")))
