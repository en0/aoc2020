from typing import NamedTuple


class Vector(NamedTuple):
    x: int
    y: int

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)

    def quadrant(self):
        if self.x >= 0 and self.y >= 0:
            return 1
        elif self.x < 0 and self.y >= 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x >= 0 and self.y < 0:
            return 4

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise ValueError()

    def __add__(self, other: "Vector"):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise ValueError()

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y)
        elif isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        else:
            raise ValueError()

    def __rmul__(self, other):
        return self.__mul__(other)


NORTH = Vector(0, 1)
EAST = Vector(1, 0)
SOUTH = Vector(0, -1)
WEST = Vector(-1, 0)


def h2s(v):
    return {
        NORTH: "NORTH",
        EAST: "EAST",
        SOUTH: "SOUTH",
        WEST: "WEST",
    }[v]
