from blackjack.hand import Hand

class BlackjackPlayer:
    def __init__(self):
        self.hand = Hand()

    def hit(self, card):
        self.hand.cards.append(card)

    @property
    def bust(self):
        if self.hand.score > 21:
            return True
        return False
