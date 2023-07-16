def is_triangle(a, b, c):
    if c >= (a + b) or b >= (c + a) or a >= (b + c):
        return False
    return True