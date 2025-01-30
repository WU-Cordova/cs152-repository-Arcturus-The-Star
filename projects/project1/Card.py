from datastructures.bag import Bag
import random

class Card:
    def __init__(self, suit, name):
        self.__suit = suit
        self.__value = name if type(name) == int else 11 if name == "A" else 10
        self.__name = name

    def __str__(self):
        return f"{self.__name}{self.__suit}"

    @property
    def suit(self) -> str:
        return self.__suit

    @property
    def value(self) -> int:
        return self.__value

    @property
    def name(self):
        return self.__name

    def flip_ace(self):
        if self.__name == "A":
            self.__value = 11 if self.__value == 1 else 1
        else:
            raise ValueError("Selected card is not Ace")

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

    def draw(self):
        if len(self.__deck) > 0:
            card = random.choice(self.__deck.distinct_items())
            self.__deck.remove(card)
            return card
        else:
            raise IndexError("Deck is empty")

    @property
    def deck(self):
        return self.__deck

if __name__ == "__main__":
    pass