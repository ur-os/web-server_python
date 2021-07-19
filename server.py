import socket
import utils
import parser

class Server:
    # Define socket host and port
    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = 8000
    last_path = ''

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pass

    def start(self):  # business logic
        while True:
            self.create_sever_socket()
            client_socket, client_address = self.server_socket.accept()
            print(self.recieve_request(client_socket))
            self.send_response(client_socket)
            self.close_server_socket()

    def create_sever_socket(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.SERVER_HOST, self.SERVER_PORT))
        self.server_socket.listen(1)
        print('Listening on port %s ...' % self.SERVER_PORT)

    def recieve_request(self, client_socket):
        request = client_socket.recv(1024).decode()
        slices = parser.slice_request(request)
        print(len(slices), type(slices), *slices, sep='\n')
        self.last_path = parser.get_path(slices[0])
        return request

    def send_response(self, client_socket):
        try:
            response_head = 'HTTP/1.1 200 OK\r\nContent-Type: \r\n Content-Length: \r\n\r\n'
            client_socket.send(response_head.encode())
            with open('/home/urick0s/' + self.last_path, 'rb') as file:
                client_socket.sendfile(file, 0)
        except FileNotFoundError:
            client_socket.send('HTTP/1.1 404 OK\r\n Content-Type: text/html\r\n\r\n'.encode())
            client_socket.send('Code: 404 request to non-exist file'.encode())
        client_socket.close()

    def close_server_socket(self):
        self.server_socket.close()
