from dataclasses import dataclass
from typing import List


@dataclass
class SumFractionsTestData:
    """Test data for sum_fractions function."""

    first: str
    second: str
    answer: float


@dataclass
class FibonacciFinderTestData:
    """Test data for find_fibonacci_in_list function."""

    sequence: List[int]
    answer: List[int]


@dataclass
class MatrixOperationTestData:
    """Test data for matrix operations functions."""

    first: List[List[int]]
    second: List[List[int]]
    answer: List[List[int]]
