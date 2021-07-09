import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)  # устанавливем размер очереди
# sock.setblocking(True)  # в этом моменту ждем клиента и не пускаем дальше если очередь пуста. режим true по умолчанию стоит
sock.setblocking(False)  #  в случае отсутвия клиент а очереди - мы будем полчать исключение "BlockingIOError: [Errno 11] Resource temporarily unavailable"

client, addr = sock.accept()
result = client.recv(1024)
client.close()

print('Recieved message is....', result.decode('utf-8'))
