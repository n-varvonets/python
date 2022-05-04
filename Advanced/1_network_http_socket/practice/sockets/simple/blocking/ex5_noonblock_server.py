import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)
# sock.setblocking(True)
"""есть аналог блокирующего режима..."""
sock.settimeout(5)  # указываем сколько секунд блокирующая функция будет ожидать клиента, а если так и не подключится,
# то передать управление в дальше
# sock.settimeout(0) -> sock.setblocking(False)
# sock.settimeout(None) -> sock.setblocking(True)


try:
    client, addr = sock.accept()
except socket.error:
    print('No content')
# except socket.timeout:
#     print('timed out')

else:
    result = client.recv(1024)
    client.close()
    print('Message', result.decode('utf-8'))