from aoc2020 import *
from .vector import NORTH, EAST, SOUTH, WEST, Vector


class Solution(SolutionABC):
    expected = 25

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._loc, self._heading = Vector(0, 0), EAST
        self.move = lambda op, arg: {
            "L": lambda a: self.rotate(-a//90),
            "R": lambda a: self.rotate(a//90),
            "F": lambda a: self.set_loc(a * self._heading + self._loc),
            "N": lambda a: self.set_loc(a * NORTH + self._loc),
            "E": lambda a: self.set_loc(a * EAST + self._loc),
            "S": lambda a: self.set_loc(a * SOUTH + self._loc),
            "W": lambda a: self.set_loc(a * WEST + self._loc),
        }.get(op, lambda a: a)(arg)

    def set_loc(self, loc: Vector):
        self._loc = loc

    def rotate(self, count):
        if count < 0:
            self._heading = self._rotate_left(self._heading, -count)
        else:
            self._heading = self._rotate_right(self._heading, count)

    def _rotate_right(self, whence, count):
        if count == 0:
            return whence
        return self._rotate_right({
            NORTH: EAST,
            EAST: SOUTH,
            SOUTH: WEST,
            WEST: NORTH,
        }[whence], count - 1)

    def _rotate_left(self, whence, count):
        if count == 0:
            return whence
        return self._rotate_left({
            NORTH: WEST,
            WEST: SOUTH,
            SOUTH: EAST,
            EAST: NORTH,
        }[whence], count - 1)

    def solve(self) -> any:
        for op, arg in self.resource_lines("input", lambda x: (x[0], int(x[1:]))):
            self.move(op, arg)
        return self._loc.manhattan_distance()
