from typing import Any

from datastructures.array import Array
from datastructures.iqueue import IQueue, T

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
        raise NotImplementedError

    def enqueue(self, item: T) -> None:
        raise NotImplementedError

    def dequeue(self) -> T:
        raise NotImplementedError

    def clear(self) -> None:
        raise NotImplementedError

    @property
    def front(self) -> T:
        raise NotImplementedError

    @property
    def full(self) -> bool:
        raise NotImplementedError

    @property
    def empty(self) -> bool:

        raise NotImplementedError
    
    @property
    def maxsize(self) -> int:
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        raise NotImplementedError   
    
    def __len__(self) -> int:

        raise NotImplementedError

    def __str__(self) -> str:

        return str(self.circularqueue)

    def __repr__(self) -> str:
        return f'ArrayQueue({repr(self.circularqueue)})'
                                  
