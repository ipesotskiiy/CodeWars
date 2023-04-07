def move_zeros(lst):
    for i in lst:
        if i == 0:
            a = i
            lst.remove(i)
            lst.append(i)
    return lst


test_list = move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])
print(test_list)
