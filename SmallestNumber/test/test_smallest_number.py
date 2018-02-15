import pytest
from SmallestNumber.smallest_number import remove_smallest_item


def test_get_empty_list_for_empty_list():
    assert remove_smallest_item([]) == []


def test_least_number_is_removed():
    assert remove_smallest_item([3, 5, 1, 2, 4]) == [3, 5, 2, 4]


def test_when_there_are_two_smallest_adjacent_numbers():
    assert remove_smallest_item([3, 5, 1, 1, 4]) == [3, 5, 1, 4]


def test_when_there_are_two_smallest_numbers():
    assert remove_smallest_item([3, 5, 1, 4, 1]) == [3, 5, 4, 1]
