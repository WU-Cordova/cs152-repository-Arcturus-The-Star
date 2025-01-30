from Card import MultiDeck
import random, time

try: # Hopefully a compatibility filter for other operating systems
    import winsound
except ImportError:
    class winsound:
        @staticmethod
        def Beep(frequency, duration):
            pass

        @staticmethod
        def PlaySound(sound, flags):
            pass

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
        winsound.PlaySound("Clair_De_Lune", winsound.SND_ASYNC | winsound.SND_ALIAS | winsound.SND_LOOP)
        for i in [".------..------..------..------..------..------..------..------..------.\n",
              "|B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |\n",
              "| :(): || :/\\: || (\\/) || :/\\: || :/\\: || :(): || (\\/) || :/\\: || :/\\: |\n",
              "| ()() || (__) || :\\/: || :\\/: || :\\/: || ()() || :\\/: || :\\/: || :\\/: |\n",
              "| '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|\n",
              "`------'`------'`------'`------'`------'`------'`------'`------'`------'\n"]:
            print(i, end='')
            time.sleep(.3)
        loop = True
        while loop:
            self.__deck = MultiDeck(random.choice([2, 4, 6, 8]))
            self.__player = Player(self.__deck)
            self.__dealer = Dealer(self.__deck)
            print("Initial Deal:")
            time.sleep(.3)
            print(f"Player's Hand:{self.__player.hand} | Score: {self.__player.score}")
            time.sleep(.3)
            print(f"Dealer's Hand:{self.__dealer.hand} [Hidden] | Score: {self.__dealer.score}")
            time.sleep(.3)
            player_turn, dealer_turn = True, True
            if self.__player.score == 21:
                print("Player has blackjack!")
                time.sleep(.3)
                player_turn, dealer_turn = False, False
            elif self.__dealer.score + self.__dealer.hidden_card.value == 21:
                print("Dealer has blackjack!")
                time.sleep(.3)
                player_turn, dealer_turn = False, False
            print("")
            time.sleep(.3)
            while player_turn:
                print(f"Player's Hand:{self.__player.hand} | Score: {self.__player.score}")
                time.sleep(.3)
                if self.__player.score == 21:
                    print("Player has blackjack!")
                    player_turn, dealer_turn = False, False
                elif self.__player.score > 21:
                    print("Bust! You went over 21")
                    time.sleep(.3)
                    player_turn = False
                if player_turn:
                    match input("Would you like to (H)it or (S)tay?\n>>").lower():
                        case "h" | "hit":
                            self.__player.draw()
                        case "s" | "stay":
                            player_turn = False
                        case _:
                            print("Input not recognized. Press H to hit or S to stay")
                print("")
                time.sleep(.3)
            self.__dealer.reveal_hidden()
            while dealer_turn:
                print(f"Dealer's Hand:{self.__dealer.hand}| Score: {self.__dealer.score}")
                if self.__dealer.score == 21:
                    print("Dealer has blackjack!")
                    dealer_turn = False
                elif self.__dealer.score > 21:
                    print("Bust! Dealer went over 21")
                    dealer_turn = False
                elif self.__dealer.score >= self.__dealer.stay_val:
                    print(">>Dealer stays")
                    dealer_turn = False
                else:
                    print(">>Dealer hits")
                    self.__dealer.draw()
                time.sleep(.3)
            if ((dscore := self.__dealer.score) <= 21) and ((pscore := self.__player.score) <= 21):
                if pscore > dscore:
                    print("Player wins")
                elif pscore < dscore:
                    print("Dealer wins")
                elif pscore == dscore:
                    print("Scores are tied")
            elif self.__dealer.score > 21 and not self.__player.score > 21:
                print("Dealer busted, Player wins")
            elif not self.__dealer.score > 21 and self.__player.score > 21:
                print("Player busted, Dealer wins")
            else:
                print("Tied. Player and Dealer busted")
            time.sleep(.3)
            match input("Would you like to play again? (Y)es or (N)o\n>>").lower():
                case "y" | "yes":
                    pass
                case "n" | "no":
                    loop = False
                case _:
                    print("Input not recognized. Press Y to play again or N to quit")

        winsound.PlaySound(None, winsound.SND_ASYNC)


if __name__ == "__main__":
    pass
