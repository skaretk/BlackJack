import unittest

from blackjack.suit import Suit

class SuitTest(unittest.TestCase):
    def test_suit_hearts(self):
        suit = Suit(1)
        self.assertEqual(Suit.Hearts.name, suit.name)

    def test_suit_diamonds(self):
        suit = Suit(2)
        self.assertEqual(Suit.Diamonds.name, suit.name)

    def test_suit_spades(self):
        suit = Suit(3)
        self.assertEqual(Suit.Spades.name, suit.name)

    def test_suit_clubs(self):
        suit = Suit(4)
        self.assertEqual(Suit.Clubs.name, suit.name)
