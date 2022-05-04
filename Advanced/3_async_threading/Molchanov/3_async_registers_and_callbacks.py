import socket
# from select import select
import selectors  # более абстрактная модуль над select


# что бы посмотреть какая функция selector умолчанию в нашей ОС в терминале след:
# /PycharmProjects/python$ python
# >>> import selectors
# >>> selectors.DefaultSelector()
# <selectors.EpollSelector object at 0x7fe2ce073978>   - т.е. Epoll - селектор по умолчания длс ОС  ubuntu

# получаю дефолтный селектор ОС в переменную + убрал to_monitor
selector = selectors.DefaultSelector()


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    # нужно зарегистрировать наш селектор.. он принимает:
    # 1. файловый обьект - тот у которого есть метод fileno()
    # 2. ивенты - то событие, которое нас интересует
    # 3. дата - любые связанные данные(сессии, обьект функции(не вызов))
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)


def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()

    # так же как и выше реистрируе уже для отслежки - клиентский сокет
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)


def send_message(client_socket):

    # в сенд_меседж происходит закрытие сокета client_socket.close() и прежде чем мы его закроем - его нужно снять
    # с регитсрации unregister, в которым передаем обьекты регистрации

    request = client_socket.recv(4096)

    if request:
        response = 'Hello world\n'.encode()
        client_socket.send(response)
    else:
        selector.unregister(client_socket)
        client_socket.close()


def event_loop():
    while True:
        # так же как и в функции select - нам нужно получить выборку файлов для чтения или записи - для этого
        # создадим переменную events

        events = selector.select()  # (key, events) нужен нам первый элемент
        # key - это SelectorKey: fileobj, events, data

        for key, _ in events:
            print(f"{key.data}| {key.fileobj} | {key.events}")
            # получаю обратно свою функцию, которая сохраненна в data
            callback = key.data
            #  и вызываю ее, передав туда наш обьект(индификтор процесса... - socket)
            callback(key.fileobj)


if __name__ == '__main__':
    """
    Вывод этого примера:
    мы регистрировали сокет вместе с сопровождаемыми данными:
    - events - служебная инфа.. read или еще какой-то вид иземенеия
    - есть сокет(fileobj) и ассоцированная(как-то связанная с ним) функция(data)
    """
    server()
    event_loop()
