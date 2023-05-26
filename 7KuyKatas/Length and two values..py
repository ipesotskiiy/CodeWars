def alternate(n, first_value, second_value):
    result = []

    while len(result) != n:
        if n - len(result) == 1:
            result.append(first_value)
        else:
            result.append(first_value)
            result.append(second_value)

    return result