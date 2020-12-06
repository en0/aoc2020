from .part_1 import Solution as Part1


class Solution(Part1):
    expected = 6
    count = lambda s, f, l: len(list(filter(f, l)))

    def solve(self) -> any:
        grp_size, rt, yes_answers = 0, 0, [0] * 26
        for line in self.resource_lines("input"):
            if line == "":
                rt += self.count(lambda x: x == grp_size, yes_answers)
                grp_size, yes_answers = 0, [0] * 26
            else:
                grp_size += 1
                for c in line:
                    yes_answers[self.c2i(c)] += 1
        return rt + self.count(lambda x: x == grp_size, yes_answers)
