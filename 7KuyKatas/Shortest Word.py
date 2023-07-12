def find_short(s):
    words = s.split()
    min_len = len(words[0])
    for word in words[1:]:
        word_len = len(word)
        if word_len < min_len:
            min_len = word_len

    return min_len