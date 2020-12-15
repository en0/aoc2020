from .part_1 import Solution as Part1


class Solution(Part1):
    expected = 436

    def solve(self) -> any:
        """
        I am sure there is a better way to do this. Must revisit this weekend.
        The below takes about 60 seconds on a 5 year old hardware /shrug
        """
        return self.spoken_at(30000000)
