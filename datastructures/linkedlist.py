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

        def __str__(self):
            return str(self.data)

        def __eq__(self, other):
            if isinstance(other, LinkedList):
                pass
            elif not self.next or self.previous:
                pass
            else:
                return self.data == other
    def __init__(self, data_type: type = object) -> None:
        self.__data_type = data_type
        self.__head = None
        self.__tail = None
        self.__count = 0

    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        new_list = LinkedList(data_type)
        for i in sequence:
            new_list.append(i)
        return new_list

    def append(self, item: T) -> None:
        if not isinstance(item, self.__data_type):
            raise TypeError("Item is of invalid type")
        elif self.empty:
            self.__head = self.__tail = self.Node(item)
        else:
            new_node = self.Node(item, previous=self.__tail)
            self.__tail.next = new_node
            self.__tail = new_node
        self.__count += 1

    def prepend(self, item: T) -> None:
        if not isinstance(item, self.__data_type):
            raise TypeError("Item is of invalid type")
        elif self.empty:
            self.__head = self.__tail = self.Node(item)
        else:
            new_node = self.Node(item, next=self.__head)
            self.__head.previous = new_node
            self.__head = new_node
        self.__count += 1

    def insert_before(self, target: T, item: T) -> None:
        if not isinstance(item, self.__data_type):
            raise TypeError("Item is of invalid type")
        elif target not in self:
            raise ValueError("Target is not present")
        else:
            for i in self:
                if i == target:
                    targetnode = i
            if targetnode == self.__head:
                self.prepend(item)
            else:
                new_node = self.Node(item, targetnode, targetnode.previous)
                targetnode.previous.next = new_node
                targetnode.previous = new_node
            self.__count += 1

    def insert_after(self, target: T, item: T) -> None:
        if not isinstance(item, self.__data_type):
            raise TypeError("Item is of invalid type")
        elif target not in self:
            raise ValueError("Target is not present")
        else:
            for i in self:
                if i == target:
                    targetnode = i
            if targetnode == self.__tail:
                self.append(item)
            else:
                new_node = self.Node(item, targetnode.next, targetnode)
                targetnode.next.previous = new_node
                targetnode.next = new_node
            self.__count += 1


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
        for i in self:
            if item == i:
                return True
        return False

    def __iter__(self) -> ILinkedList[T]:
        node = self.__head
        for i in range(len(self)):
            nd = node
            node = nd.next
            yield nd

    def __next__(self) -> T:
        raise NotImplementedError("LinkedList.__next__ is not implemented")
    
    def __reversed__(self) -> ILinkedList[T]:
        raise NotImplementedError("LinkedList.__reversed__ is not implemented")
    
    def __eq__(self, other: LinkedList) -> bool:
        thing = zip(self, other)
        stuff = []
        for i,j in thing:
            stuff.append(i == j)
        return (len(self) == len(other)) and (all(stuff))

    def __str__(self) -> str:
        items = []
        current = self.__head
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
    thang = LinkedList.from_sequence([1,2,3], int)
    thung = LinkedList.from_sequence([1,2,3], int)
    print(thang == thung)