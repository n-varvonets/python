import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('', 8888))
sock.send(b'Test msg1')

recv_msg_frm_sckt_srvr = sock.recv(64)
print('Msg from server is...', recv_msg_frm_sckt_srvr)
sock.close()