from typing import List

import pytest

from lessons.lesson2.classwork import find_fibonacci_in_list, sum_fractions
from lessons.lesson2.tests.models import FibonacciFinderTestData, SumFractionsTestData


def int_list(numbers_string: str) -> List[int]:
    """
    Cast str to list of ints.

    :param numbers_string: initial string.
    :return: resulting list.
    """
    return list(map(int, numbers_string))


sum_fractions_data = [
    SumFractionsTestData(first="2/3", second="4/9", answer="10/9"),
    SumFractionsTestData(first="23/432", second="1/1231", answer="28745/531792"),
    SumFractionsTestData(first="412/333", second="442/8432", answer="3621170/2807856"),
    SumFractionsTestData(
        first="9/432535645", second="1/4442", answer="432575623/1921323335090"
    ),
    SumFractionsTestData(first="1/44432", second="2/1112", answer="11247/6176048"),
]

find_fibonacci_test_data = [
    FibonacciFinderTestData(sequence=int_list("00001123333"), answer=int_list("01123")),
    FibonacciFinderTestData(sequence=int_list("12344"), answer=[]),
    FibonacciFinderTestData(
        sequence=int_list("452212234011233494925"),
        answer=int_list("011235"),
    ),
    FibonacciFinderTestData(
        sequence=int_list("9876543210123456789"),
        answer=[0, 1],
    ),
]


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
