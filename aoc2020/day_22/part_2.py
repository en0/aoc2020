from collections import deque
from itertools import islice
from functools import reduce

from .part_1 import Solution as Part1


class Solution(Part1):
    expected = 291

    def solve(self) -> any:
        p1, p2 = self.load_decks()
        w, s = self.play_game(p1, p2)
        print("Winner:", w)
        return s

    @classmethod
    def play_game(cls, p1_deck: deque, p2_deck: deque):
        previous_states = set()

        # Play game until 1 player has all the cards
        while len(p1_deck) > 0 and len(p2_deck) > 0:

            # Infinity check
            state_hash = cls.hash_state(p1_deck, p2_deck)
            if state_hash in previous_states:
                return "p1", cls.compute_score(p1_deck)
            previous_states.add(state_hash)

            # Start hand: Draw cards
            round_winner, p1_card, p2_card = None, p1_deck.popleft(), p2_deck.popleft()

            # Who won?
            if p1_card <= len(p1_deck) and p2_card <= len(p2_deck):
                round_winner, _ = cls.play_game(
                    cls.clone_slice(p1_deck, p1_card),
                    cls.clone_slice(p2_deck, p2_card))
            else:
                round_winner = "p1" if p1_card > p2_card else "p2"

            # Add cards to winner's deck
            if round_winner == "p1":
                p1_deck.append(p1_card)
                p1_deck.append(p2_card)
            else:
                p2_deck.append(p2_card)
                p2_deck.append(p1_card)

        # Who won the game?
        if len(p1_deck) > 0:
            return "p1", cls.compute_score(p1_deck)
        else:
            return "p2", cls.compute_score(p2_deck)

    @classmethod
    def compute_score(cls, deck):
        return reduce(lambda a, b: a + b, [c * (i + 1) for i, c in enumerate(reversed(deck))], 0)

    @classmethod
    def hash_state(cls, p1_deck, p2_deck):
        return ":".join([",".join(map(str, p1_deck)), ",".join(map(str, p2_deck))])

    @classmethod
    def clone_slice(cls, deck, length):
        return deque(islice(deck, 0, length))
