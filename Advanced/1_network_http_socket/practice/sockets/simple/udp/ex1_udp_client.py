import socket

# 1) ~~~~~~~~~~~~~~
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'Test message 1 from client', ('127.0.0.1', 8888))  #  если уже есть слущающий udp сокет, то он примет битовое сообщение