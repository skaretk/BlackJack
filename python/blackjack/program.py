from blackjack.dealer import Dealer
from blackjack.deck import Deck
from blackjack.player import Player

def main():

    deck = Deck()
    deck.shuffle()
    card = deck.cards.pop()
    dealer = Dealer(card)
    player = Player()

    while True:
        read = input('Stand, Hit:\n')
        if read.lower() == 'Hit'.lower():
            card = deck.cards.pop()
            player.hit(card)

            if player.bust:
                print(f'You Lost! You Busted! You ({player.hand.score}) Dealer ({dealer.hand.score})')
                break

        elif read.lower() == 'Stand'.lower():
            if not dealer.bust and not player.bust:
                while dealer.hand <= player.hand and dealer.allow_hit:
                    card = deck.cards.pop()
                    dealer.hit(card)

                if dealer.bust:
                    print(f'You Won! Dealer busted! You ({player.hand.score}) Dealer ({dealer.hand.score})')
                elif player.hand == dealer.hand:
                    print(f'Tie! You ({player.hand.score}) Dealer ({dealer.hand.score})')
                elif player.hand < dealer.hand:
                    print(f'Dealer Won! You ({player.hand.score}) Dealer ({dealer.hand.score})')
                else:
                    print(f'You Won! You ({player.hand.score}) Dealer ({dealer.hand.score})')
            break

if __name__ == '__main__':
    main()
