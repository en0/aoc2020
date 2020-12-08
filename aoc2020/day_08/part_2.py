from aoc2020 import *

from .part_1 import Solution as Part1


class Interpreter(Part1):
    """Override part1 program loading to allow for patching"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._resource_lines = []

    def set_program(self, resource_lines):
        self._resource_lines = resource_lines

    def resource_lines(self, name: str, xfrm=None):
        return iter(self._resource_lines)


class Solution(SolutionABC):
    """Going to go for a brute force.

    The program size is not very large: 500. The number of potential edits is around 300.
    This makes less than 100k linear lines of execution to test them all if they all run
    to completion (which they will not).  Brute force should be quite fast.
    """
    expected = 8

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._interpreter = Interpreter(*args, **kwargs)

    def solve(self) -> any:
        for _program in self.possible_programs():
            self._interpreter.set_program(_program)
            ans = self._interpreter.solve()
            if self._interpreter.exit_code == 0:
                return ans
        raise NoSolutionError()

    def possible_programs(self):
        orig_prg = list(self.resource_lines("input", Interpreter.parse_instruction))
        # Only nop instructions with non-zero args might be jumps
        to_jmp = [(line_no, ('jmp', arg)) for line_no, (op, arg) in enumerate(orig_prg) if op == 'nop' and arg != 0]
        to_nop = [(line_no, ('nop', arg)) for line_no, (op, arg) in enumerate(orig_prg) if op == 'jmp']
        for line, instruction in to_jmp + to_nop:
            prg = orig_prg.copy()
            prg[line] = instruction
            yield prg


