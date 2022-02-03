import socket

# 1) ~~~~~все тоже самое что и в первом примере, но только сейчас указываем файл на который стучаться по битам~~~~~~~~~
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
sock.sendto(b'Test message 1 from client', 'unix.sock')  #  если уже есть слущающий udp сокет, то он примет битовое сообщение