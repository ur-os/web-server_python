import socket
import utils


class Server:
    # Define socket host and port
    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = 8000

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pass

    def start(self):  # worker
        while True:
            self.create_sever_socket()
            client_socket, client_address = self.server_socket.accept()
            print(self.get_request(client_socket))
            self.send_response(client_socket)
            self.close_server_socket()

    def create_sever_socket(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.SERVER_HOST, self.SERVER_PORT))
        self.server_socket.listen(1)
        print('Listening on port %s ...' % self.SERVER_PORT)

    @staticmethod
    def get_request(client_connection):
        request = client_connection.recv(1024).decode()

        return request

    @staticmethod
    def send_response(client_socket):
        response_head = 'HTTP/1.1 200 OK\r\n Content-Type: image/jpg\r\n Content-Length: 740782\r\n\r\n'
        response_body = utils.get_file('/home/urick0s/Pictures/568edd37187323.573a47d0cb51f.jpg')

        client_socket.send(response_head.encode())
       #client_socket.send(response_body.encode())
        with open('/home/urick0s/Pictures/568edd37187323.573a47d0cb51f.jpg', 'rb') as f:
            client_socket.sendfile(f, 0)
        client_socket.close()

    def close_server_socket(self):
        # Close socket
        self.server_socket.close()
