from pydantic.main import BaseModel


class EuclidTestData(BaseModel):
    """GCD test data format."""

    val_a: int
    val_b: int
    answer: int


class FactorialTestData(BaseModel):
    """Factorial test data format."""

    number: int
    answer: int
