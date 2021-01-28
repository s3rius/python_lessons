from dataclasses import dataclass
from typing import Optional


@dataclass
class MinEvenNumberTestData:
    """Classwork task tests."""

    number: int
    answer: Optional[int]


@dataclass
class EuclidTestData:
    """GCD test data format."""

    val_a: int
    val_b: int
    answer: int


@dataclass
class FactorialTestData:
    """Factorial test data format."""

    number: int
    answer: int
