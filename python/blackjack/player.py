from blackjack.blackjackplayer import BlackjackPlayer

class Player(BlackjackPlayer):

    def hit(self, card):
        super().hit(card)
        print(f'Hit with {card}. Total is {self.hand.score}')
