import socketserver


class EchoUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).strip()
        print(f'Addres: {self.client_address[0]}')  # >>> Addres: 127.0.0.1
        print(f'Data: {data.decode()}')  # >>> Data: Test ms2g
        self.request.sendall(b'sq', b'ww')  # и как пример.. отправляем назад ему полученные данные  о нем


if __name__ == '__main__':
    with socketserver.TCPServer(('', 8888), EchoUDPHandler) as server:
        server.serve_forever()