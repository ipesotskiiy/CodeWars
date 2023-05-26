def to_acronym(inp):
    words = inp.split()
    result = ''
    for word in words:
        result += word[0].upper()
    return result