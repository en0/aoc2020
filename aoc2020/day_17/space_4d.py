from itertools import product
from math import inf


class Space4d:
    def __init__(self, initial_state):
        self._space = {p: s for p, s in initial_state}
        xi, yi, zi, wi = inf, inf, inf, inf
        xa, ya, za, wa = -inf, -inf, -inf, -inf
        for x, y, z, w in self._space.keys():
            xi, yi, zi, wi = min(xi, x), min(yi, y), min(zi, z), min(wi, w)
            xa, ya, za, wa = max(xa, x), max(ya, y), max(za, z), max(wa, w)
        self._min, self._max = (xi, yi, zi, wi), (xa, ya, za, wa)

    def __iter__(self):
        x_min, y_min, z_min, w_min = self._min
        x_max, y_max, z_max, w_max = self._max
        return map(lambda p: (p, self._space.get(p, False), self._active_around(p)), product(
            range(x_min - 1, x_max + 2),
            range(y_min - 1, y_max + 2),
            range(z_min - 1, z_max + 2),
            range(w_min - 1, w_max + 2),
        ))

    def simulate(self):
        back, rt = self._space.copy(), 0
        for p, s, a in self:
            back[p] = 2 <= a <= 3 if s else a == 3
            rt += back[p]
        self._min = tuple(v - 1 for v in self._min)
        self._max = tuple(v + 1 for v in self._max)
        self._space = back
        return rt

    def _active_around(self, point):
        x, y, z, w = point
        return sum((
            self._space.get(p, False)
            for p in product([x+1, x-1, x], [y+1, y-1, y], [z+1, z-1, z], [w+1, w-1, w])
            if p != point))
