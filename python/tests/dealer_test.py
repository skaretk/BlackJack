import unittest

from blackjack.card import Card
from blackjack.dealer import Dealer

class DealerTest(unittest.TestCase):
    def setUp(self):
        self.dealer = Dealer(Card(10,1))

    def test_dealer_hand_with_card(self):
        self.assertEqual(1, len(self.dealer.hand.cards))

    def test_dealer_allow_hit(self):
        self.assertTrue(self.dealer.allow_hit)
        self.dealer.hit(Card(6,1))
        self.assertTrue(self.dealer.allow_hit)
        self.dealer.hit(Card(2,1))
        self.assertFalse(self.dealer.allow_hit)
