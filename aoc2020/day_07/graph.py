from typing import List
from collections import deque


class Graph:
    def __init__(self, vertices: List[str]):
        self._size = len(vertices)
        self._vertex_map = {n: i for i, n in enumerate(vertices)}
        self._vertices = vertices
        self._matrix = [[None] * self._size for _ in range(self._size)]

        # because im lazy
        self._find_ancestors = lambda vi: filter(lambda e: e[1] is not None, map(lambda _vi: (_vi, self._matrix[_vi][vi]), range(self._size)))
        self._children = lambda vi: [(_vi, wgt) for _vi, wgt in enumerate(self._matrix[vi]) if wgt is not None]
        self._value_of = lambda vi: sum([wgt + (wgt * self._value_of(_vi)) for _vi, wgt in self._children(vi)])

    def add_edge(self, src: str, dst: str, wgt: int):
        s_vi = self._vertex_map[src]
        d_vi = self._vertex_map[dst]
        self._matrix[s_vi][d_vi] = wgt

    def find_ancestors(self, vertex: str) -> List[str]:
        """part 1"""
        visited = set()
        queue = deque()
        vi = self._vertex_map[vertex]
        [queue.appendleft(n) for n, _ in self._find_ancestors(vi)]
        while queue:
            vi = queue.pop()
            if vi not in visited:
                visited.add(vi)
                [queue.appendleft(_vi) for _vi, _ in self._find_ancestors(vi)]
        return [self._vertices[_vi] for _vi in visited]

    def value_of(self, vertex: str) -> int:
        """part 2"""
        vi = self._vertex_map[vertex]
        return self._value_of(vi)
