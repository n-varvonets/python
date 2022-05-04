import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('example.com', 80))
# следующей строкой мы собираем заголовки
content_items = [
    'GET / HTTP/1.1',
    'Host: example.com',
    'Connection: keep-alive',
    'Accept: text/html',
    '\n'
]  # пока массиовм, но наиже срокой склеиваем в одну строку + '\n' - это в конце по стандарту
content = '\n'.join(content_items)
print('~~~ http message. start ~~~')
print(content)
print('~~~ http message. end ~~~')

"""т.к. это метод тсп и мы уже установили соединение, то через метод сенд отправляем запрос"""
sock.send(content.encode())  # отправляем наш заголовок предварительно переводя его в байт код
result = sock.recv(10024)
print(result.decode())  # дальше вывдим наш ответ от сервера переводя байт в строку
