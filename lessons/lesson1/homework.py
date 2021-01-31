def euclid(val_a: int, val_b: int) -> int:
    """
    Первое задание.

    Функция вычисления наибольшего общего делителя двух целых чисел
    по алгоритму Евклида.
    В случае, если НОД найти нельзя возвращает None.

    :param val_a: первое число больше нуля.
    :param val_b: второе число больше нуля.
    :return: НОД чисел a и b.
    """
    while val_a > 0 and val_b > 0:
        if val_a > val_b:
            val_a %= val_b
        else:
            val_b %= val_a

    return val_a + val_b


def factorial(number: int) -> int:
    """
    Второе задание.

    Функция вычисления факториала числа.

    :param number: число больше или равное нулю.
    :return: факториал числа a.
    """
    fact = 1
    while number >= 1:
        fact *= number
        number -= 1
    return fact
