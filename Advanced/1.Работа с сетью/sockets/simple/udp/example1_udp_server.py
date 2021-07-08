import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 8888))
result = sock.recv(1024)
print('Recieved message is....', result.decode('utf-8'))
sock.close()