import socketserver  # socketserver - набор классов, который позволяет в ооп стиле сделать сервер


class EchoUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # request содержит данные и сокет-клиент для коммуникации
        data, socket = self.request
        print(f'Address: {self.client_address[0]}')
        print(f'Data:  {data.decode("utf-8")}')
        socket.sendto(data, self.client_address)  # отправляем обратно клиенту ответ с датограммой, в случае есил он ожидает получить ответ(это не обьязательно)


if __name__ == '__main__':
    # используем оператор with для создания сервера на 0:8888 и запускаем
    # with гарантирует освобождение порта и корректное завершение работы
    # сервера- у класса реализован `__enter__` / `__exit__`.
    with socketserver.UDPServer(('0', 8888), EchoUDPHandler) as server:
        server.serve_forever()  # позволяет запустить сервер с ожиданием запросов от клиента
