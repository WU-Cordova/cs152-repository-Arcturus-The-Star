from abc import abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class IQueue(Generic[T]):
    ''' Interface for a queue data structure '''

    @abstractmethod
    def enqueue(self, item: T) -> None:
        """
        Adds an item to the rear of the queue

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> q.front
                1
                >>> q.rear
                3
                >>> q.enqueue(4)
                >>> q.enqueue(5)
                >>> q.full
                True
                >>> q.enqueue(6)
                IndexError('Queue is full')

            Arguments:
                item: The item to add to the queue

            Raises:
                IndexError: If the queue is full
        """
        ...

    @abstractmethod
    def dequeue(self) -> T:
        """
        Removes and returns the item at the front of the queue

                    Examples:
                        >>> q = CircularQueue(maxsize=5, data_type=int)
                        >>> q.enqueue(1)
                        >>> q.enqueue(2)
                        >>> q.enqueue(3)
                        >>> q.dequeue()
                        1
                        >>> q.dequeue()
                        2
                        >>> q.dequeue()
                        3
                        >>> q.dequeue()
                        IndexError('Queue is empty')
                        >>> q.dequeue()
                        IndexError('Queue is empty')

                    Returns:
                        The item at the front of the queue

                    Raises:
                        IndexError: If the queue is empty
                """
        ...

    @abstractmethod
    def front(self) -> T:
        """ Returns the item at the front of the queue without removing it

                    Returns:
                        The item at the front of the queue

                    Raises:
                        IndexError: If the queue is empty
                """
        ...

    @abstractmethod
    def back(self) -> T:
        ...

    @abstractmethod
    def __len__(self) -> int:
        """ Returns the number of items in the queue

                    Returns:
                        The number of items in the queue
                """
        ...

    @abstractmethod
    def is_empty(self) -> bool:
        """ Returns True if the queue is empty, False otherwise

            Returns:
                True if the queue is empty, False otherwise
        """
        ...

    @abstractmethod
    def clear(self) -> None:
        """ Removes all items from the queue """
        ...

    @abstractmethod
    def __contains__(self, item: T) -> bool:
        ...

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        """ Returns True if this CircularQueue is equal to another object, False otherwise

                    Equality is defined as:
                        - The front and rear pointers are equal
                        - The elements between the front and rear pointers are equal, even if they are in different positions

                    Arguments:
                        other: The object to compare this CircularQueue to

                    Returns:
                        True if this CircularQueue is equal to another object, False otherwise
                """
        ...

    @abstractmethod
    def __str__(self) -> str:
        """ Returns a string representation of the CircularQueue

                   Returns:
                       A string representation of the queue
               """
        ...

    @abstractmethod
    def __repr__(self) -> str:
        """ Returns a developer string representation of the CircularQueue object

                    Returns:
                        A string representation of the CircularQueue object
                """
        ...
