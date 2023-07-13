def tribonacci(signature, n):
    if n == 0:
        return []

    result = []

    if 0 < n < 3:
        for i in range(n):
            result.append(signature[i])

    elif n >= 3:
        result = signature

    for index in range(2, n - 1):
        next_element = result[index] + result[index - 1] + result[index - 2]
        result.append(next_element)
    return result