def square_digits(num):
    str_number = str(num)
    result = ''
    for char in str_number:
        result += str(int(char)**2)
    return int(result)