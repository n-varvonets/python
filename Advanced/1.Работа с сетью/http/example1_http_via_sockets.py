import socket

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
print(result.decode())