class Cell:
    def __init__(self, coords:tuple, status:bool = False):
        """
        A single cell of the game of life
        :param coords: The coordinates of the cell, in (Row, Column) form
        :param status: True if the cell is living, False if it is dead. Defaults to False
        """
        if not isinstance(status, bool):
            raise TypeError("Status should be a boolean")
        self.__neighbors:int = 0 # Live neighbors
        self.__will_be_alive:bool = status
        self.__living:bool = status
        self.__coordinates:tuple = coords

    @property
    def coordinates(self) -> tuple:
        return self.__coordinates

    @property
    def living(self) ->bool:
        return self.__living

    @property
    def will_be_alive(self) ->bool:
        return self.__will_be_alive

    @property
    def neighbors(self) ->int:
        return self.__neighbors

    @neighbors.setter
    def neighbors(self, neighbors) ->None:
        self.__neighbors = neighbors

    def prospective_life(self):
        """
        Uses the cell's number of living neighbors to calculate if it will be alive in the next round and updates the __will_be_alive attribute.
        """
        if self.__neighbors == 2:
            self.__will_be_alive = self.__living
        elif self.__neighbors == 3:
            self.__will_be_alive = True
        else:
            self.__will_be_alive = False

    def update_life(self):
        """
        Changes the cell's current living status to its prospective status.
        """
        self.__living = self.__will_be_alive

    def __str__(self):
        if self.living:
            return "\u25A0"
        else:
            return "\u25A1"

    def __repr__(self):
        return f"{"Living" if self.living else "Dead"} Cell at Row:{self.coordinates[0]}, Column:{self.coordinates[1]} with {self.neighbors} neighbors, predicted to be {"Living" if self.__will_be_alive else "Dead"}"

    def __eq__(self, other):
        return self.living == other.living