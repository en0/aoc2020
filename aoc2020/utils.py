from functools import reduce


def coalesce(a, b):
    return b if a is None else a


def math_product(l):
    return reduce(lambda a, b: a * b, l, 1)
