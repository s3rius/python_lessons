from math import gcd
from typing import List


def nok(val_a: int, val_b: int) -> int:
    """
    Подсчет значения НОК.

    Используя формулу НОК (м,н) = (м*н)/НОД (м,н).
    Высчитывает общий занаменатель.

    :param val_a: 1 аргумент
    :param val_b: 2 аргумент
    :return: НОК
    """

    return (val_a * val_b) // gcd(val_a, val_b)


def sum_fractions(val_a: str, val_b: str) -> str:
    """
    Sum two fraction numbers.

    This function is used to sum two fractions represented as strings.
    The format is the following: "23/44". In other words numerator and denominator
    are splitted by the '/' sign.

    :param val_a: first fraction.
    :param val_b: second fraction.
    :return: sum result in string format like "a/b".
    """
    num1, denum1 = val_a.split("/")
    num2, denum2 = val_b.split("/")

    denum = nok(int(denum1), int(denum2))
    num1 = (denum // int(denum1)) * int(num1)
    num2 = (denum // int(denum2)) * int(num2)
    num = num1 + num2
    return str(num) + "/" + str(denum)


def find_fibonacci_in_list(input_list: List[int]) -> List[int]:
    """
    Find Fibonacci sequence in list.

    Create a program that will dissect all the elements that make up the
    Fibonacci sequence and located in the input list in a given order.

    Fibonacci numbers are elements of a numerical sequence,
    the first two numbers of which are equal to 0 and 1,
    and each subsequent one is the sum of the previous two.

    Start of sequence: 0, 1, 1, 2, 3, 5 ...

    :param input_list: input list. Each number of the list is lower than 10.
    :return: found sequence.
    """
    return []  # Your code goes here.
