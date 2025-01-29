from datastructures.bag import Bag

class Card:
    def __init__(self, suit, name):
        self.__suit = suit
        self.__value = name if type(name) == int else 11 if name == "A" else 10
        self.__name = name

    def __str__(self):
        return f"{self.__suit} {self.__name}"

    @property
    def suit(self) -> str:
        return self.__suit

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def name(self):
        return self.__name

class MultiDeck:
    def __init__(self, num):
        self.__deck = Bag()
        if num not in {2,4,6,8}:
            raise ValueError("MultiDeck only supports deck numbers of 2, 4, 6, or 8")
        self.create_deck()
        for num in range(num - 1):
            for card in self.__deck.distinct_items():
                self.__deck.add(card)

    def create_deck(self) -> None:
        for suit in [chr(9829), chr(9830), chr(9827), chr(9824)]:
            for value in ["A", "J", "Q", "K"] + list(range(1,11)):
                self.__deck.add(Card(suit, value))

    @property
    def deck(self):
        return self.__deck
