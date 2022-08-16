import unittest

from blackjack.blackjackplayer import BlackjackPlayer
from blackjack.card import Card

class BlackjackPlayerTest(unittest.TestCase):
    def setUp(self):
        self.blackjack_player = BlackjackPlayer()

    def test_blackjack_player_empty_hand(self):
        self.assertEqual(0, len(self.blackjack_player.hand.cards))

    def test_blackjack_player_hit(self):
        self.blackjack_player.hit(Card(1,1))
        self.assertEqual(1, len(self.blackjack_player.hand.cards))

    def test_blackjack_player_bust(self):
        self.blackjack_player.hit(Card(10,1))
        self.assertFalse(self.blackjack_player.bust)
        self.blackjack_player.hit(Card(11,1))
        self.assertFalse(self.blackjack_player.bust)
        self.blackjack_player.hit(Card(2,1))
        self.assertTrue(self.blackjack_player.bust)
