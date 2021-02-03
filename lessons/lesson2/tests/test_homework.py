import pytest

from lessons.lesson2.homework import dec_to_binary, hamming_distance
from lessons.lesson2.tests.models import DecimalToBinary, HammingDistance

decimal_to_bin_data = [
    DecimalToBinary(thought=5, message="101"),
    DecimalToBinary(thought=32, message="100000"),
    DecimalToBinary(thought=405, message="110010101"),
    DecimalToBinary(thought=10889, message="10101010001001")
]

hamming_data = [
    HammingDistance(
        first_dna="GAGCCTACTAACGGGAT",
        second_dna="CATCGTAATGACGGCCT",
        distance=7
    ),
    HammingDistance(
        first_dna="GACC",
        second_dna="GCACCT",
        distance=4
    )
]


@pytest.mark.parametrize("test_data", decimal_to_bin_data)
def test_decimal_to_bin(test_data: DecimalToBinary):
    """Test function."""
    message = dec_to_binary(test_data.thought)
    assert message == test_data.message


@pytest.mark.parametrize("test_data", hamming_data)
def test_hamming_distance(test_data: HammingDistance):
    """Test function."""
    distance = hamming_distance(test_data.first_dna, test_data.second_dna)
    assert distance == test_data.distance
