def is_prime(num):
    if num <= 1:
        return False
    delimiter = 2
    while delimiter * delimiter <= num and num % delimiter != 0:
        delimiter += 1
    return delimiter * delimiter > num