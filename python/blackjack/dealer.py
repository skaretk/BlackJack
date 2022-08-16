from blackjack.blackjackplayer import BlackjackPlayer

class Dealer(BlackjackPlayer):
    def __init__(self, card = None):
        super().__init__()
        if card is not None:
            self.hit(card)

    def hit(self, card):
        super().hit(card)
        print(f'Dealer hit with {card}. Total is {self.hand.score}')

    @property
    def allow_hit(self):
        if self.hand.score < 17:
            return True
        return False
