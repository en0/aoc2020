from aoc2020 import *
from .vector import NORTH, EAST, SOUTH, WEST, Vector


ROTATE_LEFT = Vector(-1, 1)
ROTATE_RIGHT = Vector(1, -1)


class Solution(SolutionABC):
    expected = 286

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._waypoint = (10 * EAST) + (1 * NORTH)
        self._boat = Vector(0, 0)
        self.move = lambda op, arg: {
            "L": lambda a: self.rotate(ROTATE_LEFT, a//90),
            "R": lambda a: self.rotate(ROTATE_RIGHT, a//90),
            "F": lambda a: self.set_boat(a * self._waypoint + self._boat),
            "N": lambda a: self.set_waypoint(a * NORTH + self._waypoint),
            "E": lambda a: self.set_waypoint(a * EAST + self._waypoint),
            "S": lambda a: self.set_waypoint(a * SOUTH + self._waypoint),
            "W": lambda a: self.set_waypoint(a * WEST + self._waypoint),
        }.get(op, lambda a: a)(arg)

    def set_waypoint(self, wp: Vector):
        self._waypoint = wp

    def set_boat(self, boat: Vector):
        self._boat = boat

    def rotate(self, direction, count):
        self._waypoint = self._rotate(self._waypoint, direction, abs(count))

    def _rotate(self, whence, direction, count):
        if count == 0:
            return whence
        return self._rotate(direction * Vector(whence.y, whence.x), direction, count - 1)

    def solve(self) -> any:
        for op, arg in self.resource_lines("input", lambda x: (x[0], int(x[1:]))):
            self.move(op, arg)
        return self._boat.manhattan_distance()
