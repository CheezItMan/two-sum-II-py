import pytest
from lib.two_sum import two_sum


def test_example_one():
    nums = [2, 7, 11, 15]
    target = 9

    assert two_sum(nums, target) == [0, 1]


def test_example_two():
    nums = [2, 3, 4]
    target = 6

    assert two_sum(nums, target) == [0, 2]


def test_example_three():
    nums = [-1, 0]
    target = -1

    assert two_sum(nums, target) == [0, 1]


def test_edge_case():
    nums = []
    target = -1

    assert two_sum(nums, target) == None


def test_other_edge_case():
    nums = [1, 2, 3, 4, 5]
    target = 27

    assert two_sum(nums, target) == None
