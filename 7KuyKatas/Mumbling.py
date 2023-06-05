def accum(s):
    result = []
    step = 0
    for char in s:
        result.append(char.upper() + char.lower() * step)
        step += 1
    return '-'.join(result)