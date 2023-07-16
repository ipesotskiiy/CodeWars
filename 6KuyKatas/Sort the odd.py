def sort_array(source_array):
    odds = iter(sorted(number for number in source_array if number % 2))
    return [next(odds) if number % 2 else number for number in source_array]
