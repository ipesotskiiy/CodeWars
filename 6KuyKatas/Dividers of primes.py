def get_dividers(values, powers):
    result_number = 1
    dividers = []
    for i in range(len(values)):
        result_number *= (values[i] ** powers[i])

    for number in range(1, result_number + 1):
        if result_number % number == 0:
            dividers.append(number)
    return dividers

