import copy
import os
from datastructures.istack import IStack
from typing import Generic
from datastructures.linkedlist import LinkedList

from datastructures.linkedlist import LinkedList

class ListStack[T](IStack[T]):
    """
    ListStack (LinkedList-based Stack)

    """

    def __init__(self, data_type:type=object) -> None:
        """
        Initializes the ListStack.

        Args:
            data_type (type): The type of data the stack will hold.

        """
        self.__list = LinkedList(data_type)
        self.__data_type = data_type

    def push(self, item: T):
        """
        Pushes an item onto the stack.

        Args:
            item (T): The item to push onto the stack.
        
        Raises:
            TypeError: If the item is not of the correct type.

        """
        if not isinstance(item, self.__data_type):
            raise TypeError("Item is not of the correct type")
        else:
            self.__list.append(item)

    def pop(self) -> T:
        """
        Removes and returns the top item from the stack.

        Returns:
            T: The top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        if self.empty:
            raise IndexError("Stack is empty")
        else:
            return self.__list.pop()

    def peek(self) -> T:
        """
        Returns the top item from the stack without removing it.

        Returns:
            T: The top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        if self.empty:
            raise IndexError("Stack is empty")
        else:
            return self.__list.back

    @property
    def empty(self) -> bool:
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.__list.empty

    def clear(self):
        """
        Clears all items from the stack.
        """
        self.__list.clear()

    def __contains__(self, item: T) -> bool:
        """
        Checks if an item exists in the stack.

        Args:
            item (T): The item to check for.

        Returns:
            bool: True if the item exists in the stack, False otherwise.

        """
        return item in self.__list

    def __eq__(self, other) -> bool:
        """
        Compares two stacks for equality.

        Args:
            other (ListStack): The stack to compare with.

        Returns:
            bool: True if the stacks are equal, False otherwise.

        """
        if len(self) != len(other):
            return False
        else:
            scopy = copy.deepcopy(self)
            ocopy = copy.deepcopy(other)
            for i in range(len(self)):
                if scopy.pop() != ocopy.pop():
                    return False
            return True


    def __len__(self) -> int:
        """
        Returns the number of items in the stack.

        Returns:
            int: The number of items in the stack.
        """
        return len(self.__list)

    def __str__(self) -> str:
        """
        Returns a string representation of the stack.

        Returns:
            str: A string representation of the stack.
        """
        return str([i for i in self.__list])

    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the stack.

        Returns:
            str: A detailed string representation of the stack.

        """
        return f"LinkedList Stack {str(self)}, data type {self.__data_type}"
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')