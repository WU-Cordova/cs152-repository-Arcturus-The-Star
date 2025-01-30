from datastructures.bag import Bag
import random

class Card:
    """
    A single playing card.
    """
    def __init__(self, suit:str, name:str | int) -> None:
        """
        :param suit: The suit of the card. Hearts, Diamonds, Clubs, or Spades. Unicode Characters.
        :param name: The name of the card. A number or a face card.
        """
        self.__suit = suit
        self.__value = name if type(name) == int else 11 if name == "A" else 10
        self.__name = name

    def __str__(self) -> str:
        return f"{self.__name}{self.__suit}"

    def flip_ace(self) -> None:
        """
        Flips an ace from 1 to 11 or 11 to 1.
        :return: None
        """
        if self.__name == "A":
            self.__value = 11 if self.__value == 1 else 1
        else:
            raise ValueError("Selected card is not Ace")

    @property
    def suit(self) -> str:
        return self.__suit

    @property
    def value(self) -> int:
        return self.__value

    @property
    def name(self):
        return self.__name

class MultiDeck:
    """
    A deck of playing cards consisting of multiple standard decks of cards.
    """
    def __init__(self, num):
        """
        :param num: The number of decks contained in the MultiDeck. Can be 2, 4, 6, or 8.
        """
        self.__deck = Bag()
        if num not in {2,4,6,8}:
            raise ValueError("MultiDeck only supports deck numbers of 2, 4, 6, or 8")
        self.create_deck(num)

    def create_deck(self, num:int) -> None:
        """
        Creates and stores a MultiDeck.
        :param num: The number of standard decks the MultiDeck consists of.
        :return: None
        """
        for suit in [chr(9825), chr(9826), chr(9827), chr(9824)]: # A list of the various suits. Hearts, Diamonds, Clubs, Spades.
            for value in ["A", "J", "Q", "K"] + list(range(1,11)):
                self.__deck.add(Card(suit, value))
        for num in range(num - 1):
            for card in self.__deck.distinct_items():
                self.__deck.add(card)

    def draw(self) ->Card:
        """
        Draws a randomly selected card from the deck, without replacement.
        :return card: A randomly selected card.
        """
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