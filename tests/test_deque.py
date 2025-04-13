import pytest
from datastructures.deque import Deque
from cg_pytest_reporter import suite_weight, suite_name, name

@suite_weight(1.0)
@suite_name('Deque Test Suite')
class TestDeque:
    @pytest.fixture
    def empty_deque(self) -> Deque[int]:
        # @name Fixture for an empty deque
        return Deque[int](data_type=int)

    @pytest.fixture
    def populated_deque(self) -> Deque[int]:
        # @name Fixture for a deque pre-populated with integers
        deque = Deque[int](data_type=int)
        for i in range(5):  # Enqueue 0, 1, 2, 3, 4
            deque.enqueue(i)
        return deque

    @name('Test Enqueue Adds Element to Back of Deque')
    def test_enqueue(self, empty_deque: Deque[int]) -> None:
        empty_deque.enqueue(10)
        assert len(empty_deque) == 1
        assert empty_deque.back() == 10
        assert empty_deque.front() == 10
        assert empty_deque.empty() is False
        assert 10 in empty_deque

    @name('Test Dequeue Removes Element from Front of Deque')
    def test_dequeue(self, populated_deque: Deque[int]) -> None:
        assert populated_deque.dequeue() == 0
        assert len(populated_deque) == 4
        assert populated_deque.front() == 1

    @name('Test Dequeue on Empty Deque Raises Exception')
    def test_dequeue_empty(self, empty_deque: Deque[int]) -> None:
        with pytest.raises(IndexError):
            empty_deque.dequeue()

    @name('Test Enqueue Front Adds Element to Front of Deque')
    def test_enqueue_front(self, empty_deque: Deque[int]) -> None:
        empty_deque.enqueue_front(10)
        assert len(empty_deque) == 1
        assert empty_deque.front() == 10
        assert empty_deque.back() == 10
        assert empty_deque.empty() is False
        assert 10 in empty_deque

    @name('Test Dequeue Back Removes Element from Back of Deque')
    def test_dequeue_back(self, populated_deque: Deque[int]) -> None:
        assert populated_deque.dequeue_back() == 4
        assert len(populated_deque) == 4
        assert populated_deque.back() == 3

    @name('Test Dequeue Back on Empty Deque Raises Exception')
    def test_dequeue_back_empty(self, empty_deque: Deque[int]) -> None:
        with pytest.raises(IndexError):
            empty_deque.dequeue_back()

    @name('Test Front Property Returns First Element')
    def test_front(self, populated_deque: Deque[int]) -> None:
        assert populated_deque.front() == 0

    @name('Test Front Property on Empty Deque Raises Exception')
    def test_front_empty(self, empty_deque: Deque[int]) -> None:
        with pytest.raises(IndexError):
            _ = empty_deque.front()

    @name('Test Back Property Returns Last Element')
    def test_back(self, populated_deque: Deque[int]) -> None:
        assert populated_deque.back() == 4

    @name('Test Back Property on Empty Deque Raises Exception')
    def test_back_empty(self, empty_deque: Deque[int]) -> None:
        with pytest.raises(IndexError):
            _ = empty_deque.back()

    @name('Test Empty Property Returns True for Empty Deque')
    def test_empty_property(self, empty_deque: Deque[int], populated_deque: Deque[int]) -> None:
        assert empty_deque.empty() is True
        assert populated_deque.empty() is False

    @name('Test Length of Deque')
    def test_len(self, empty_deque: Deque[int], populated_deque: Deque[int]) -> None:
        assert len(empty_deque) == 0
        assert len(populated_deque) == 5

    @name('Test Clear Empties the Deque')
    def test_clear(self, populated_deque: Deque[int]) -> None:
        populated_deque.clear()
        assert len(populated_deque) == 0
        assert populated_deque.empty() is True

    @name('Test Contains Checks Membership in Deque')
    def test_contains(self, populated_deque: Deque[int]) -> None:
        assert 3 in populated_deque
        assert 10 not in populated_deque

    @name('Test Equality of Two Deques')
    def test_eq(self, populated_deque: Deque[int]) -> None:
        other_deque = Deque[int](data_type=int)
        for i in range(5):  # Enqueue 0, 1, 2, 3, 4
            other_deque.enqueue(i)
        assert populated_deque == other_deque

    @name('Test Inequality of Two Deques with Different Elements')
    def test_neq_different_elements(self, populated_deque: Deque[int]) -> None:
        other_deque = Deque[int](data_type=int)
        for i in range(4):  # Enqueue 0, 1, 2, 3
            other_deque.enqueue(i)
        assert populated_deque != other_deque

    @name('Test Inequality of Two Deques with Different Sizes')
    def test_neq_different_sizes(self, populated_deque: Deque[int]) -> None:
        other_deque = Deque[int](data_type=int)
        for i in range(6):  # Enqueue 0, 1, 2, 3, 4, 5
            other_deque.enqueue(i)
        assert populated_deque != other_deque

    @name('Test Equality with Non-Deque Object')
    def test_eq_non_deque(self, populated_deque: Deque[int]) -> None:
        assert populated_deque != [0, 1, 2, 3, 4]

