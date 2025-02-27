from Cell import Cell
from datastructures.array2d import Array2D


class Grid(Array2D):

    def __init__(self, input_permutation:list[list[bool]]):
        super(Grid, self).__init__([[Cell((j,i), input_permutation[j][i]) for i in range(len(input_permutation[0]))] for j in range(len(input_permutation))], Cell)
        self.__living_cells = 0
        self.count_living()

    @property
    def living_cells(self):
        return self.__living_cells

    def count_living(self):
        counter = 0
        for i in self:
            for j in i:
                if j.living:
                    counter += 1
        self.__living_cells = counter

    def update_neighbors(self, row, col) ->int:
        neighbors = []
        for i in range(-1,2):
            for j in range(-1,2):
                if  (0 <= row + i < len(self) and 0 <= col + j < self.width) and not (i == 0 and j == 0):
                    neighbors.append(self[row + i][col + j].living)
        self[row][col].neighbors = neighbors.count(True)

    def update_all_neighbors(self):
        for row in range(len(self)):
            for col in range(self.width):
                self.update_neighbors(row,col)

    def predict_all_cells(self):
        for row in range(len(self)):
            for col in range(self.width):
                self[row][col].prospective_life()

    def update_all_cells(self):
        for row in range(len(self)):
            for col in range(self.width):
                self[row][col].update_life()

    def __str__(self):
        output = ""
        for i in range(len(self)):
            for j in range(self.width):
                output += str(self[i][j]) + " "
            output += "\n"
        return output

    def __repr__(self):
        return f'Grid {self.width} Rows x {len(self)} Columns, living cells: {self.__living_cells}, items:\n{str(self)}'



if __name__ == "__main__":
    gr = Grid([[False,False,True,False,False],[False,False,True,False,False],[False,False,True,False,False]])
