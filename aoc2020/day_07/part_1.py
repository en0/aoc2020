from aoc2020 import *

from .rule_parser import parse_rule
from .graph import Graph


class Solution(SolutionABC):
    expected = 4

    def build_graph(self):
        rules = list(self.resource_lines("input", parse_rule))
        graph = Graph([n for n, _ in rules])
        for src, edges in rules:
            for dst, wgt in edges:
                graph.add_edge(src, dst, wgt)
        return graph

    def solve(self) -> any:
        graph = self.build_graph()
        return len(graph.find_ancestors('shiny gold'))
