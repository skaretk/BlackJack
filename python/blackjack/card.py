from blackjack.rank import Rank
from blackjack.suit import Suit

class Card:
    def __init__(self, rank, suit):
        self.rank = Rank(rank)
        self.suit = Suit(suit)

    def __str__(self):
        return f'{self.suit.name} {self.rank}'
