import re


def is_backwards_path(string: str) -> bool:
    dots = re.search(r'\.\.\\', string)
    minuses = re.search(r'-\\', string)
    if dots is None and minuses is None:
        return False
    return True


def is_request_index(path: str) -> bool:
    if re.split(r'\.', path) is None:
        return True
    return False