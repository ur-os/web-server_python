import re


def slice_request(string: str) -> list:
    return re.split(r'\r\n', string)


def get_string(string: str, row_number: int) -> str:
    return string[row_number]


def get_path(header_with_path) -> str:
    return re.split(r' ', header_with_path)[1]


def parse(request):
    pass