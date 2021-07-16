import re


class Parser:
    request = ''

    def setup_request(self, string):
        self.request = re.split('r\n\r', string)
        print(self.request)

    @staticmethod
    def get_path(string):
        return re.search(r'', string)

    def get_string(self, string_number):
        return self.request[string_number]

    def parse(self, request):
        pass