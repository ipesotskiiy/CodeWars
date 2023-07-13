def nb_year(p0, percent, aug, p):
    years = 0
    while True:
        p0 += (p0 * (percent/100)) + aug
        years += 1
        if p0 >= p:
            return years