def chain(value, functions):
    for f in functions:
        value = f(value)
    return value