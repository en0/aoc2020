from .part_1 import Solution as Part1
from itertools import product


class Solution(Part1):
    expected = 208

    def get_resource_name(self, name: str) -> str:
        if self.testing and name == "input":
            return "test-input-2"
        else:
            return f"test-{name}" if self.testing else name

    def solve(self) -> any:
        memory = dict()
        mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        for op, val, addr in self.resource_lines("input", self.parse_op):
            if op == "mask":
                mask = val
                continue
            for _addr in self.all_address_generator(mask, bin(addr)[2:].zfill(36)):
                #print(f"mem[{_addr}] = {val}")
                memory[_addr] = val

        return sum(memory.values())

    def all_address_generator(self, mask, base):
        floaters = []
        addr = []
        for m, b in zip(mask, base):
            if m == "0":
                addr.append(b)
            elif m == "1":
                addr.append("1")
            else:
                floaters.append(len(addr))
                addr.append("X")

        for state in product(*["01"]*len(floaters)):
            ret = addr.copy()
            for i, c in zip(floaters, state):
                ret[i] = c
            yield "".join(ret)
