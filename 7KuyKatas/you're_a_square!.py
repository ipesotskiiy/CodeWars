def is_square(n: int) -> bool:
    """
    This function checks if the given number is the square of another number.
    :param n: number to check
    :return: true if the number is the square of the number. false if the number is not a square
    """
    if n < 0:
        return False
    else:
        for i in range(n + 1):
            i2: int = i * i
            if i2 == n:
                return True
            elif i2 > n:
                break

    return False