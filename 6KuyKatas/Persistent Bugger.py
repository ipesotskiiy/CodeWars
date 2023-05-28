def persistence(n, count=0):
    if len(str(n)) == 1:
        return count
    result = 1
    for i in str(n):
        result *= int(i)
    count += 1
    return persistence(result, count)
