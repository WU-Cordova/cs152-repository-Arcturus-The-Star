import random
from character import Character

class Game:
    """
    Manages the Dice Battle game logic
    """
    def __init__(self, player1: Character, player2: Character):
        """
        Initializes the game with 2 players
        """
        self.__player1 = player1
        self.__player2 = player2

    def attack(self, attacker: Character, defender: Character):
        pass # TODO: Implement die roll 1-6 and apply scaled attack power to the defender

    def start_battle(self):
        """
        Starts a turn based battle between the two players
        """
        pass # TODO: Implement the battle loop where players take turns attacking