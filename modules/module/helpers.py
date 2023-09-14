from typing import TypeVar

T = TypeVar("T", int, float)


def sum(num1: T, num2: T) -> T:
    return num1 + num2


def diff(num1: T, num2: T) -> T:
    return num1 - num2


def product(num1: T, num2: T) -> T:
    return num1 * num2
