
class Rank():
    def __init__(self, rank):
        self.rank = rank
        self._value = None
        self.initial_value()

    def __str__(self):
        if self.rank == 1:
            return "A"
        if self.rank == 11:
            return "J"
        if self.rank == 12:
            return "Q"
        if self.rank == 13:
            return "K"
        else:
            return str(self.rank)

    def initial_value(self):
        if self.rank == 1:
            self.value = 11
        elif self.rank > 10:
            self.value = 10
        else:
            self.value = self.rank

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val
