def high_and_low(numbers):
    numbers_list = []
    for str_num in numbers.split():
        numbers_list.append(int(str_num))
    return f'{max(numbers_list)} {min(numbers_list)}'