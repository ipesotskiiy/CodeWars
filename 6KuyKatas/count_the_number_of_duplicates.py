def duplicate_count(text: str) -> int:
    """
    function to count characters having duplicates

    :param text: line inside which you want to count duplicates
    :return: number of characters with duplicates
    """
    text: str = text.lower()
    chars: dict[str:int] = {char: text.count(char) for char in text}
    return len([char for char in chars if chars[char] >= 2])
