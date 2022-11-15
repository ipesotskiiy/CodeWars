def to_camel_case(text: str) -> str:
    """
    This function converts a string according to camel case
    :param text: string to be converted
    :return: converted string
    """
    if len(text) == 0:
        return text
    string: str = text.replace('-', ' ').replace('_', ' ')
    list_string: list[str, ...] = string.split()
    return list_string[0] + ''.join(i.capitalize() for i in list_string[1:])
