from functools import reduce


def coalesce(a, b):
    return b if a is None else a


def math_product(l):
    return reduce(lambda a, b: a * b, l, 1)


def count_all(a, b):
    """Count all occurrence of a in b"""
    return len([1 for w in b if w == a])
