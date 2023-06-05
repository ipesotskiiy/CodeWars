def positive_sum(arr):
    sum_numbers = 0
    for number in arr:
        if number > 0:
            sum_numbers += number
    return sum_numbers