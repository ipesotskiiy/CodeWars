def solution(s: str) -> str:
    """
    This function converts a camel-style string by adding a space between words
    :param s: string to be converted
    :return: converted string
    """
    return ''.join([' ' + c if c.isupper() else c for c in s])