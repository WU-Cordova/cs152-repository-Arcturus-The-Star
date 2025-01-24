from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        """
        Initialises the bag data structure and iterates over items and adds them, if present
        Arguments:
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
            item: the item to be removed
        Returns:
            None
        """
        if item not in self.__bag:
            raise ValueError
        else:
            self.__bag[item] -= 1
            if self.__bag[item] == 0:
                self.__bag[item].remove()

    def count(self, item: T) -> int:
        """
        Returns the count of a specific item if present, zero otherwise
        Arguments:

        Returns:
            int: number of occurrences in the item
        """

        try:
            count = self.__bag[item]
            return count
        except KeyError:
            return 0

    def __len__(self) -> int:
        raise NotImplementedError("__len__ method not implemented")

    def distinct_items(self) -> int:
        raise NotImplementedError("distinct_items method not implemented")

    def __contains__(self, item) -> bool:
        raise NotImplementedError("__contains__ method not implemented")

    def clear(self) -> None:
        raise NotImplementedError("clear method not implemented")