import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 255.255.255.255 - широковещательный канал для всех пользователей
sock.bind(('127.0.0.1', 8888))
sock.listen(5)
# если мы хотим отправить сообщение для всех клиентов которые прослушивают наш сокет
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# если мы хотим переиспользовать адрес в случае когда после закрытия сокета ос не успевает закрыть адрес и что бы
# предотвратить блок функцию - этим методом разрешаем переюзывать наш порт
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)