from aoc2020 import *


class Solution(SolutionABC):
    expected, exit_code, pc, ax = 5, 0, 0, 0
    program: list = None
    trace: set = None

    def solve(self) -> any:
        self.load_program()
        while self.pc < len(self.program):
            if self.pc in self.trace:
                self.exit_code = 1
                break
            self.trace.add(self.pc)
            self.execute(*self.program[self.pc])
            self.pc += 1
        return self.ax

    def exec_nop(self, arg):
        pass

    def exec_jmp(self, arg):
        self.pc += (arg - 1)

    def exec_acc(self, arg):
        self.ax += arg

    def execute(self, op: str, arg: int):
        return {
            'nop': self.exec_nop,
            'jmp': self.exec_jmp,
            'acc': self.exec_acc,
        }[op](arg)

    def load_program(self):
        self.pc = 0
        self.ax = 0
        self.exit_code = 0
        self.trace = set()
        self.program = list(self.resource_lines("input", self.parse_instruction))

    @classmethod
    def parse_instruction(cls, line: str):
        op, arg = line.split(' ')
        return op, int(arg)
