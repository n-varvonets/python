import socketserver


class EchoTCPHandler(socketserver.BaseRequestHandler):
    """тот же класс, что и в юдп, но риквест по другом принимаем"""

    def handle(self):

        data = self.request.recv(1024).strip()
        print(f'Address: {self.client_address[0]}')
        print(f'Data:  {data.decode()}')
        self.request.sendall(data)  # а стороне клиента, после отправки, так же можно принять сообщения с сервера


if __name__ == '__main__':
    """уже только ТСПсервер"""
    with socketserver.TCPServer(('', 8888), EchoTCPHandler) as server:
        server.serve_forever()
