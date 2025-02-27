from Cell import Cell
from Grid import Grid
from random import getrandbits
import os, time, copy
from kbhit import KBHit

class GameController:
    def __init__(self):
        self.__grid = None
        self.__previous_grids:list[Grid] = []
        self.__storage_count:int = 5
        self.__sim_speed:int = 1
        self.__manual_mode:bool = False

    def start(self):
        print("Welcome to the Game of Life.")
        while board_state:= input("To begin, press l to load a file, or r to generate a random board.\n>") + " ":
            match board_state.lower().strip():
                case "l":
                    print("Load chosen.\nPlease enter the name of the configuration file.")
                    files = [f[:f.find(".")].upper() for f in os.listdir("GOL_Configs") if os.path.isfile(os.path.join("GOL_Configs", f))]
                    [print("  - " + line) for line in files]
                    while filename := input("> ") + " ":
                        if filename.rstrip().upper() in files:
                            board = self.read_config(filename.rstrip())
                            break
                        else:
                            print("Not a valid configuration file.")
                    break
                case "r":
                    print("Random chosen.\nPlease input your dimensions:")
                    while rows := input("Rows:\n>") + " ":
                        try:
                            int(rows)
                            break
                        except ValueError:
                            print("Rows should be an integer")
                    while cols := input("Columns:\n>") + " ":
                        try:
                            int(cols)
                            break
                        except ValueError:
                            print("Cols should be an integer")
                    board = self.random_config(int(rows), int(cols))
                    break
                case _:
                    print("Input not recognized, please try again")
        self.__grid = Grid(board)
        print(f"Board loaded.\nNote: \u25A0 denotes a living cell and \u25A1 denotes a dead one\n{self.__grid}")
        input("Controls:\nPress 'Q' to quit\nPress 'M' to activate manual mode\nPress 'S' to step manual mode forward\nPress 'A' to return to automatic mode\nPress 'Enter' to begin the simulation\n")
        kb = KBHit()
        turn = 0
        repeat = False
        death = False
        while not death and not repeat:
            self.__grid.count_living()
            print(f"Turn: {turn}\n{self.__grid}")
            turn += 1
            self.__grid.update_all_neighbors()
            self.__grid.predict_all_cells()
            next_grid = copy.deepcopy(self.__grid)
            next_grid.update_all_cells()
            repeat = self.check_repeat()
            self.add_to_prev()
            self.__grid = next_grid
            if self.__grid.living_cells <= 0:
                print("All the cells died...")
                death = True
            if kb.kbhit():
                c = kb.getch()
                match c.upper():
                    case "Q":
                        quit()
                    case "M":
                        print("Manual Mode, press 'S' to step and 'A' to return to automatic")
                        self.__manual_mode = True
            if self.__manual_mode:
                while True:
                    if kb.kbhit():
                        c = kb.getch()
                        match c.upper():
                            case "Q":
                                quit()
                            case "A":
                                print("Automatic Mode")
                                self.__manual_mode = False
                                break
                            case "S":
                                break
            else:
                time.sleep(self.__sim_speed)


    @staticmethod
    def read_config(config) ->list[list[bool]]:
        with open("GOL_Configs/" + config + ".txt") as f:
            rows = int(f.readline().strip().split(":")[1])
            cols = int(f.readline().strip().split(":")[1])
            f.readline()
            symbol_list = []
            while line:= f.readline().strip().upper():
                symbol_list.append([i for i in line])
        output = []
        for line in symbol_list:
            line_output = []
            for symbol in line:
                match symbol:
                    case "X":
                        line_output.append(True)
                    case "O":
                        line_output.append(False)
                    case _:
                        raise ValueError("Invalid configuration file")
            output.append(line_output)
        return output

    @staticmethod
    def random_config(rows, cols) ->list[list[bool]]:
        return [[bool(getrandbits(1)) for _ in range(cols)] for _ in range(rows)]

    def add_to_prev(self):
        if len(self.__previous_grids) >= self.__storage_count:
            del self.__previous_grids[0]
            self.__previous_grids.append(self.__grid)
        else:
            self.__previous_grids.append(self.__grid)

    def check_repeat(self) ->bool:
        if self.__grid in self.__previous_grids:
            while inp := input("Repeat detected, would you like to quit? (Y/N)\n>"):
                match inp.rstrip().upper():
                    case "Y":
                        return True
                    case "N":
                        return False
                    case _:
                        print("Invalid input")
        else:
            return False