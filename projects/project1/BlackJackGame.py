from Card import MultiDeck, Card
import random

class Player:
    """
    A player in the game
    """
    def __init__(self, deck: MultiDeck):
        """
        :param deck: The main deck of the game
        """
        self._hand = []
        self.__score = 0
        self.__deck = deck
        for i in range(2):
            self.draw()

    def draw(self) -> None:
        """
        Adds a card to the player's hand
        """
        card = self.__deck.draw()
        self._hand.append(card)
        self.score += card.value
        if (self.score > 21) and ("A" in (hand_str := [i.name for i in self._hand])) and ((ace := self._hand[hand_str.index("A")]).value == 11):
            ace.flip_ace()

    @property
    def hand(self):
        return "".join([f" [{i.name}{i.suit}]" for i in self._hand])

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score


class Dealer(Player):
    """
    The dealer in the game
    """
    def __init__(self, deck: MultiDeck):
        super(Dealer,self).__init__(deck)
        self.__stay_val = 17
        self.__hidden_card = self._hand.pop(0)
        self.score -= self.__hidden_card.value

    def reveal_hidden(self):
        self._hand.append(self.__hidden_card)
        self.score += self.__hidden_card.value

    @property
    def stay_val(self):
        return self.__stay_val

    @property
    def hidden_card(self):
        return self.__hidden_card

class BlackJackGame:
    """
    The main logic for a game of blackjack
    """

    def __init__(self):
        self.__deck = None
        self.__player = None
        self.__dealer = None

    def play(self):
        """
        The game logic.
        """
        print(".------..------..------..------..------..------..------..------..------.\n"
              "|B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |\n"
              "| :(): || :/\\: || (\\/) || :/\\: || :/\\: || :(): || (\\/) || :/\\: || :/\\: |\n"
              "| ()() || (__) || :\\/: || :\\/: || :\\/: || ()() || :\\/: || :\\/: || :\\/: |\n"
              "| '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|\n"
              "`------'`------'`------'`------'`------'`------'`------'`------'`------'\n")
        loop = True
        while loop:
            self.__deck = MultiDeck(random.choice([2, 4, 6, 8]))
            self.__player = Player(self.__deck)
            self.__dealer = Dealer(self.__deck)
            print("Initial Deal:")
            print(f"Player's Hand:{self.__player.hand} | Score: {self.__player.score}")
            print(f"Dealer's Hand:{self.__dealer.hand} [Hidden] | Score: {self.__dealer.score}")
            player_turn, dealer_turn = True, True
            if self.__player.score == 21:
                print("Blackjack! Player wins")
                player_turn, dealer_turn = False, False
            elif self.__dealer.score + self.__dealer.hidden_card.value == 21:
                print("Blackjack! Dealer wins")
                player_turn, dealer_turn = False, False
            print("")
            while player_turn:
                if self.__player.score == 21:
                    print("Blackjack! Player wins")
                    player_turn, dealer_turn = False, False
                elif self.__player.score > 21:
                    print("Bust! You went over 21")
                    player_turn = False
                print(f"Player's Hand:{self.__player.hand} | Score: {self.__player.score}")
                if player_turn:
                    inp = input("Would you like to (H)it or (S)tay?\n>>")
                    print("")
                    match inp.lower():
                        case "h":
                            self.__player.draw()
                        case "s":
                            player_turn = False
                        case _:
                            print("Input not recognized. Press H to hit or S to stay")
                print("")
            self.__dealer.reveal_hidden()
            while dealer_turn:
                if self.__dealer.score == 21:
                    print("Blackjack! Dealer wins")
                    dealer_turn = False
                elif self.__dealer.score > 21:
                    print("Bust! Dealer went over 21")
                print(f"Dealer's Hand:{self.__dealer.hand}| Score: {self.__dealer.score}")
                if self.__dealer.score > self.__dealer.stay_val:
                    dealer_turn = False
                else:
                    self.__dealer.draw()
            loop = False


if __name__ == "__main__":
    pass
