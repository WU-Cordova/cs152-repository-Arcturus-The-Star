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
            return (id(self) == id(other)) if isinstance(other, LinkedList.Node) else self.data == other

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
        elif not isinstance(target, self.__data_type):
            raise TypeError("Target is of invalid type")
        elif target not in self:
            raise ValueError("Target is not present")
        else:
            for i in self:
                if i == target:
                    target_node = i
                    break
            if target_node == self.__head:
                self.prepend(item)
            else:
                new_node = self.Node(item, target_node, target_node.previous)
                target_node.previous.next = new_node
                target_node.previous = new_node
            self.__count += 1

    def insert_after(self, target: T, item: T) -> None:
        if not isinstance(item, self.__data_type):
            raise TypeError("Item is of invalid type")
        elif not isinstance(target, self.__data_type):
            raise TypeError("Target is of invalid type")
        elif target not in self:
            raise ValueError("Target is not present")
        else:
            for i in self:
                if i == target:
                    target_node = i
                    break
            if target_node == self.__tail:
                self.append(item)
            else:
                new_node = self.Node(item, target_node.next, target_node)
                target_node.next.previous = new_node
                target_node.next = new_node
            self.__count += 1


    def remove(self, item: T) -> None:
        if not isinstance(item, self.__data_type):
            raise TypeError("Item is of invalid type")
        elif item not in self:
            raise ValueError("Item is not present")
        else:
            for i in self:
                if i == item:
                    target = i
                    break
            if len(self) == 1:
                self.clear()
            elif target == self.__head:
                self.pop_front()
            elif target == self.__tail:
                self.pop()
            else:
                target.next.previous = target.previous
                target.previous.next = target.next
                self.__count -= 1


    def remove_all(self, item: T) -> None:
        if not isinstance(item, self.__data_type):
            raise TypeError("Item is of invalid type")
        elif item not in self:
            raise ValueError("Item is not present")
        else:
            for i in self:
                if i == item:
                    self.remove(i.data)

    def pop(self) -> T:
        if self.empty:
            raise IndexError("List is empty")
        else:
            node = self.__tail
            self.__tail = node.previous
            self.__tail.next = None
            self.__count -= 1
            return node

    def pop_front(self) -> T:
        if self.empty:
            raise IndexError("List is empty")
        else:
            node = self.__head
            self.__head = node.next
            self.__head.next = None
            self.__count -= 1
            return node

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
        self.__head = self.__tail = None
        self.__count = 0

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
        node = self.__tail
        for i in range(len(self)):
            nd = node
            node = nd.previous
            yield nd

    def __eq__(self, other: LinkedList) -> bool:
        return (len(self) == len(other)) and all([(i.data == j.data) and (i.previous.data == j.previous.data if i.previous else True) and (i.next.data == j.next.data if i.next else True) for i,j in zip(self, other)])

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