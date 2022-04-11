import socket
import selectors

to_monitor = []

# 1)определение серверного сокета оставлю в глобальной области видимости
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

""" ~~~ 1.) Пример синхронного кода из пред примера из файла #1 ~~~ """
# def accept_connection(server_socket):
#     """Принятие соединения клиента"""
#     while True:
#         client_socket, addr = server_socket.accept()
#
#         send_message(client_socket)
#
#
# def send_message(client_socket):
#     while True:
#         print('Before recv()')
#         request = client_socket.recv(4096)
#         if not request:
#             break
#         else:
#             response = 'Hello world\n'.encode()
#             client_socket.send(response)
#
#     client_socket.close()
#
#
# if __name__ == '__main__':
#     accept_connection(server_socket)

""" ~~~ 2.) Пример асинхронного кода ~~~ """
# Для этого нужно разбить атомарность функций, сделать их несвязанными(убрать вызов одной функции из другой). \
# Т.е. сделать механизм, который будет вызывать их по отдельность передав в них нужные сокеты - event loop.

from select import select


to_monitor = []  # изначально он будет пустым, но передадим в него \
# наши read объекты(server_socket.accept(), client_socket.recv(4096))


def accept_connection(server_socket):
    """Принятие соединения клиента, а именно:
    - дождаться СОБЫТИЯ когда во входящем буфере появятся данные о новом подключении by accept method """
    # while True: *** уже без надобности - потому что в event loop используем цикл

    client_socket, addr = server_socket.accept()

    # send_message(client_socket) *** убрав ЭТУ строку кода мы разбили атомрность функций - тем самым позволили \
    # написать код в асинхронном стиле

    #  и теперь в нашу очередь для мониторинга мы должны добавить клиентский сокет
    to_monitor.append(client_socket)  # как только мы добавили элемент, то select - это увидел, т.е - run event_loop


def send_message(client_socket):
    """Принятия событий:
    - а) когда СОБЫТИЕ клиент нам написал
    - б) когда СОБЫТИЕ отправилось смс клиенту, тем самым очистив кеш события recv, сделав его активным для чтения"""
    # while True:  *** уже без надобности
    print('Before recv()')
    request = client_socket.recv(4096)

    if request:  # если есть запрос, то отправляем смс
        response = 'Hello world\n'.encode()
        client_socket.send(response)
    else:  # в ином случае закрываем подключении и передаем дальше управление, тем самым освобождая элемент для "read"
        client_socket.close()


def event_loop():
    """Event loop - это механизм переключения наших функций между собой"""

    while True:
        """
        ВОПРОС: как нам узнать когда серверный или клиентский сокет готов для чтения или записи?
        РШЕНИЕ: функция select - мониторит состояние изменение файловых объектов и сокетов.
        Add info: в unix файлом является все - usb, socket, сам файл(.ру как этот к примеру), бд, видеокарты и т.д. \
        Каждый запущенный процесс - это тоже файл. Когда мы вызываем у серверного сокета bind - создается сокет, т.е. \
        создается файл. select  работает со всеми объектами у которого есть .fileno(), который возвращает \
        "файловый дескриптор"(простыми словами - id/номер/ссылка_на_файловый_объект файла в ОС)
        """
        # На ВХОД функция select получает 3 списка(list):  # (за изменением состояние, которых мы будем следить)
        #     - read: объекты, которые станут доступны для ЧТЕНИЯ.
        #     - write: объекты, которыми станут доступны для ЗАПИСИ.
        #     - err: объекты от которых мы ожидаем какие-либо ошибки.
        # На ВЫХОД она возвращает те же списка/объекты, НО после того как они станут ДОСТУПНЫ.

        ready_to_read, _, _ = select(to_monitor, [], [])  # 1) объекты 2(для записи) и 3(ошибки) в данном примере \
        # нам не нужны. 2) в select нужно передать объекты, за которыми нужно мониторить, поэтому в глобал скоп \
        # создадим этот объект.

        # Дальше как только появился клиент(server_socket) или клиент что-то написал(client_socket), то селект \
        # это увидел и обновил наши переменные(ready_to_read, _, _)
        for sock in ready_to_read:
            if sock is server_socket:  # тупая проверка на тип сокета
                accept_connection(sock)
            else:  # а если не серверный сокет, то вызываем клиент
                send_message(sock)


if __name__ == '__main__':
    to_monitor.append(server_socket)
    # accept_connection(server_socket) *** этот метод в асинхронном коде не нужен
    event_loop()
