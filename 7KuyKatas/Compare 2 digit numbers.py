def compare(a, b):
    fir = sorted(str(a))
    sec = sorted(str(b))
    return '100%' if fir == sec else '50%' if fir[0] in sec or fir[1] in sec else '0%'


