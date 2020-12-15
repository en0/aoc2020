from aoc2020 import *
import re


class Solution(SolutionABC):
    expected = 165

    def solve(self) -> any:
        memory = dict()
        mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        for op, val, addr in self.resource_lines("input", self.parse_op):
            if op == "mask":
                mask = val
                continue
            memory[addr] = int("".join([b if m == 'X' else m for m, b in zip(mask, bin(val)[2:].zfill(36))]), 2)
        return sum(memory.values())

    @classmethod
    def parse_op(cls, line: str):
        if line.startswith("mask = "):
            return "mask", line[7:], None
        match = re.fullmatch(r"mem\[(\d*)\] = (\d*)", line)
        if match is None:
            raise ValueError("Input does not conform.")
        addr, arg = match.groups()
        return "mem", int(arg), int(addr)
