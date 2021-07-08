import socket
import os

unix_sock_name = 'unix.sock'
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

# проверяем если файл уже существует, то удаляем его
if os.path.exists(unix_sock_name):
    os.remove(unix_sock_name)

sock.bind(unix_sock_name)

while True:
    try:
        result = sock.recv(1024)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print('Recieved message is....', result.decode('utf-8'))
