from aoc2020 import *
from aoc2020.utils import math_product
from itertools import chain
import numpy as np


def tborder(tile):
    _, m = tile
    return "".join(m[0])


def bborder(tile):
    _, m = tile
    return "".join(m[-1])


def lborder(tile):
    _, m = tile
    return "".join(m[:,0])


def rborder(tile):
    _, m = tile
    return "".join(m[:,-1])


def orientations(tile):
    k, m = tile
    for _ in range(2):
        for i in range(4):
            yield k, m
            m = np.rot90(m)
        m = np.fliplr(m)


class Solution(SolutionABC):
    expected = 20899048083289

    def solve(self) -> any:
        all_tiles = self.load_tiles()
        image_table = self.get_image_table(all_tiles)
        return math_product([image_table[y][x][0] for x, y in [(0, 0), (0, -1), (-1, 0), (-1, -1)]])

    @classmethod
    def get_image_table(cls, tiles):
        # Find the top most piece.
        search_tile = tiles[0]
        while search_tile is not None:
            t0, search_tile = search_tile, None
            for t in chain(*[orientations(x) for x in tiles if x[0] != t0[0]]):
                if tborder(t0) == bborder(t):
                    search_tile = t
                    break
        search_tile = t0

        # Find the left most piece.
        while search_tile is not None:
            t0, search_tile = search_tile, None
            for t in chain(*[orientations(x) for x in tiles if x[0] != t0[0]]):
                if lborder(t0) == rborder(t):
                    search_tile = t
                    break
        search_tile = t0

        assigned = set([search_tile[0]])

        # Find all the left most pieces.
        img = [[search_tile]]
        while search_tile is not None:
            t0, search_tile = search_tile, None
            for t in chain(*[orientations(x) for x in tiles if x[0] not in assigned]):
                if bborder(t0) == tborder(t):
                    search_tile = t
                    img.append([t])
                    assigned.add(t[0])
                    break

        # Find the rest of each row
        for row in img:
            search_tile = row[0]
            while search_tile is not None:
                t0, search_tile = search_tile, None
                for t in chain(*[orientations(x) for x in tiles if x[0] not in assigned]):
                    if rborder(t0) == lborder(t):
                        search_tile = t
                        row.append(t)
                        assigned.add(t[0])
                        break
        #for r in img:
        #    print(" ".join([str(c) for c, _ in r]))

        return img

    def load_tiles(self):
        with self.load_resource("input") as src:
            return [(k, m) for k, m in self.read_tiles(src)]

    def read_tiles(self, src):
        while True:
            tile_heading = self.read_line(src)
            if tile_heading == "":
                return
            tile_id = int(tile_heading[5:-1])
            matrix = list(self.read_until(src, xfrm=lambda s: list(s)))
            yield tile_id, np.array(matrix)
