import numpy as np
from functools import reduce

from .part_1 import Solution as Part1, orientations


def find_all(c, s):
    for i, _c in enumerate(s):
        if c == _c:
            yield i


class Solution(Part1):
    expected = 273

    @classmethod
    def print_img(cls, img):
        for row in img:
            print("".join(row))

    @classmethod
    def assemble_image(cls, table):
        def remove_border(tile):
            _, m = tile
            return m[1:-1, 1:-1]

        return np.fliplr(np.flip(reduce(
            lambda a, b: np.append(a, b, axis=0),
            [reduce(lambda a, b: np.append(a, b, axis=1), map(remove_border, row)) for row in table]
        )))

    def solve(self) -> any:
        pattern = [
            list(find_all("#", "                  # ")),
            list(find_all("#", "#    ##    ##    ###")),
            list(find_all("#", " #  #  #  #  #  #   ")),
        ]

        all_tiles = self.load_tiles()
        image_table = self.get_image_table(all_tiles)
        img = self.assemble_image(image_table)

        for k, _img in orientations((0, img)):
            count = 0
            for i in range(len(_img) - len(pattern)):
                count += self.count_monsters(_img[i:i+3], pattern)
            if count > 0:
                break

        pixels = 15 * count
        return np.count_nonzero(img == '#') - pixels

    @classmethod
    def count_monsters(cls, lines, pat):
        rt = 0
        lw = len(lines[0])
        pw = max([max(v) for v in pat])
        for i in range(lw - pw):
            found = True
            for j in range(len(pat)):
                for _pat in pat[j]:
                    if lines[j][i:][_pat] != '#':
                        found = False
                        break
            rt += int(found)
        return rt
