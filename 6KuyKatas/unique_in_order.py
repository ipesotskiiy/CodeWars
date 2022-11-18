def unique_in_order(iterable: str) -> list[str, ...]:
    """
    This function removes identical elements next to each other and returns a list with the remaining elements.
    :param iterable: unconverted string
    :return: converted list
    """
    result_list: list = []
    for i in range(len(iterable)):
        if i == 0 or iterable[i] != iterable[i-1]:
            result_list.append(iterable[i])
    return result_list