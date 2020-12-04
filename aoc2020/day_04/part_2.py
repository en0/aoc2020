import re
from .part_1 import Solution as Part1Solution


def between(low, hi, val):
    return low <= int(val) <= hi


def re_validate(pattern, value):
    return re.fullmatch(pattern, value) is not None


def re_validate_groups(pattern, value, check):
    match = re.fullmatch(pattern, value)
    return False if match is None else check(*match.groups())


hgt_validators = {
    'cm': lambda b: between(150, 193, b),
    'in': lambda b: between(59, 76, b),
}

field_validator = {
    'byr': lambda b: between(1920, 2002, b),
    'iyr': lambda b: between(2010, 2020, b),
    'eyr': lambda b: between(2020, 2030, b),
    'hgt': lambda b: re_validate_groups(
        r"(\d*)(cm|in)", b, lambda v, u: hgt_validators.get(u, lambda x: False)(v)),
    'hcl': lambda b: re_validate(r"#[a-f0-9]{6}", b),
    'ecl': lambda b: b in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    'pid': lambda b: re_validate(r"\d{9}", b),
    'cid': lambda b: True,
}


class Solution(Part1Solution):
    expected = 2

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

        for field, val in map(lambda f: f.split(":"), buffer):
            required_fields[field] = field_validator.get(field, lambda x: True)(val)

        return all(required_fields.values())
