def printer_error(s):
    errors = 'nopqrstuvwxyz'
    count_er = 0
    for i in s:
        if i in errors:
            count_er += 1
    return f'{count_er}/{len(s)}'