def generate_hashtag(s: str) -> str | bool:
    if len(s) == 0:
        return False
    result: str = '#'
    if s[0] == ' ':
        s: str = s.strip()
    list_with_words: list = s.split(' ')
    for i in list_with_words:
        result += i.capitalize()
    if len(result) > 140:
        return False
    return result
