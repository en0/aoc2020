from aoc2020 import *

from .game_of_seats import GOS, GOSBehavior
from .part_1 import Solution as Part1


class AdvancedGOSBehavior(GOSBehavior):
    """
    If a seat is empty (L) and there are no occupied seats in a ray in the 8 directions, the seat becomes occupied.
    If a seat is occupied (#) and five or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.
    """

    def get_seat_state(self, i: int, j: int, gos: GOS):
        current = gos.get_state(i, j)
        if current == ".":
            return current
        occupied_count = self.occupied_count_near(i, j, gos)
        if current == "L" and occupied_count == 0:
            return "#"
        elif current == "#" and occupied_count >= 5:
            return "L"
        return current

    @classmethod
    def occupied_count_near(cls, i, j, gos: GOS) -> int:
        return sum([
            gos.is_ray_occupied(i, j, -1, -1),    # up, left
            gos.is_ray_occupied(i, j, -1, 0),     # up
            gos.is_ray_occupied(i, j, -1, 1),     # up, right

            gos.is_ray_occupied(i, j, 0, -1),     # left
            gos.is_ray_occupied(i, j, 0, 1),      # right

            gos.is_ray_occupied(i, j, 1, -1),     # down, left
            gos.is_ray_occupied(i, j, 1, 0),      # down
            gos.is_ray_occupied(i, j, 1, 1),      # down, right
        ])


class Solution(Part1):
    expected = 26

    def build_gos(self):
        behavior = AdvancedGOSBehavior()
        init_state = list(self.resource_lines("input", lambda x: list(x)))
        return GOS(behavior, init_state)
