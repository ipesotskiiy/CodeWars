import re


def alphanumeric(password: str) -> bool:
    if len(password) > 0 and re.fullmatch(r'[a-zA-Z0-9]+', password):
        return True
    else:
        return False