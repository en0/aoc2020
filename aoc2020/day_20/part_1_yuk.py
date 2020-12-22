"""
123    781    567    345    123
8 4 -> 6 2 -> 4 8 -> 2 6 -> 8 4
765    543    321    187    765

765

                123 345 567 781
            781 123 345 567
        567 781 123 345
    345 567 781 123
123 345 567 781
"""
from aoc2020 import *
from aoc2020.utils import math_product
from typing import Optional
from collections import deque

class ImageNode:
    tile_id: int
    _sides: deque
    _rotate_count: int
    top: Optional["ImageNode"]
    right: Optional["ImageNode"]
    bottom: Optional["ImageNode"]
    left: Optional["ImageNode"]

    def __init__(self, tile_id: int, sides: deque):
        self.tile_id = tile_id
        self._sides = sides
        self._rotate_count = 0
        self.top, self.right, self.bottom, self.left = None, None, None, None

    def __repr__(self):
        return f"<{self.tile_id}: T=({self.top.tile_id if self.top else None}), R=({self.right.tile_id if self.right else None}), B=({self.bottom.tile_id if self.bottom else None}), L=({self.left.tile_id if self.left else None}) +{self._rotate_count}>"

    def __len__(self):
        return sum([
            self.top is not None,
            self.right is not None,
            self.bottom is not None,
            self.left is not None,
        ])

    def rotate(self):
        self._rotate_count += 1
        self._sides.rotate()

    def flip(self):
        top, right, bottom, left = self._sides
        self._sides = deque([
            bottom[::-1],
            right[::-1],
            top[::-1],
            left[::-1],
        ])

    def stich(self, other: "ImageNode"):
        if self.top is None and self.top_side == other.bottom_side:
            self.top = other
            other.bottom = self
            return True
        if self.right is None and self.right_side == other.left_side:
            self.right = other
            other.left = self
            return True
        if self.bottom is None and self.bottom_side == other.top_side:
            self.bottom = other
            other.top = self
            return True
        if self.left is None and self.left_side == other.right_side:
            self.left = other
            other.right = self
            return True

    def fit(self, other: "ImageNode"):
        for _ in range(2):
            for _ in range(4):
                if self.top_side == other.bottom_side:
                    self.top = other
                    other.bottom = self
                    return True
                other.rotate()
            for _ in range(4):
                if self.right_side == other.left_side:
                    self.right = other
                    other.left = self
                    return True
                other.rotate()
            for _ in range(4):
                if self.bottom_side == other.top_side:
                    self.bottom = other
                    other.top = self
                    return True
                other.rotate()
            for _ in range(4):
                if self.left_side == other.right_side:
                    self.left = other
                    other.right = self
                    return True
                other.rotate()
            other.flip()
        return False

    @property
    def top_side(self):
        return self._sides[0]

    @property
    def right_side(self):
        return self._sides[1]

    @property
    def bottom_side(self):
        return self._sides[2][::-1]

    @property
    def left_side(self):
        return self._sides[3]


class Solution(SolutionABC):
    expected = 20899048083289

    def solve(self) -> any:
        with self.load_resource("input") as src:
            tiles = {key: sides for key, sides in self.load_tiles(src)}

        list_of_tiles = list(tiles.values())
        q = deque([list_of_tiles[0]])

        while q:
            t = q.pop()
            for _t in list_of_tiles:
                if len(_t) > 0 or t == _t:
                    continue
                if t.fit(_t):
                    q.appendleft(_t)

        for t in list_of_tiles:
            for _t in list_of_tiles:
                if t != _t:
                    t.stich(_t)

        return math_product([t.tile_id for t in list_of_tiles if len(t) == 2])

    def load_tiles(self, src):
        while True:
            tile = self.read_line(src)
            if tile == "":
                return None
            tile = tile[5:-1]
            lside, rside = [], []

            tside = self.read_line(src)
            lside.append(tside[0])
            rside.append(tside[-1])

            for i in range(8):
                row = self.read_line(src)
                lside.insert(0, row[0])
                rside.append(row[-1])

            bside = self.read_line(src)
            lside.insert(0, bside[0])
            rside.append(bside[-1])

            yield int(tile), ImageNode(int(tile), deque([tside, "".join(rside), bside[::-1], "".join(lside)]))
            self.read_line(src)
