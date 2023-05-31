def count_weight(s):
    return sum(int(c) for c in s), s


def order_weight(s):
    return ' '.join(sorted(s.split(' '), key=count_weight))

