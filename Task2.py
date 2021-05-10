class Wear:

    def consumption(self):
        pass


class Coat(Wear):
    _size: float

    @property
    def wear_size(self):
        return self._size

    @wear_size.setter
    def wear_size(self, value: float):
        self._size = value

    @property
    def consumption(self):
        return self._size / 6.5 + 0.5


class Suit(Wear):
    _height: float

    @property
    def wear_height(self):
        return self._height

    @wear_height.setter
    def wear_height(self, value: float):
        self._height = value

    @property
    def consumption(self):
        return self._height * 2 + 0.3


coat = Coat()
suit = Suit()

coat.wear_size = 3
suit.wear_height = 120
print(coat.consumption)
print(suit.consumption)
