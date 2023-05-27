def multiplication_table(size):
    result = []
    for i in range(1, size + 1):
        multiplying_a_number = []
        for j in range(1, size + 1):
            multiplying_a_number.append(i*j)
            if len(multiplying_a_number) == size:
                result.append(multiplying_a_number)
    return result
