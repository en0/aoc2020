from aoc2020 import *
from collections import deque


class Solution(SolutionABC):
    expected = 306

    def solve(self) -> any:
        p1, p2 = self.load_decks()
        count = 0
        while len(p1) != 0 and len(p2) != 0:

            count += 1
            #print(f"ROUND {count}")
            #print("p1", p1)
            #print("p2", p2)
            #print("")

            c1 = p1.popleft()
            c2 = p2.popleft()
            if c1 > c2:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)

        rt = 0
        winner = p1 if len(p1) > 0 else p2

        for i, c in enumerate(reversed(winner)):
            rt += (c * (i + 1))
        return rt

    def load_decks(self):
        with self.load_resource("input") as src:
            p1 = self.load_deck(src)
            p2 = self.load_deck(src)
        return p1, p2

    def load_deck(self, src):
        [_ for _ in self.read_until(src, lambda l: l != "")]
        cards = deque([_ for _ in self.read_until(src, lambda l: l == "", xfrm=lambda x: int(x))])
        return cards


