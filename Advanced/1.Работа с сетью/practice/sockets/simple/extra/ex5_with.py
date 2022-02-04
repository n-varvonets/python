import socket

# __enter__/__exit__ -  оператор with  при входе и выходе вызывает эти функции, которые может обработать модуль socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    print('8888 is bind')
    sock.bind(('127.0.0.1', 8888))

    while True:
        result = sock.recv(1024)
        print('Message', result.decode('utf-8'))