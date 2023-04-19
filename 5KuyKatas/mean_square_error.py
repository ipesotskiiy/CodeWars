def solution(array_a: list, array_b: list) -> int:
    result_array: list = []
    for i, j in zip(array_a, array_b):
        if i > j:
            result_array.append((abs(i-j))**2)
        elif j > i:
            result_array.append((abs(j-i))**2)
        elif i == j:
            result_array.append(0)
    result_int: int = sum(result_array)/len(result_array)
    return result_int


b1 = [10, 20, 10, 2]
b2 = [10, 25, 5, -2]

test = solution(b1, b2)