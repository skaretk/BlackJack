import unittest

from blackjack.card import Card
from blackjack.player import Player

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_player_hit(self):
        self.player.hit(Card(1,1))
        self.assertEqual(11, self.player.hand.score)

    def test_player_bust(self):
        self.player.hit(Card(10,1))
        self.assertFalse(self.player.bust)
        self.player.hit(Card(11,1))
        self.assertFalse(self.player.bust)
        self.player.hit(Card(2,1))
        self.assertTrue(self.player.bust)
