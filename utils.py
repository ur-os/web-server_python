def get_file(path):
    with open(path, 'rb') as file:
        data = file.read()
        print(str(data))
        return str(data)

def request_parse(string_req):
    struct_req = {}
    #struct_req['head'] = struct_req[]