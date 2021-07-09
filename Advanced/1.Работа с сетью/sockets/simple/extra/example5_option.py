import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 255.255.255.255 - это широквещательный канал, что бы наше сообщение приходило на каждого клиента
sock.bind(('127.0.0.1', 8888))
sock.listen(5)

"""что бы отправлять такие сообщение, то нам необходимо использовать специальную опцию  бродкаст"""
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

"""так же бывают ситуации, когда мы зарезервировали наш порт, потом отправили датугарму, потом закрыли,НО...
есть 'какое-то определенное время', что прочитать из БУФЕРА эти смс, отправить их и в уже в действительности закрыть
соеденение. И в этот момент питон может блокировать буфер и не дать доиспользовать данные, тем самым закрыв порт оставив
в нем дату и не дать дргому клиенту подключиться"""
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    client, addr = sock.accept()
except socket.error:
    print('no connection')
else:
    result = client.recv(1024)
    client.close()
    print('Recieved message is....', result.decode('utf-8'))