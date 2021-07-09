import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)
sock.setblocking(True)  # но так же есть замена блокирующего элемента...
sock.settimeout(5)  # если в течении 5ти сек к нам никто не подлючится, то попадем в ветку  except
# sock.settimeout(0)  --> sock.setblocking(False)
# sock.settimeout(None) --> sock.setblocking(True)

try:
    client, addr = sock.accept()
except socket.error:
    print('no connection')
else:
    result = client.recv(1024)
    client.close()
    print('Recieved message is....', result.decode('utf-8'))