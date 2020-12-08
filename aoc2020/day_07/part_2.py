from .part_1 import Solution as Part1


class Solution(Part1):
    expected = 32

    def solve(self) -> any:
        graph = self.build_graph()
        return graph.value_of('shiny gold')
