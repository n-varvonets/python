import socket

def parse_http_response(text_response):
    lines = text_response.split('\n')  # разбиваем по переносу строки
    status_raw, lines = lines[0], lines[1:]
    protocol, status_code, message = status_raw.split(' ') # еще раз делим status_raw('HTTP/1.1 200 OK)'
    empty_index =1
    headers = {}
    for index, line in enumerate(lines):
        line = line.strip()
        line = line.strip('\r')
        if line == "":
            empty_index = index
            break
        print(line)
        k, _, v = line.partition(":")
        headers.setdefault(k.strip(), v.strip())

    content = ''.join(lines[empty_index + 1:])
    return int(status_code), headers, content



sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('example.com', 80))
content_items = [
    'GET / HTTP/1.1',
    'Host: example.com',
    'Connection: keep-alive',
    'Accept: text/html',
    '\n'
]
content = '\n'.join(content_items)
print('---HTTP MESSAGE---')
print(content)
print('---END MESSAGE---')
sock.send(content.encode())
result = sock.recv(1024)

status_code, headers, content = parse_http_response(result.decode())
print('Status Code: {}'.format(status_code))
print('Headers: {}'.format(headers))
print('Content:')
print(content)
