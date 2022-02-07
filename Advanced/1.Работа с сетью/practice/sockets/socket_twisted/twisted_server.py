from twisted.internet import reactor, protocol, endpoints
from twisted.internet.protocol import connectionDone

# твистед - использует там где необходимо скорость без блокировки цикла событий
# в твистеде все очень удобно разбито на модульные единицы: протокол, фабрика и...
# возможность переопределить методы(создание/потеря соединение, принятие/ответ информации)


class ProcessClient(protocol.Protocol):
    """протокол - привила обработки сообщений при помощи которых мы общаемся с клиентом"""

    def __init__(self, server):
        self.server = server

    def connectionMade(self):
        print('Client connected...')
        self.server.concurrentClientCount += 1

    def connectionLost(self, reason=connectionDone):
        print('Client connected...')
        self.server.concurrentClientCount -= 1

    def dataReceived(self, data: str):
        data = data.strip()
        print('Data: ', data)
        self.transport.write(data)


class Server(protocol.Factory):
    """фабрика - генерирует наши протоколы на каждого нового клиента"""
    commands = ('init', 'send', 'get', 'close')

    def __init__(self):
        self.concurrentClientCount = 0
        self.database = {}

    def buildProtocol(self, addr):
        return ProcessClient(self)


server = endpoints.serverFromString(reactor, 'tcp:8888')  # таким способом создаем инстанс твистеда
server.listen(Server())
reactor.run()  # реактор - наш ИВЕНТЛУП


