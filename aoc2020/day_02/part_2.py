from .part_1 import Solution as Part1Solution


class Solution(Part1Solution):

    expected = 1

    @classmethod
    def check_pw(cls, line: str):
        policy, pw = line.split(': ', 2)
        pos, letter = policy.split(' ')
        pos1, pos2 = pos.split('-')
        return sum([
            pw[int(pos1)-1] == letter,
            pw[int(pos2)-1] == letter,
        ]) == 1

