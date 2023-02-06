def to_weird_case(words):
    i = 0
    new_string = ''
    for j in words:
        if i % 2 == 0:
            new_string += j.upper()
        else:
            new_string += j.lower()

        if j == ' ':
            i = 0
        else:
            i += 1
    return new_string