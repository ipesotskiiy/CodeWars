def find_outlier(integers):
    evens = []
    not_evens = []
    for i in integers:
        if i % 2 == 0:
            evens.append(i)
        else:
            not_evens.append(i)
    if len(evens) == 1:
        return evens[0]
    else:
        return not_evens[0]