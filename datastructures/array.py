# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
import copy
from numpy.typing import NDArray


from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: 
        if not isinstance(starting_sequence, Sequence):
            raise ValueError("starting_sequence should be a sequence")
        if not isinstance(data_type, type):
            raise ValueError("data_type should be a type")
        sequence_copy = copy.deepcopy(starting_sequence)
        self.__items = np.array(sequence_copy, data_type)
        self.__item_count = len(sequence_copy) # Logical size
        self.__data_type = data_type
        self.__capacity = len(sequence_copy) # Physical size

    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        valid_range = range(-self.__item_count, self.__item_count + 1)
        if isinstance(index, slice):
            start = index.start if index.start else 0
            stop = index.stop if index.start else -1
            step = index.step if index.step else 1
            if start not in valid_range and stop not in valid_range:
                raise IndexError("Slide not in range")
            else:
                return Array(starting_sequence=self.__items[start:stop:step].tolist(), data_type=self.__data_type)
        else:
            if index not in valid_range:
                raise IndexError("Index not in range")
            else:
                item = self.__items[index]
                return item.item() if isinstance(item, np.generic) else item
    
    def __setitem__(self, index: int, item: T) -> None:
        if index not in range(-self.__item_count, self.__item_count + 1):
            raise IndexError("Index out of range")
        elif not isinstance(item, self.__data_type):
            raise TypeError("Data type does not match")
        else:
            self.__items[index] = item

    def append(self, data: T) -> None:
        raise NotImplementedError('Append not implemented.')

    def append_front(self, data: T) -> None:
        raise NotImplementedError('Append front not implemented.')

    def pop(self) -> None:
        raise NotImplementedError('Pop not implemented.')
    
    def pop_front(self) -> None:
        raise NotImplementedError('Pop front not implemented.')

    def __len__(self) -> int: 
        return len(self.__items)

    def __eq__(self, other: Array[T]) -> bool:
        return (len(self) == len(other)) and ([item for item in self] == [item for item in other])
    
    def __iter__(self) -> Iterator[T]:
       return iter(self.__items)

    def __reversed__(self) -> Iterator[T]:
        return iter(Array(starting_sequence=list(self.__items)[::-1], data_type=self.__data_type))

    def __delitem__(self, index: int) -> None:
        raise NotImplementedError('Delete not implemented.')

    def __contains__(self, item: Any) -> bool:
        return any([item == other_item for other_item in self])

    def clear(self) -> None:
        raise NotImplementedError('Clear not implemented.')

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__item_count}, Physical: {len(self.__items)}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')