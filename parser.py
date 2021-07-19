import re


def slice_request(string) -> list:
    return re.split(r'\r\n', string)


def get_string(string, row_number):
    return string[row_number]


def get_path(header_with_path) -> str:
    return re.split(r' ', header_with_path)[1]


def parse(request):
    pass