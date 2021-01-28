import pytest

from lessons.lesson1.classwork import min_even_digit
from lessons.lesson1.tests.models import MinEvenNumberTestData

mid_even_digit_data = [
    MinEvenNumberTestData(number=123, answer=2),
    MinEvenNumberTestData(number=1111, answer=None),
    MinEvenNumberTestData(number=0, answer=None),
    MinEvenNumberTestData(number=169943, answer=4),
    MinEvenNumberTestData(number=8967925876, answer=2),
]


@pytest.mark.parametrize("test_data", mid_even_digit_data)
def test_euclid(test_data: MinEvenNumberTestData):
    """Tests that min_even_digit is written good."""
    answer = min_even_digit(test_data.number)
    assert answer == test_data.answer
