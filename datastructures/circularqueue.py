from typing import Any

from datastructures.array import Array
from datastructures.iqueue import IQueue, T
from copy import deepcopy


class CircularQueue(IQueue[T]):
    """ Represents a fixed-size circular queue. The queue
        is circular in the sense that the front and rear pointers wrap around the
        array when they reach the end. The queue is full when the rear pointer is
        one position behind the front pointer. The queue is empty when the front
        and rear pointers are equal. This implementation uses a fixed-size array.
    """

    def __init__(self, maxsize: int = 0, data_type=object) -> None:
        ''' Initializes the CircularQueue object with a maxsize and data_type.

            Arguments:
                maxsize: The maximum size of the queue
                data_type: The type of the elements in the queue
        '''
        self.__data_type = data_type
        self.__max_size = maxsize
        self.__queue = Array([self.__data_type() for _ in range(self.__max_size + 1)])
        self.__front = 0
        self.__rear = 0

    def enqueue(self, item: T) -> None:
        if not isinstance(item, self.__data_type):
            raise TypeError("Item is of invalid type")
        elif self.full:
            raise IndexError("Queue is full")
        else:
            self.__queue[self.__rear] = item
            self.__rear = (self.__rear + 1) % (self.__max_size + 1)

    def dequeue(self) -> T:
        if self.empty:
            raise IndexError("Queue is empty")
        else:
            item = self.__queue[self.__front]
            self.__front = (self.__front + 1) % (self.__max_size + 1)
            return item

    def clear(self) -> None:
        self.__front = 0
        self.__rear = 0

    @property
    def front(self) -> T:
        return self.__queue[self.__front]

    @property
    def full(self) -> bool:
        return (self.__rear + 1) % (self.__max_size + 1) == self.__front

    @property
    def empty(self) -> bool:
        return self.__front == self.__rear
    
    @property
    def maxsize(self) -> int:
        return self.__max_size

    @property
    def front_pointer(self):
        return self.__front

    @property
    def rear_pointer(self):
        return self.__rear

    def __eq__(self, other: object) -> bool:
        if not len(self) == len(other):
            return False
        else:
            s_queue = deepcopy(self)
            o_queue = deepcopy(other)
            eq = []
            for _ in range(len(self)):
                eq.append(s_queue.dequeue() == o_queue.dequeue())
            return all(eq)



    
    def __len__(self) -> int:
        return (self.__rear - self.__front + self.__max_size + 1) % (self.__max_size + 1)

    def __str__(self) -> str:
        return str(self.__queue)

    def __repr__(self) -> str:
        return f'ArrayQueue({repr(self.__queue)})'
                                  
