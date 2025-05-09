from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional, Sequence, Iterator
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
            return self.data == other.data if isinstance(other, LinkedList.Node) else self.data == other

    def __init__(self, data_type: type = object) -> None:
        self.__data_type:type = data_type
        self.__head:LinkedList.Node | None = None
        self.__tail:LinkedList.Node | None = None
        self.__count:int = 0

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
        else:
            target_node = self.find(target)
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
            target_node = self.find(target)
            if target_node == self.__tail:
                self.append(item)
            else:
                new_node = self.Node(item, target_node.next, target_node)
                target_node.next.previous = new_node
                target_node.next = new_node
            self.__count += 1


    def remove(self, item: T) -> None:
        if not (node := isinstance(item, LinkedList.Node)) and not isinstance(item, self.__data_type):
            raise TypeError("Item is of invalid type")
        elif item not in self:
            raise ValueError("Item is not present")
        else:
            if node:
                target = item
            else:
                target = self.find(item)
            if len(self) == 1:
                self.clear()
            elif not target.previous:
                self.pop_front()
            elif not target.next:
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
            travel = self.__head
            while travel:
                if travel == item:
                    self.remove(travel)
                travel = travel.next

    def pop(self) -> T:
        if self.empty:
            raise IndexError("List is empty")
        elif len(self) == 1:
            data = self.__tail.data
            self.clear()
            return data
        else:
            node = self.__tail
            self.__tail = node.previous
            self.__tail.next = None
            self.__count -= 1
            return node.data

    def pop_front(self) -> T:
        if self.empty:
            raise IndexError("List is empty")
        elif len(self) == 1:
            data = self.__tail.data
            self.clear()
            return data
        else:
            node = self.__head
            self.__head = node.next
            self.__head.previous = None
            self.__count -= 1
            return node.data

    @property
    def front(self) -> T:
        if self.empty:
            raise IndexError("List is empty")
        else:
            return self.__head.data

    @property
    def back(self) -> T:
        if self.empty:
            raise IndexError("List is empty")
        else:
            return self.__tail.data

    @property
    def empty(self) -> bool:
        return False if self.__head or self.__tail else True

    def __len__(self) -> int:
        return self.__count

    def clear(self) -> None:
        self.__head = self.__tail = None
        self.__count = 0

    def find(self, target:T) ->LinkedList.Node:
        """
        Finds the first instance of a node with the target data
        :param target: The desired data
        :return: The first instance of the data
        """
        if not isinstance(target, self.__data_type):
            raise TypeError("Target is of invalid type")
        else:
            travel = self.__head
            while travel:
                if travel == target:
                    return travel
                else:
                    travel = travel.next
            raise ValueError("Target is not present")

    def __contains__(self, item: T) -> bool:
        for i in self:
            if item == i:
                return True
        return False

    def __iter__(self) -> Iterator[T]:
        node = self.__head
        while node:
            nd = node
            node = nd.next
            yield nd.data

    def __next__(self) -> T:
        pass
    
    def __reversed__(self) -> ILinkedList[T]:
        link = LinkedList(self.__data_type)
        for i in self:
            link.prepend(i)
        return link

    def __eq__(self, other: LinkedList) -> bool:
        return (len(self) == len(other)) and all([(i == j) for i,j in zip(self, other)])

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
