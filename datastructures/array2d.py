from __future__ import annotations
import os
from typing import Iterator, Sequence

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T


class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int, data_type: type) -> None:
            self.__row_index = row_index
            self.__num_columns = num_columns
            self.__data_type = data_type
            self.__array = array

        def __getitem__(self, column_index: int) -> T:
            if column_index >= self.__num_columns:
                raise IndexError("Column index out of bounds")
            else:
                return self.__array[(self.__row_index * self.__num_columns) + column_index]
        
        def __setitem__(self, column_index: int, value: T) -> None:
            if column_index >= self.__num_columns:
                raise IndexError("Column index out of bounds")
            elif not isinstance(value, self.__data_type):
                raise ValueError(f"This array only accepts data of type {self.__data_type}")
            else:
                self.__array[(self.__row_index * self.__num_columns) + column_index] = value
        
        def __iter__(self) -> Iterator[T]:
            for column_index in range(self.__num_columns):
                yield self[column_index]
        
        def __reversed__(self) -> Iterator[T]:
            for column_index in range(self.__num_columns-1, -1, -1):
                yield self[column_index]

        def __len__(self) -> int:
            return self.__num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.__num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.__row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.__num_columns - 1)])}, {str(self[self.__num_columns - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        if not isinstance(starting_sequence, Sequence):
            raise ValueError("Starting_sequence should be a sequence")
        if not isinstance(data_type, type):
            raise ValueError("Data_type should be a type")
        self.__data_type = data_type
        self.__num_columns = len(starting_sequence[0])
        self.__num_rows = len(starting_sequence)
        unpacked_sequence = []
        for row in starting_sequence:
            if not isinstance(row, Sequence):
                raise ValueError("Starting_sequence should contain sequences")
            elif len(row) != self.__num_columns:
                raise ValueError("All elements of starting_sequence should be of the same length")
            else:
                for i in row:
                    if not isinstance(i, data_type):
                        raise ValueError(f"All elements of starting_sequence should be of type {data_type}")
                    else:
                        unpacked_sequence.append(i)
        self.__array = Array(unpacked_sequence, data_type)

    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        return Array2D([[data_type() for _ in range(cols)] for _ in range(rows)], data_type)

    def __getitem__(self, row_index: int) -> Array2D.IRow[T]:
        if row_index >= self.__num_rows:
            raise IndexError("Row index out of bounds")
        else:
            return self.Row(row_index, self.__array, self.__num_columns, self.__data_type)
    
    def __iter__(self) -> Iterator[Sequence[T]]: 
        for row_index in range(self.__num_rows):
            yield self[row_index]
    def __reversed__(self):
        for row_index in range(self.__num_rows-1, -1, -1):
            yield self[row_index]
    
    def __len__(self): 
        return self.__num_rows
                                  
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(row)}" for row in self)}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.__num_rows} Rows x {self.__num_columns} Columns, items: {str(self)}'

    @property
    def width(self) ->int:
        return self.__num_columns

    def __eq__(self,other:Array2D):
        if len(self) != len(other):
            return False
        else:
            is_equal = []
            for i in range(len(self)):
                for j in range(self.width):
                    is_equal.append(self[i][j] == other[i][j])
            return all(is_equal)

    def tolist(self) ->list:
        return [[self[j][i] for i in range(self.width)] for j in range(len(self))]

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')