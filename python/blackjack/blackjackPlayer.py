from blackjack.hand import Hand

class BlackjackPlayer:
    def __init__(self):
        self.hand = Hand()

    def hit(self, card):
        self.hand.cards.append(card)

    @property
    def bust(self):
        return self.hand.score > 21
