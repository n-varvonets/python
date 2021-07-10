import socketserver


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """ThreadingMixIn - распаралеливает обработку наших клиентов """
    pass


class EchoUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).strip()
        print(f'Addres: {self.client_address[0]}')
        print(f'Data: {data.decode()}')
        self.request.sendall(data)

if __name__ == '__main__':
    with ThreadingTCPServer(('', 8888), EchoUDPHandler) as server:
        server.serve_forever()