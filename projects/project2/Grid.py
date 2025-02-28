from Cell import Cell
from datastructures.array2d import Array2D


class Grid(Array2D):

    def __init__(self, input_permutation:list[list[bool]]):
        """
        A grid that contains cells, feeds them data, and tells them what to do.
        :param input_permutation: A list of lists of booleans, used to build the grid.
        """
        super(Grid, self).__init__([[Cell((j,i), input_permutation[j][i]) for i in range(len(input_permutation[0]))] for j in range(len(input_permutation))], Cell)
        self.__living_cells = 0
        self.count_living()
        self.update_all_neighbors()
        self.predict_all_cells()

    @property
    def living_cells(self):
        return self.__living_cells

    def count_living(self):
        """
        Counts the number of living cells in the grid
        """
        counter = 0
        for i in self:
            for j in i:
                if j.living:
                    counter += 1
        self.__living_cells = counter

    def __update_neighbors(self, row, col):
        """
        Takes a cell at the specified coordinates and updates its number of neighbors
        :param row: The row coordinate of the desired cell
        :param col: The column coordinate of the desired cell
        """
        neighbors = []
        for i in range(-1,2):
            for j in range(-1,2):
                if  (0 <= row + i < len(self) and 0 <= col + j < self.width) and not (i == 0 and j == 0):
                    neighbors.append(self[row + i][col + j].living)
        self[row][col].neighbors = neighbors.count(True)

    def update_all_neighbors(self):
        """
        Updates the neighbors of every cell in the
        """
        for row in range(len(self)):
            for col in range(self.width):
                self.__update_neighbors(row, col)

    def predict_all_cells(self):
        """
        Tells every cell to calculate its prospective life
        """
        for row in range(len(self)):
            for col in range(self.width):
                self[row][col].prospective_life()

    def update_all_cells(self):
        """
        Updates every cell in the grid
        """
        for row in range(len(self)):
            for col in range(self.width):
                self[row][col].update_life()

    def __str__(self):
        output = ""
        for i in range(len(self)):
            for j in range(self.width):
                output += str(self[i][j]) + "  "
            output += "\n"
        return output

    def __repr__(self):
        return f'Grid {self.width} Rows x {len(self)} Columns, living cells: {self.__living_cells}, items:\n{str(self)}'

