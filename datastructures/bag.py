from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        """
        Initialises the bag data structure and iterates over items and adds them, if present
        Arguments:
            self
            items: The items to be added, optional
        Returns:
            None
        """
        self.__bag = {}
        if items:
            for i in items:
                self.add(i)

    def add(self, item: T) -> None:
        """
        Adds one item to the bag, updating count if already present
        Arguments:
            self
            item: Item to be added
        Returns:
            None
        """
        if item is None:
            raise TypeError
        else:
            if item not in self.__bag:
                self.__bag[item] = 1
            else:
                self.__bag[item] += 1

    def remove(self, item: T) -> None:
        """
        Decreases an item's count, removing when it releases zero. Raises ValueError if item is not present
        Parameters:
            self
            item: the item to be removed
        Returns:
            None
        """
        if item not in self.__bag:
            raise ValueError
        else:
            self.__bag[item] -= 1
            if self.__bag[item] == 0:
                del self.__bag[item]

    def count(self, item: T) -> int:
        """
        Returns the count of a specific item if present, zero otherwise
        Arguments:
            self
        Returns:
            count: number of occurrences in the item
        """
        try:
            count = self.__bag[item]
            return count
        except KeyError:
            return 0

    def __len__(self) -> int:
        """
        Returns the total number of occurrences of all items
        Parameters:
            self
        Returns:
            count: The total number of occurrences of all items
        """
        count = 0
        for i in self.__bag:
            count += self.__bag[i]
        return count

    def distinct_items(self) -> Iterable[T]:
        """
        Returns a list of all unique items in the bag
        Parameters:
            self
        Returns:
            Iterable[T]: a list of the unique items in the bag
        """
        return list(self.__bag.keys())

    def __contains__(self, item) -> bool:
        """
        Magic method tied to the "in" command
        Parameters:
            self
            item: the item to be checked
        Returns:
            bool: True if the item is in the bag, false otherwise
        """
        return item in self.__bag

    def clear(self) -> None:
        """
        Clears the bag of all data
        Parameters:
            self
        Returns:
            None
        """
        for i in self.distinct_items():
            self.remove(i)