def narcissistic(value):
    str_value = str(value)
    result = 0
    for i in str_value:
        result += int(i) ** len(str_value)
    if result == value:
        return True
    else:
        return False