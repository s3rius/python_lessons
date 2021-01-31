from dataclasses import dataclass
from typing import List


@dataclass
class SumFractionsTestData:
    """Test data for sum_fractions function."""

    first: str
    second: str
    answer: str


@dataclass
class FibonacciFinderTestData:
    """Test data for find_fibonacci_in_list function."""

    sequence: List[int]
    answer: List[int]


@dataclass
class DecimalToBinary:
    """Test data for computer translator."""

    thought: int
    message: str


@dataclass
class HammingDistance:
    """Test data for hamming_distance."""

    first_dna: str
    second_dna: str
    distance: int
