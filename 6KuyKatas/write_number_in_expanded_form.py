def duplicate_encode(word: str) -> str:
    """
    This function converts a string in such a way that if there is no duplicate character in the function, the sign ( ,
    otherwise )
    :param word: string to be converted
    :return: converted string
    """
    word: list[str, ...] = list(word.lower())
    new_word: str = ''
    for i in range(len(word)):
        if word.count(word[i]) > 1:
            new_word += ')'
        elif word.count(word[i]) == 1:
            new_word += '('
    return new_word
