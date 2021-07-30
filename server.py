import socket
import utils
import parser

class Server:
    # Define socket host and port
    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = 3004

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pass

    def start(self):  # business logic
        while True:
            try:
                self.create_sever_socket()
                client_socket, client_address = self.server_socket.accept()
                self.send_response(client_socket, self.recieve_request(client_socket))
                self.server_socket.close()
            except Exception:
                print("shit happens, sorry :) remove after testing")

    def create_sever_socket(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.SERVER_HOST, self.SERVER_PORT))
        self.server_socket.listen(1)
        print('Listening on port %s ...' % self.SERVER_PORT)

    def recieve_request(self, client_socket) -> dict:
        request = client_socket.recv(1024).decode()

        slices = parser.slice_request(request)
        print(len(slices), type(slices), *slices, sep='\n')
        path = parser.get_path(slices[0])
        if utils.is_request_index(path):
            return {'request': request, 'code': None, 'content': path}

        if utils.is_backwards_path(path):
            return {'request': request, 'code': 403, 'content': path}

        return {'request': request, 'code': None, 'path': path}

    def send_response(self, client_socket, content: dict):
        try:
            response_head = 'HTTP/1.1 ' + content['code'] + ' OK\r\nContent-Type: \r\n Content-Length: \r\n\r\n'
            client_socket.send(response_head.encode())

            print(content['code'], content['path'], content['request'])
            with open('/home/urick0s/' + content['path'], 'rb') as file:
                client_socket.sendfile(file, 0)
        except FileNotFoundError:
            client_socket.send('Code: 404 request to non-exist file'.encode())

        client_socket.close()

# request structure {
#     request: str: ('GET /wiki/HTTP HTTP/1.0 Host: ru.wikipedia.org')
#     { -- sys info
#              path: str: 'www.youtube.com/channel/UCeJI8IUHpbtyezySM5VBkiw')
#              code: int: 200
#     }








