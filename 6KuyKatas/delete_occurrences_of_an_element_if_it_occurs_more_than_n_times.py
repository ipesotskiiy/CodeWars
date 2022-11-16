def delete_nth(order: list[int, ...], max_e: int) -> list[int, ...]:
    """
    This function removes unnecessary duplicates if their number is greater than max_e
    :param order: list to remove duplicates from
    :param max_e: maximum number of allowed duplicates
    :return: list with duplicates removed
    """
    new_order: list[int, ...] = []

    for i in order:
        if new_order.count(i) >= max_e:
            continue
        else:
            new_order.append(i)

    return new_order