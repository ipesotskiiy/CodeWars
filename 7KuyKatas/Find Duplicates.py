def duplicates(array):
    seen = []
    dups = []
    for char in array:
        if char not in seen:
            seen.append(char)
        elif char not in dups:
            dups.append(char)

    return dups

