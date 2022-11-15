def is_square(n):
    if n < 0:
        return False
    else:
        for i in range(n + 1):
            i2 = i * i
            if i2 == n:
                return True
            elif i2 > n:
                break

    return False