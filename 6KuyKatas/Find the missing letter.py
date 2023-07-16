def find_missing_letter(chars):
    alp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ind = alp.find(chars[0])
    need_alp = alp[ind:ind+len(chars)+1]
    for i in need_alp:
        if i not in chars:
            return i