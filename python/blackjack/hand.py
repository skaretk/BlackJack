
class Hand():
    def __init__(self):
        self.cards = []

    def __eq__(self, other):
        return self.score == other.score

    def __gt__(self, other):
        return self.score > other.score

    def __lt__(self, other):
        return self.score < other.score

    def __le__(self, other):
        return self.score <= other.score

    def __ge__(self, other):
        return self.score >= other.score

    @property
    def score(self):
        total = 0
        contain_ace = False
        for card in self.cards:
            if str(card.rank) == "A":
                contain_ace = True
            total += card.rank.value
        if total > 21 and contain_ace:
            total = self.convert_aces(total)
        return total

    def convert_aces(self, total):
        for card in self.cards:
            if str(card.rank) == "A":
                card.rank.value = 1
                total -= 10
                if total <= 21:
                    break
            total += card.rank.value
        return total
