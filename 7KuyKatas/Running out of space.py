def spacey(array):
    result_array = []
    element = 0
    while len(result_array) != len(array):
        if not result_array:
            result_array.append(array[element])
        else:
            result_array.append(result_array[element-1] + array[element])
        element += 1


    return result_array

