def count_smileys(arr):
    if len(arr) == 0:
        return 0
    count_smileys = 0
    for smiley in arr:
        if len(smiley) == 2 and (':' in smiley or ';' in smiley) and (')' in smiley or 'D' in smiley):
            count_smileys += 1
        elif len(smiley) == 3 and (':' in smiley or ';' in smiley) and (')' in smiley or 'D' in smiley) \
                and ('-' in smiley or '~' in smiley):
            count_smileys += 1
    return count_smileys