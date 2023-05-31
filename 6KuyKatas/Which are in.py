def in_array(array1, array2):
    result = []
    for chars in array1:
        for word in array2:
            if chars in word and chars not in result:
                result.append(chars)
    return sorted(result)