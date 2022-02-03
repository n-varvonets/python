import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 8888))

# в отличие от простого соединения мы хотим сделать так что бы сервер постоянно слушал сколько угодно..ю
# подключений без перерыва(т.е. без выхода из цикла прослушанивания)

while True:
    try:
        result = sock.recv(1024)
    except KeyboardInterrupt:  # выйти из цикла и закрыть порт можно будет при ctl+c - keyboard
        sock.close()
        break
    else:
        print('Received message "in loop" from udp client is ...', result.decode('utf-8'))
