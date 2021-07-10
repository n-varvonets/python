import socketserver


class EchoUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data, socket = self.request  # sokcet - тот адресс откуда подключается(отправляет пользовательскую датуграму) клиент
        print(f'Addres: {self.client_address[0]}')  # >>> Addres: 127.0.0.1
        print(f'Data: {data.decode()}')  # >>> Data: Test ms2g
        socket.sendto(data, self.client_address)  # и как пример.. отправляем назад ему полученные данные  о нем


if __name__ == '__main__':
    with socketserver.UDPServer(('0', 8888), EchoUDPHandler) as server:
        server.serve_forever()