from collections import deque
from functools import reduce
from aoc2020 import *


class Graph:
    def __init__(self):
        self._vertex_map = {}
        self._vertices = []
        self._matrix = []

    def __iter__(self):
        return iter(self._vertices)

    def __contains__(self, item):
        return item in self._vertex_map

    def __len__(self):
        return len(self._vertices)

    def __repr__(self):
        return self.dumps()

    def add_vertex(self, v):
        if v in self:
            return
        vi = len(self)
        self._matrix.append([False] * len(self))
        for row in self._matrix:
            row.append(False)
        self._vertices.append(v)
        self._vertex_map[v] = vi

    def add_edge(self, src, dst):
        if src not in self:
            self.add_vertex(src)
        if dst not in self:
            self.add_vertex(dst)
        svi = self._vertex_map[src]
        dvi = self._vertex_map[dst]
        self._matrix[svi][dvi] = True

    def child_count(self, v):
        return len(list(self.children(v)))

    def parent_count(self, v):
        return len(list(self.parents(v)))

    def children(self, v):
        return map(lambda e: self._vertices[e[0]], filter(lambda e: e[1], enumerate(self._matrix[self._vertex_map[v]])))

    def parents(self, v):
        return map(lambda e: self._vertices[e[0]], filter(lambda e: e[1][self._vertex_map[v]], enumerate(self._matrix)))

    def dumps(self):
        lines = []
        for i, row in enumerate(self._matrix):
            lines.append(", ".join(['1' if _ else '0' for _ in row]))
        return "\n".join(lines)
        #lines = ["    " + " ".join(map(lambda s: str(s).zfill(3), self._vertices))]
        #for i, row in enumerate(self._matrix):
            #lines.append(f"{str(self._vertices[i]).zfill(3)} " + " ".join([' X ' if _ else ' - ' for _ in row]))
        #return "\n".join(lines)

    def count_all_paths(self, start, end):
        count, queue = 0, deque(self.children(start))
        while queue:
            current = queue.pop()
            if current == end:
                count += 1
            elif current > end:
                continue
            for neighbor in self.children(current):
                queue.appendleft(neighbor)
        return count


class Solution(SolutionABC):
    expected = None

    def __init__(self, *args, file="input", **kwargs):
        super().__init__(*args, **kwargs)
        self._file = file

    @classmethod
    def make_graph(cls, a):
        g = Graph()
        for i in range(len(a) - 1):
            for j in range(i + 1, len(a)):
                if a[j] - a[i] > 3:
                    break
                g.add_edge(a[i], a[j])
        return g

    def solve(self) -> any:
        adapters = [0] + sorted(self.resource_lines(self._file, int))
        start, end, count = 0, adapters[-1], 0
        print("[+] Constructing graph...")
        graph = self.make_graph(adapters)
        graph.add_edge(end, end+3)
        end += 3
        print("    COMPLETE")

        print("[+] Searching path...")
        rp = 1
        last = start
        for v in sorted(graph):
            if v == 0:
                continue
            if graph.child_count(v) != 1:
                continue
            c = next(graph.children(v))
            if graph.parent_count(c) != 1:
                continue
            print("[-] FOUND CLUMP: ", last, "->", v)
            count = graph.count_all_paths(last, v)
            rp *= count
            last = v
        print("    COMPLETE")

        return rp
