import random
from collections import deque

from blackjack.card import Card
from blackjack.suit import Suit

class Deck:
    def __init__(self):
        self.cards = deque()

        for suit in Suit:
            for i in range(1, 14):
                self.cards.append(Card(i, suit))

    def shuffle(self):
        random.shuffle(self.cards)
