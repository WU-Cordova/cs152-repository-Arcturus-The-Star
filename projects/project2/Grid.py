from Cell import Cell
from datastructures.array2d import Array2D

def random_permutation():
    pass

class Grid(Array2D):
    def __init__(self, input_permutation=random_permutation()):
        super(Grid, self).__init__(input_permutation, Cell)
        self.__living_cells = 0

    @property
    def living_cells(self):
        return self.__living_cells