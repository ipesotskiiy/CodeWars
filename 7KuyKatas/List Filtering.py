def filter_list(l):
    'return a new list with the strings filtered out'
    return [i for i in l if isinstance(i, int)]