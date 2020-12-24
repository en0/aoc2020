from aoc2020 import *


class Solution(SolutionABC):
    expected = "67384529"

    def solve(self) -> any:
        cups = next(self.resource_lines("input", lambda l: [int(i) for i in l]))
        max_cup_value = max(cups)
        round = 0
        for _ in range(100):
            round += 1
            print(round, cups)
            the_three, cups = self.take_3(cups)
            print("pickup", the_three)
            cd = cups[0] - 1
            while cd not in cups:
                cd = cd - 1 if cd > 0 else max_cup_value
            print("dest", cd, cups.index(cd), cups)
            cups = self.put_3(cups, the_three, cups.index(cd))
            cups = self.rotate(cups)
            print("")

        print("final", cups)
        while cups[0] != 1:
            cups = self.rotate(cups)
        return "".join(map(str, cups[1:]))

    @classmethod
    def rotate(cls, cups):
        c = cups[0]
        return cups[1:] + [c]

    @classmethod
    def take_3(cls, cups):
        return cups[1:4], cups[0:1] + cups[4:]

    @classmethod
    def put_3(cls, cups, the_three, i):
        return cups[:i+1] + the_three + cups[i+1:]
