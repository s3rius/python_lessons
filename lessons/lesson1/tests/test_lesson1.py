import pytest

from lessons.lesson1.main import euclid, factorial
from lessons.lesson1.tests.models import EuclidTestData, FactorialTestData

euclid_data = [
    EuclidTestData(val_a=1, val_b=1, answer=1),
    EuclidTestData(val_a=34, val_b=442, answer=34),
    EuclidTestData(val_a=329120, val_b=17564830712, answer=1496),
    EuclidTestData(val_a=334960000, val_b=83739991626, answer=8374),
    EuclidTestData(val_a=334960000, val_b=83739991626, answer=8374),
    EuclidTestData(
        val_a=31402746386687432, val_b=81527783110470864834184, answer=179507896
    ),
]

factorial_data = [
    FactorialTestData(number=0, answer=1),
    FactorialTestData(number=2, answer=2),
    FactorialTestData(number=7, answer=5040),
    FactorialTestData(number=11, answer=39916800),
    FactorialTestData(number=12, answer=479001600),
    FactorialTestData(number=30, answer=265252859812191058636308480000000),
]


@pytest.mark.parametrize("test_data", euclid_data)
def test_euclid(test_data: EuclidTestData):
    """Tests that Euclidean gcd is written good."""
    answer = euclid(val_a=test_data.val_a, val_b=test_data.val_b)
    assert answer == test_data.answer


@pytest.mark.parametrize("test_data", factorial_data)
def test_factorial(test_data: FactorialTestData):
    """Tests that factorial is written good."""
    answer = factorial(number=test_data.number)
    assert answer == test_data.answer
