from aoc2020 import *
from functools import reduce


class Congruence:
    def __init__(self, modulo, remainder, scalar=1):
        self._mod = modulo
        # Simplify the congruence
        self._rem = remainder % modulo
        self._scalar = scalar

    @property
    def modulo(self):
        return self._mod

    @property
    def remainder(self):
        return self._rem

    @property
    def scalar(self):
        return self._scalar

    def solve(self):
        x = self.scalar % self.modulo
        for i in range(self.modulo):
            if x * i % self._mod == self.remainder:
                return i
        raise ValueError(f"Unable to find congruence for {self}")

    def check(self, j: int) -> bool:
        return self.scalar * j % self.modulo == self.remainder

    def __repr__(self):
        if self._scalar > 1:
            return f"{self._scalar}𝑥≡ {self._rem} (mod {self._mod})"
        else:
            return f"𝑥≡ {self._rem} (mod {self._mod})"


class Solution(SolutionABC):
    """
    After a LOT of brain scratching and hopeless attempts to brute force, I started googling around.
    I found out about this theorem. https://brilliant.org/wiki/chinese-remainder-theorem/
    It took me couple days to wrap my head around the concept but here is my solution.

    Things i found useful:
    - https://www.youtube.com/watch?v=EolotL9HN8k
    - https://www.math.nyu.edu/faculty/hausner/congruence.pdf
    """
    expected = 1068781

    def load_congruence(self):
        _, bids = list(self.resource_lines("input"))
        bids = bids.split(",")
        filtered = filter(lambda s: s[1] != 'x', enumerate(bids))
        return list(map(lambda s: Congruence(int(s[1]), int(s[1]) - s[0]), filtered)), len(bids)

    def solve(self) -> any:
        # Find a solution for the given system of linear congruences
        # I assume all moduli are co-prime
        #
        # Suppose that n1, n2, ..., ni ∈ ℕ
        #     and gdc(ni, nj) = 1
        #     and b1, b2, ..., bi ∈ ℤ
        # Than the system, 𝑥 ≡ b1 (mod n1), 𝑥 ≡ b2 (mod n2), ..., 𝑥 ≡ bi (mod ni)
        # has a unique solution modulo ∏ ni

        system, bus_count = self.load_congruence()

        print("System of congruence")
        print("--------------------------------------------")
        print("\n".join([str(_) for _ in system]))
        print("--------------------------------------------")

        # let N = ∏ ni
        N = reduce(lambda a, b: b.modulo * a, system, 1)

        # Let Ni = N/ni ⟹ gcd(ni,Ni) = 1
        Ni = [N // c.modulo for c in system]

        # Let bi be the remainder for each congruence in the system of congruence
        bi = [c.remainder for c in system]

        # Let xi be an integer such that Ni•xi ≡ 1 (mod ni)
        xi = [Congruence(c.modulo, 1, Ni[i]).solve() for i, c in enumerate(system)]

        # Let biNixi = ∑ bi•Ni•xi
        biNixi = [bi[i] * Ni[i] * xi[i] for i in range(len(system))]

        # Let congruence be the unique congruence in module biNixi
        congruence = Congruence(N, sum(biNixi))

        print(congruence)

        ans = congruence.remainder

        for c in system:
            if not c.check(ans):
                raise NoSolutionError("Wrong answer my friend.")

        return ans

