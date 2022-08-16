import unittest

from blackjack.card import Card

class CardTest(unittest.TestCase):
    def test_card_ace(self):
        card = Card(1,1)
        self.assertEqual("A", str(card.rank))
        self.assertEqual(11, card.rank.value)

    def test_card_jack(self):
        card = Card(11,1)
        self.assertEqual("J", str(card.rank))
        self.assertEqual(10, card.rank.value)

    def test_card_queen(self):
        card = Card(12,1)
        self.assertEqual("Q", str(card.rank))
        self.assertEqual(10, card.rank.value)

    def test_card_king(self):
        card = Card(13,1)
        self.assertEqual("K", str(card.rank))
        self.assertEqual(10, card.rank.value)

    def test_card_two_to_ten(self):
        for i in range(2, 10):
            card = Card(i,1)
            self.assertEqual(str(i), str(card.rank))
            self.assertEqual(card.rank.value, i)
