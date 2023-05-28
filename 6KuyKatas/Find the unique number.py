def find_uniq(arr):
    set_arr = set(arr)
    for number in set_arr:
        if arr.count(number) == 1:
            return number