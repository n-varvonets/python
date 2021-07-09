import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)   # то кол-во кол--во сколько осединений с клиентов мы можем слушать для обменпа данными с ними

while True:
    try:
        client, addr = sock.accept()  # accept смотрит есть ли в очереди клиенты, которые установили с нами соединение и:
        # а) дастает его из очереди
        # б) если очередь пуста, то ждет его
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        result = client.recv(1024)
        client.close()
        print('Recieved message is....', result.decode('utf-8'))