import os
import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM - это tcp соеденинение, AF_INET - по айпи
sock.connect(('', 8888))  # конектится к локалхосту и указываем на какой порт отправить - 8888
sock.send(b'Just a message uwllbhckd -  take it as a nickname for yourself - let them break their tongue')

#  в данном случае ожидаем что бы сервер отправил нам смс
result_of_server_msg = sock.recv(64)
print(f'Response from server is.. :{result_of_server_msg.decode("utf-8")}')
sock.close()