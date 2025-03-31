from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

        def __eq__(self, other):
            return self == other if isinstance(other, LinkedList.Node) else self.data == other

    def __init__(self, data_type: type = object) -> None:
        self.__data_type = data_type
        self.__head = None
        self.__tail = None
        self.__count = 0

    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        raise NotImplementedError("LinkedList.from_sequence is not implemented")

    def append(self, item: T) -> None:
        if self.empty:
            self.__head = self.__tail = self.Node(item)
        else:
            new_node = self.Node(item, previous=self.__tail)
            self.__tail.next = new_node
            self.__tail = new_node
        self.__count += 1

    def prepend(self, item: T) -> None:
        if self.empty:
            self.__head = self.__tail = self.Node(item)
        else:
            new_node = self.Node(item, next=self.__head)
            self.__head.previous = new_node
            self.__head = new_node
        self.__count += 1

    def insert_before(self, target: T, item: T) -> None:
        raise NotImplementedError("LinkedList.insert_before is not implemented")

    def insert_after(self, target: T, item: T) -> None:
        raise NotImplementedError("LinkedList.insert_after is not implemented")

    def remove(self, item: T) -> None:
        raise NotImplementedError("LinkedList.remove is not implemented")

    def remove_all(self, item: T) -> None:
        raise NotImplementedError("LinkedList.remove_all is not implemented")

    def pop(self) -> T:
        raise NotImplementedError("LinkedList.pop is not implemented")

    def pop_front(self) -> T:
        raise NotImplementedError("LinkedList.pop_front is not implemented")

    @property
    def front(self) -> T:
        if self.empty:
            raise IndexError("List is empty")
        else:
            return self.__head

    @property
    def back(self) -> T:
        if self.empty:
            raise IndexError("List is empty")
        else:
            return self.__tail

    @property
    def empty(self) -> bool:
        return False if self.__head or self.__tail else True

    def __len__(self) -> int:
        return self.__count

    def clear(self) -> None:
        raise NotImplementedError("LinkedList.clear is not implemented")

    def __contains__(self, item: T) -> bool:
        raise NotImplementedError("LinkedList.__contains__ is not implemented")

    def __iter__(self) -> ILinkedList[T]:
        raise NotImplementedError("LinkedList.__iter__ is not implemented")

    def __next__(self) -> T:
        raise NotImplementedError("LinkedList.__next__ is not implemented")
    
    def __reversed__(self) -> ILinkedList[T]:
        raise NotImplementedError("LinkedList.__reversed__ is not implemented")
    
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("LinkedList.__eq__ is not implemented")

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.__head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.__count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
