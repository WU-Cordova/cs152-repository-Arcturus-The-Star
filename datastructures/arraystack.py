from __future__ import annotations
import os
from datastructures.array import Array, T
from datastructures.istack import IStack
from copy import deepcopy

class ArrayStack(IStack[T]):
    """ ArrayStack class that implements the IStack interface. The ArrayStack is a
        fixed-size stack that uses an Array to store the items."""
    
    def __init__(self, max_size: int = 0, data_type=object) -> None:
        """ Constructor to initialize the stack

            Arguments:
                max_size: int -- The maximum size of the stack.
                data_type: type -- The data type of the stack.
        """
        self.__data_type = data_type
        self.__stack = Array([self.__data_type() for _ in range(max_size)], data_type)
        self.__max_size = max_size
        self.__top = -1

    def push(self, item: T) -> None:
        if self.__top == self.__max_size - 1:
            raise IndexError("Stack overflow")
        elif not isinstance(item, self.__data_type):
            raise TypeError("Item type is invalid")
        else:
            self.__top += 1
            self.__stack[self.__top] = item

    def pop(self) -> T:
        if self.__top == -1:
            raise IndexError("Stack underflow")
        else:
            item = self.__stack[self.__top]
            self.__top -= 1
            return item

    def clear(self) -> None:
       self.__top = -1
    @property
    def peek(self) -> T:
       return self.__stack[self.__top]

    @property
    def maxsize(self) -> int:
        """ Returns the maximum size of the stack.

            Returns:
                int: The maximum size of the stack.
        """
        return self.__max_size
    
    @property
    def full(self) -> bool:
        """ Returns True if the stack is full, False otherwise.

            Returns:
                bool: True if the stack is full, False otherwise.
        """
        return self.__top == self.__max_size - 1

    @property
    def empty(self) -> bool:
        return self.__top == -1

    def __eq__(self, other: ArrayStack) -> bool:
        if not len(self) == len(other):
            return False
        else:
            return all([deepcopy(self).pop() == deepcopy(other).pop() for _ in range(len(self))])


    def __len__(self) -> int:
       return self.__top + 1
    
    def __contains__(self, item: T) -> bool:
       return item in self.__stack

    def __str__(self) -> str:
        return str([self.__stack[i] for i in range(self.__top + 1)])
    
    def __repr__(self) -> str:
        return f"ArrayStack({self.maxsize}): items: {str(self)}"
    
if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')

