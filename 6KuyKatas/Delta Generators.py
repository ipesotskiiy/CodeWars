def delta(values, n):
    values_iter = iter(values)
    if n == 0:
        return values_iter
    else:
        return delta(diference(values_iter), n - 1)


def diference(values_iter):
    first = next(values_iter)
    while True:
        try:
            second = next(values_iter)
            yield second.__sub__(first)
            first = second
        except StopIteration:
            return