class Cell:
    def __init__(self, status:bool):
        if not isinstance(status, bool):
            raise TypeError("Status should be a boolean")
        self.__neighbors:int = 0 # Live neighbors
        self.__will_be_alive:bool = False
        self.__living:bool = status

    @property
    def living(self) ->bool:
        return self.__living

    @living.setter
    def living(self, status:bool) ->None:
        self.__living = status

    @property
    def will_be_alive(self) ->bool:
        return self.__will_be_alive

    @property
    def neighbors(self) ->int:
        return self.__neighbors

    @neighbors.setter
    def neighbors(self, neighbors) ->None:
        self.__neighbors = neighbors
