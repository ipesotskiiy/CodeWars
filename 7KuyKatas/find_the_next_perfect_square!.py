import math


def find_next_square(sq: int) -> int:
    """
    This function finds the square of the next number
    :param sq: the square of the number that is one less than the number whose square is to be found
    :return: the square of the next number, or -1 if the given number was not the square of an integer
    """
    sqrt_sq: float = math.sqrt(sq)
    if sqrt_sq.is_integer():
        sqrt_sq: int = int(sqrt_sq)
        next_sq: int = (sqrt_sq + 1) ** 2
        return next_sq

    return -1
