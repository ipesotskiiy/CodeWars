def digital_root(n):
    if len(str(n)) == 1:
        return n
    sum_numbers = 0
    for i in list(str(n)):
        sum_numbers += int(i)
    return digital_root(sum_numbers)