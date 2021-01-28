from typing import List, Optional


def get_digits_from_num(number: int) -> List[int]:
    """
    Split number by digits.

    :param number: target number.
    :return: list of digits.
    """
    digits = []
    while number > 0:
        digits.append(number % 10)
        number = number // 10
    return digits


def is_even(num: int) -> bool:
    """
    Test if number is even.

    :param num: number to test.
    :return: True if number is even.
    """
    return num % 2 == 0


def min_even_digit(number: int) -> Optional[int]:
    """
    Нахождение минимальной четной цифры.

    На обработку поступает натуральное число, не превышающее 10**9.
    Нужно написать функцию, которая возвращает  минимальную чётную цифру этого числа.
    Если в числе нет чётных цифр, требуется вернуть None.

    :param number: число цифры которого надо обработать.
    :return: Минимальную цифру или None.
    """
    number = int(number)
    digits = get_digits_from_num(number)
    even_digits = list(filter(is_even, digits))
    if not even_digits:
        return None
    return min(even_digits)
