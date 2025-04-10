import random, time
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
        self.__player_list = [self.__player1, self.__player2]

    def attack(self, attacker: Character, defender: Character):
        """
        Performs an attack where the attacker rolls a die to determine damage dealt
        """
        defender.health -= (damage := ((roll := random.randint(1,6)) * attacker.attack_power))
        print(f"{attacker.name} attacked {defender.name} with a roll of {roll}. {defender.name} took {damage} damage")
        time.sleep(.3)
        print(f"{defender.name} has {max(0, defender.health)} health remaining")

    def check_win(self):
        if self.__player1.health < 0:
            time.sleep(.3)
            print(f"{self.__player2.name} has won!")
            return True
        elif self.__player2.health < 0:
            time.sleep(.3)
            print(f"{self.__player1.name} has won!")
            return True
        else:
            return False

    def start_battle(self):
        """
        Starts a turn based battle between the two players
        """
        in_battle = True
        starter = random.randint(0,1)
        while in_battle:
            self.attack(self.__player_list[starter], self.__player_list[1 - starter])
            if win := self.check_win():
                in_battle = not win
                break
            time.sleep(.3)
            self.attack(self.__player_list[1 - starter], self.__player_list[starter])
            if win := self.check_win():
                in_battle = not win
                break
            time.sleep(.3)
