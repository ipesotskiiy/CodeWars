def solution(s):
    character_pairs = []
    pair = ''

    if len(s) % 2 != 0:
        s += '_'

    for char in s:
        pair += char
        if len(pair) == 2:
            character_pairs.append(pair)
            pair = ''

    return character_pairs