"""рассмотрим пример, который позволяет нам расспаралелить работу наших клиентов"""

import socketserver


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """ThreadingMixIn - создает клиента на каждого нового клиента и обрабатывает его в отдельном потоке"""
    pass


class EchoTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).strip()
        print(f"Address from thread server: {self.client_address[0]}")
        print(f"Data form client: {data.decode()}")
        self.request.sendall(data)


if __name__ == "__main__":
    with ThreadingTCPServer(('', 8888), EchoTCPHandler) as server:
        server.serve_forever()
