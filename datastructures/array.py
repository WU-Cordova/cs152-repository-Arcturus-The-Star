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
            raise ValueError("Starting_sequence should be a sequence")
        if not isinstance(data_type, type):
            raise ValueError("Data_type should be a type")
        for i in starting_sequence:
            if not isinstance(i, data_type):
                raise TypeError("Data type and items in the starting sequence are not the same type")
        sequence_copy = copy.deepcopy(starting_sequence)
        self.__items = np.array(sequence_copy, data_type)
        self.__item_count = len(self.__items) # Logical size
        self.__data_type = data_type
        self.__capacity = len(self.__items) # Physical size

    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        valid_range = range(-self.__item_count, self.__item_count + 1)
        if isinstance(index, slice):
            start = index.start if index.start else None
            stop = index.stop if index.start else None
            step = index.step if index.step else 1
            if (start not in valid_range or stop not in valid_range) and (start is not None or stop is not None):
                raise IndexError("Index out of bounds")
            else:
                return Array(starting_sequence=(self.__items[start:stop:step]).tolist(), data_type=self.__data_type)
        elif isinstance(index, int):
            if index not in valid_range:
                raise IndexError("Index out of bounds")
            else:
                item = self.__items[index]
                return item.item() if isinstance(item, np.generic) else item
        else:
            raise TypeError("Bracket operation should be of type int or slice")
    
    def __setitem__(self, index: int, item: T) -> None:
        if index not in range(-self.__item_count, self.__item_count + 1):
            raise IndexError("Index out of bounds")
        elif not isinstance(item, self.__data_type):
            raise TypeError(f"Input should be of type {self.__data_type}")
        else:
            self.__items[index] = item

    def append(self, data: T) -> None:
        if type(data) != self.__data_type:
            raise TypeError(f"This Array has a data type of {self.__data_type} and does not accept other types")
        self.__grow()
        self.__items[self.__item_count] = data
        self.__item_count += 1

    def append_front(self, data: T) -> None:
        self.__grow()
        new_contents = [data] + self.__items.tolist()[:self.__item_count]
        for i in range(len(self.__items[:self.__item_count])):
            self.__items[i] = new_contents[i]
        self.__item_count += 1

    def pop(self) -> T:
        item = self[-1]
        del self[-1]
        return item
    
    def pop_front(self) -> T:
        item = self[0]
        del self[0]
        return item

    def __len__(self) -> int: 
        return self.__item_count

    def __eq__(self, other: Array[T]) -> bool:
        return isinstance(other, Array) and (len(self) == len(other)) and ([item for item in self] == [item for item in other])
    
    def __iter__(self) -> Iterator[T]:
       return iter(self.__items[:self.__item_count + 1])

    def __reversed__(self) -> Iterator[T]:
        return iter(list(self.__items)[::-1])

    def __delitem__(self, index: int) -> None:
        if index not in range(-self.__item_count, self.__item_count + 1):
            raise IndexError("Index out of range")
        else:
            data_list = self.__items.tolist()
            self.__items = np.array(data_list[:index] + data_list[index + 1:] + [self.__data_type()], self.__data_type)
            self.__item_count -= 1
            self.__shrink()

    def __contains__(self, item: Any) -> bool:
        return any([item == other_item for other_item in self])

    def clear(self) -> None:
        self.__items = np.array([], self.__data_type)
        self.__capacity = 0
        self.__item_count = 0

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in list(self)[:self.__item_count]) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__item_count}, Physical: {len(self.__items)}, type: {self.__data_type}'

    def __grow(self) -> None:
        """
        Grows the internal array to double its current size if the logical size (item_count) reaches the physical size (capacity).
        """
        if self.__capacity > self.__item_count:
            return
        else:
            new_ar = np.array([self.__data_type() for i in range((self.__capacity * 2) if self.__capacity else 1)], self.__data_type)
            for i in range(len(self)):
                new_ar[i] = self.__items[i]
            self.__capacity = len(new_ar)
            self.__items = new_ar

    def __shrink(self) -> None:
        """
        Shrinks the array to half of its current size if the logical size (item_count) reaches one quarter of the physical size (capacity)
        """
        if self.__item_count > self.__capacity // 4:
            return
        else:
            new_ar = np.array([self.__data_type() for i in range(self.__capacity // 2)], self.__data_type)
            for i in range(len(self)):
                new_ar[i] = self.__items[i]
            self.__capacity = len(new_ar)
            self.__items = new_ar



    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')