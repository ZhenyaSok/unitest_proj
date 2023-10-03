import unittest

import pytest

from utils import arrs


@pytest.fixture
def arr_():
    return [1, 2, 3, 4, 5]


def test_get(arr_):
    assert arrs.get(arr_, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get(arr_, 6, "hi_test") == "hi_test"

def test_slice(arr_):
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], 1) == [2, 3, 4, 5]
    assert arrs.my_slice([2, 3], None, 3) == [2, 3]
