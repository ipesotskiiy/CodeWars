def get_middle(s):
    if len(s) <= 2:
        return s
    if len(s) % 2 != 0:
        return s[int(len(s)/2 + 0.5)-1]
    return s[int(len(s)/2)-1: int(len(s)/2 + 1)]