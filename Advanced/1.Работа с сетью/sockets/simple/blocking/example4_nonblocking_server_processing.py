import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)  # устанавливем размер очереди
sock.setblocking(False)  # в данном примере устанавливаем неблокирующий режим перед методом accacpt

while True:
    try:
        client, addr = sock.accept()
    except socket.error:
        print('no clients')  # постоянно будет печатать что нет клиентов, когда никто к нам не подлючится, но кттс, то..
    except KeyboardInterrupt:
        break
    else:  # ... попадаем в ветку  else
        sock.setblocking(True)   # установили блокирующий режим, что бы в этом режими обмениваться данными
        result = client.recv(1024)
        client.close()
        print('Recieved message is....', result.decode('utf-8'))