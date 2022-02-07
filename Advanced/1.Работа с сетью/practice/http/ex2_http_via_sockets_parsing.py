import socket


def parse_http_response(text_response):
    lines = text_response.split('\n')
    status_raw, lines = lines[0], lines[1:]  # status_raw = lines[0] = HTTP/1.1 200 OK
    protocol, status_code, message = status_raw.split(' ')  # ['HTTP/1.1', '200', 'OK\r']
    empty_index = 1
    headers = {}
    for index, line in enumerate(lines):
        line = line.strip()
        line = line.strip('\r')
        if line == '':
            empty_index = index
            break
        k, _, v = line.partition(':')  #  из строки line('Accept-Ranges: bytes') делаем тюпл(('Accept-Ranges', ':', ' bytes'))
        headers.setdefault(k.strip(), v.strip())  #  таким образом добавляем наши заголвоки в хедерс
    content = ''.join(lines[empty_index + 1:])  # берем остальной контент(атррс без хедоров) прикольная конструкция котрая позволяет взять срез
    return int(status_code), headers, content


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
sock.send(content.encode())  # отправляем наш заголовок предварительно переводя его в байт код
result = sock.recv(10024)
print(result.decode())
status_code, headers, content = parse_http_response(result.decode())