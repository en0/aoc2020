from aoc2020 import *

from .game_of_seats import GOS, GOSBehavior


class BasicGOSBehavior(GOSBehavior):
    """
    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.
    """

    def get_seat_state(self, i: int, j: int, gos: GOS):
        current = gos.get_state(i, j)
        if current == ".":
            return current
        occupied_count = self.occupied_count_near(i, j, gos)
        if current == "L" and occupied_count == 0:
            return "#"
        elif current == "#" and occupied_count >= 4:
            return "L"
        return current

    @classmethod
    def occupied_count_near(cls, i, j, gos: GOS) -> int:
        return sum([
            gos.is_occupied(i-1, j-1),
            gos.is_occupied(i-1, j),
            gos.is_occupied(i-1, j+1),

            gos.is_occupied(i, j-1),
            gos.is_occupied(i, j+1),

            gos.is_occupied(i+1, j-1),
            gos.is_occupied(i+1, j),
            gos.is_occupied(i+1, j+1),
        ])


class Solution(SolutionABC):
    expected = 37

    def build_gos(self):
        behavior = BasicGOSBehavior()
        init_state = list(self.resource_lines("input", lambda x: list(x)))
        return GOS(behavior, init_state)

    def solve(self) -> any:
        g = self.build_gos()
        while g.tick() > 0: ...
        return g.count_occupied()
