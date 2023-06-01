def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return f'{hours:0>2}:{minutes:0>2}:{remaining_seconds:0>2}'
