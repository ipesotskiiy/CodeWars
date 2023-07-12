def find_even_index(arr):
    for i in range(len(arr)):
        left_sum = sum(arr[:i+1])
        right_sum = sum(arr[i:])
        if left_sum == right_sum:
            return i
    return -1