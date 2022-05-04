import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))

sock.listen(5)  # устанавливаем размер очереди
sock.setblocking(False)  # False не блокирующий режим, если будет false и по умолчанию True (блокирующий)

"""что изменилось с  False -  не блокирующем элементом
в случае отсутствия клиента - будет кидаться ошибка, что никто из клиентов к нам не подключился - это удобно, потому
что мы можем обработать данное исключение как будет показано в следующем примере"""
client, addr = sock.accept()

result = client.recv(1024)
client.close()

print('Message from client is ... ', result.decode('utf-8'))

