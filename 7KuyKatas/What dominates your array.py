def dominator(arr):
    for x in set(arr):
        if arr.count(x) > len(arr)/2.0:
            return x
    return -1
