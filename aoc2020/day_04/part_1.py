from aoc2020 import *


class Solution(SolutionABC):
    expected = 2

    def solve(self) -> any:
        ret, buffer = 0, []
        for line in self.resource_lines("input"):
            if line != "":
                [buffer.append(_) for _ in line.split(" ")]
                continue
            elif self.is_valid(buffer):
                ret += 1
            buffer = []

        if buffer and self.is_valid(buffer):
            ret += 1
        return ret

    @classmethod
    def is_valid(cls, buffer):
        required_fields = {
            'byr': False,
            'iyr': False,
            'eyr': False,
            'hgt': False,
            'hcl': False,
            'ecl': False,
            'pid': False,
            'cid': True,
        }

        for field, _ in map(lambda f: f.split(":"), buffer):
            required_fields[field] = True

        return all(required_fields.values())
