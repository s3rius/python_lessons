import pytest

from lessons.lesson2.homework import matrix_addition, matrix_multiplication
from lessons.lesson2.tests.models import MatrixOperationTestData

matrix_addition_test_data = []

matrix_multiplication_test_data = []


@pytest.mark.parametrize("test_data", matrix_addition_test_data)
def test_matrix_addition(test_data: MatrixOperationTestData):
    """Tests that matrix_addition is written good."""
    answer = matrix_addition(matrix_a=test_data.first, matrix_b=test_data.second)
    assert answer == test_data.answer


@pytest.mark.parametrize("test_data", matrix_addition_test_data)
def test_matrix_multiplication(test_data: MatrixOperationTestData):
    """Tests that matrix_multiplication is written good."""
    answer = matrix_multiplication(matrix_a=test_data.first, matrix_b=test_data.second)
    assert answer == test_data.answer
