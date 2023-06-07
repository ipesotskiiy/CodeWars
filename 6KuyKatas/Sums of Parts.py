def parts_sums(ls):
    sums = sum(ls)
    if not ls:
        return [0]
    result = []
    for i in range(len(ls)):
        result.append(sums)
        sums -= ls[i]
    result.append(0)
    return result