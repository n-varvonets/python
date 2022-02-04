import socketserver


class EchoUDPHandler(socketserver.BaseRequestHandler):
    """тот же класс, что и в юдп, но риквест по другом принимаем"""

    def handle(self):

        data, socket = self.request.recv(1024).strip()
        print(f'Address: {self.client_address[0]}')
        print(f'Data:  {data.decode("utf-8")}')
        socket.sendto(data, self.client_address)  # а стороне клиента, после отправки, так же можно принять сообщения с сервера


if __name__ == '__main__':
    """уже только ТСПсервер"""
    with socketserver.TCPServer(('', 8888), EchoUDPHandler) as server:
        server.serve_forever()
