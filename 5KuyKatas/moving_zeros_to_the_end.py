def move_zeros(lst: list) -> list:
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(i)
    return lst
