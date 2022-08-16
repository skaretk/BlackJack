import unittest

from blackjack.card import Card
from blackjack.hand import Hand

class HandTest(unittest.TestCase):
    def test_hand_empty(self):
        hand = Hand()
        self.assertEqual(len(hand.cards), 0)

    def test_hand_one_ace(self):
        hand = Hand()
        hand.cards.append(Card(1,1))
        self.assertEqual(len(hand.cards), 1)
        self.assertEqual(hand.score, 11)

    def test_hand_two_aces(self):
        hand = Hand()
        hand.cards.append(Card(1,1))
        hand.cards.append(Card(1,2))
        self.assertEqual(len(hand.cards), 2)
        self.assertEqual(hand.score, 12)

    def test_hand_numbers(self):
        hand = Hand()
        for i in range(2, 11):
            hand.cards.append(Card(i,1))

        self.assertEqual(len(hand.cards), 9)
        self.assertEqual(hand.score, 54)
