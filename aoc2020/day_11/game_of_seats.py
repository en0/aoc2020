import itertools
from abc import ABC, abstractmethod
from typing import List, Tuple


class GOSBehavior(ABC):
    @abstractmethod
    def get_seat_state(self, i: int, j: int, gos: "GOS"):
        pass


class GOS:
    def __init__(self, behavior: GOSBehavior, grid: List[List[str]]):
        self.behavior = behavior
        self._size = len(grid), len(grid[0])
        self._grid = grid.copy()

    def __repr__(self):
        return "\n".join(["".join(r) for r in self._grid])

    def tick(self):
        i_limit, j_limit = self._size
        _back_buffer, change_count = [r.copy() for r in self._grid], 0
        for i, j in itertools.product(range(i_limit), range(j_limit)):
            new_state = self.behavior.get_seat_state(i, j, self)
            if new_state != self.get_state(i, j):
                _back_buffer[i][j] = new_state
                change_count += 1
        self._grid = _back_buffer
        return change_count

    def get_state(self, i, j):
        return self._grid[i][j]

    def is_occupied(self, i, j) -> bool:
        i_limit, j_limit = self._size
        if 0 <= i < i_limit and 0 <= j < j_limit:
            return self._grid[i][j] == "#"
        else:
            return False

    def is_ray_occupied(self, i, j, delta_i, delta_j):
        i_limit, j_limit = self._size
        while True:
            i += delta_i
            j += delta_j
            if not (0 <= i < i_limit and 0 <= j < j_limit):
                return False
            state = self.get_state(i, j)
            if state == "L":
                return False
            elif state == "#":
                return True

    def count_occupied(self):
        i_limit, j_limit = self._size
        rt = 0
        for i in range(i_limit):
            for j in range(j_limit):
                if self.is_occupied(i, j):
                    rt += 1
        return rt


