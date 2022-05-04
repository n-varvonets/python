import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))

sock.listen(5)  # устанавливаем размер очереди
sock.setblocking(False)  # False не блокирующий режим, если будет false и по умолчанию True (блокирующий)

"""в данном примере обрабатываем исключение с блоком"""
while True:
    try:
        client, addr = sock.accept()
    except socket.error:  # socket.error - возникает в случае отсутствия каких-либо клиентов при неблокирующем режиме
        """успешно обрабатывает ошибку выводя в принт сообщение что нет клиента, но как только подключится..."""
        print('no clients')
    except KeyboardInterrupt:
        break
    else:
        """как только поступил запрос, то в блокирующем режиме я хочу с клиентом общаться"""
        client.setblocking(True)
        result = client.recv(1024)
        client.close()

        print('Message from client is ... ', result.decode('utf-8'))

