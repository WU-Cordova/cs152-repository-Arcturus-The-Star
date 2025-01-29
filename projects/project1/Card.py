from datastructures.bag import Bag

class Card:
    def __init__(self, suit, value):
        self.__suit = suit
        self.__value = value

    @property
    def suit(self) -> str:
        return self.__suit

    @property
    def value(self) -> int:
        return self.__value

class MultiDeck:
    def __init__(self, num):
        self.__deck = Bag()
        if num not in [2,4,6,8]:
            raise ValueError("MultiDeck only supports deck numbers of 2, 4, 6, or 8")
        self.create_deck()
        for num in range(num - 1):
            for card in self.__deck.distinct_items():
                self.__deck.add(card)

    def create_deck(self) -> None:
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for value in ["Ace", "Jack", "Queen", "King"] + list(range(1,11)):
                self.__deck.add(Card(suit, value))

    @property
    def deck(self):
        return self.__deck