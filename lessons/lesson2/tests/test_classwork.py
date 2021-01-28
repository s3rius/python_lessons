import pytest

from lessons.lesson2.classwork import find_fibonacci_in_list, sum_fractions
from lessons.lesson2.tests.models import FibonacciFinderTestData, SumFractionsTestData

sum_fractions_data = []

find_fibonacci_test_data = []


@pytest.mark.parametrize("test_data", sum_fractions_data)
def test_fraction_sum(test_data: SumFractionsTestData):
    """Tests that sum_fractions is written good."""
    answer = sum_fractions(val_a=test_data.first, val_b=test_data.second)
    assert answer == test_data.answer


@pytest.mark.parametrize("test_data", find_fibonacci_test_data)
def test_fibonacci_finder(test_data: FibonacciFinderTestData):
    """Tests that find_fibonacci_in_list is written good."""
    answer = find_fibonacci_in_list(input_list=test_data.sequence)
    assert answer == test_data.answer
