def dig_pow(n, p):
    num = str(n)
    sum_numbers = sum([int(num[i]) ** (p+i) for i in range(len(num))])
    return sum_numbers/n if sum_numbers % n == 0 else -1