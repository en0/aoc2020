from aoc2020 import *
from functools import reduce
from typing import List, Tuple
import re


class FieldValidator:
    def __init__(self, name: str, ranges: List[Tuple[int, int]]):
        self._name = name
        self._ranges = ranges

    def is_valid(self, value: int):
        for low, hi in self._ranges:
            if low <= value <= hi:
                return True
        return False

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return self._name


class Ticket:
    def __init__(self, field_values: List[int], validators: List[FieldValidator]):
        self._field_values = field_values
        self._validators = validators
        self._invalid_fields = []

    def validate(self):
        invalid_fields = []
        for val in self._field_values:
            if not any([f.is_valid(val) for f in self._validators]):
                invalid_fields.append(val)
        self._invalid_fields = invalid_fields

    @property
    def is_valid(self):
        return len(self._invalid_fields) == 0

    @property
    def field_values(self):
        return iter(self._field_values)

    @property
    def invalid_field_values(self):
        return iter(self._invalid_fields)


class Solution(SolutionABC):
    expected = 71
    my_ticket: Ticket = None
    nearby_tickets: List[Ticket] = list()
    validators: List[FieldValidator] = list()

    def solve(self) -> any:
        self.load_ticket_data()
        rt = 0
        for ticket in self.nearby_tickets:
            rt += sum(ticket.invalid_field_values)
        return rt

    def solve2(self) -> any:
        """Oh the horror!!"""
        self.load_ticket_data()
        field_map = dict()
        for validator in self.validators:
            field_map[validator] = [True]*len(self.validators)

        for ticket in [t for t in self.nearby_tickets if t.is_valid] + [self.my_ticket]:
            for i, value in enumerate(ticket.field_values):
                for validator, fits in field_map.items():
                    if not validator.is_valid(value):
                        fits[i] = False
        assigned = set()
        field_match_set = {}
        for validator, fits in sorted(field_map.items(), key=lambda v: sum(v[1])):
            for i, state in enumerate(fits):
                if state is False:
                    continue
                elif i in assigned:
                    continue
                assigned.add(i)
                field_match_set[validator.name] = i

        departure_fields = {x[1] for x in filter(lambda x: x[0].startswith("departure"), field_match_set.items())}
        return reduce(lambda a, v: a*v, [v for i, v in enumerate(self.my_ticket.field_values) if i in departure_fields], 1)

    def load_ticket_data(self):
        loader_function = self.load_fields
        for line in self.resource_lines("input"):
            loader_function = loader_function(line)

    def load_fields(self, line):
        if line == "":
            return self.load_ticket
        match = re.fullmatch(r"^([a-z ]*): (\d*)-(\d*) or (\d*)-(\d*)$", line)
        if match is None:
            raise ValueError("Input is not conforming.")
        name, low1, hi1, low2, hi2 = match.groups()
        self.validators.append(FieldValidator(name, [(int(low1), int(hi1)), (int(low2), int(hi2))]))
        return self.load_fields

    def load_ticket(self, line):
        if line == "":
            return self.load_nearby_ticket
        elif line == "your ticket:":
            return self.load_ticket
        self.my_ticket = Ticket([int(i) for i in line.split(",")], self.validators)
        self.my_ticket.validate()
        return self.load_ticket

    def load_nearby_ticket(self, line):
        if line == "" or line == "nearby tickets:":
            return self.load_nearby_ticket
        ticket = Ticket([int(i) for i in line.split(",")], self.validators)
        ticket.validate()
        self.nearby_tickets.append(ticket)
        return self.load_nearby_ticket
