import socket
from select import select
# 2 главные задачи относительно сокетов:
# 1) определить какие сокеты уже готовы для (чтения/записи) (I/O) что бы вызвать у них соответствующие методы()
# Решение для 1 - это select, который отслеживает состояния файлов-процессов-сокетов.
# 2) нужен механизм, который мог бы переключаться управление между функциями (server(), client(client_socket))
# # Решение для 2 - это механизм event loop

# Concurrency from the Ground up Live(PyCon 2015) - конкурентность в питоне с нуля вживую

tasks = []  # Именно этот список будет наполняться генераторами... из этого списка мы будем брать первый элемент
# и передавать его в next

to_read = {}
to_write = {}


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        print('1.. after method next in even_loop')
        yield ('read', server_socket)  # Делаем так что бы наши генераторы отдавали кортежи... наши метки для фильтра
        print('2')
        client_socket, addr = server_socket.accept()  # read - таким образом данный сокет мы связываем с данным методом

        print('Connection from client после установки связи, до получения-отправки сообщения', addr)
        tasks.append(client(client_socket))  # нужно клиентский сокет добавить в список таск


def client(client_socket):
    while True:

        print('4', client_socket)
        yield ('read', client_socket)  # Делаем так что бы наши генераторы отдавали кортежи... наши метки для фильтра
        request = client_socket.recv(4096)  # read - таким образом данный сокет мы связываем с данным методом

        if not request:
            break
        else:
            response = 'Hello world\n'.encode()

            yield ('write', client_socket)  # Делаем так что бы наши генераторы отдавали кортежи... наши метки для фильтра
            client_socket.send(response)  # write - таким образом данный сокет мы связываем с данным методом

    client_socket.close()


def event_loop():

    # while True: - это вариант может быть, но Дэвид Бизле в своем докладе сделал так:
    while any([tasks, to_read, to_write]):  # any() - принимаем в себя список значений, каждое их которых дает либо
        # true, либо false...и если хоть один из них будет true, то any return true...
        # т.е. если хоть что-то из списка вернет нам тру, то цикл будет работать

        """
        если tasks - это список с генераторами, то словари (to_read, to_write) это так сказать сырье, из которых
        мы будем доставать генераторы+сокеты и кидать их на выполнение в next"""

        # Важно! Задача №1
        # Необходимо событийный цикл все время наполнять работой,
        # а именно - наполнять наш список tasks - генераторами, для этого создадим бесконечный цикл, который
        while not tasks:  # будет работать если  tasks - будет пустым

            # print(f"3.0.to_read={to_read}, to_write={to_write}")  # ключами словарей должны быть сокеты
            # >>> to_read={<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0,
            # laddr=('127.0.0.1', 5000)>: <generator object server at 0x7f68b4043360>}, to_write={}

            print(f"3.1.to_read.items()={to_read.items()}, to_write.items()={to_write.items()}")  # ключами словарей должны быть сокеты
            # >>> to_read.items()=dict_items([(<socket.socket fd=5, family=AddressFamily.AF_INET,
            # type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 5000)>, <generator object server at 0x7f68b4043360>)]),
            # to_write.items()=dict_items([])

            # example = {'key_name': 'Nick', 'key_age': 82}
            # for el in example:
            #     print(el)
            # >>> key_name, key_age

            # for key, value in to_read.items():
            #     print(f"8.key should be a socket and looks like ..{key}, value is...{value}")
            # >>> 8.key should be a socket and looks like ..<socket.socket fd=5, family=AddressFamily.AF_INET,
            # type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 5000)>, value is...<generator object server at 0x7f8ff08ba360>

            """проработав наш скрипт на этом месте останавливается - ждет уже подключение клиента"""
            ready_read, ready_write, _ = select(to_read, to_write, [])  # Передаем списки которые нужно мониторить...
            # результат вернет кортеж(файлов изменивших свое состояние), который распакуем в списки
            print(f"5.ready_read={ready_read}, ready_write={ready_write}")

            # теперь для каждого i/o файла(наших списков) передадим его генератор в tasks
            for sock in ready_read:
                """наполним наш tasks сокетом to_read[sock]"""
                print(f'5.1.to_read[sock]={to_read[sock]},| sock={sock},| to_read={to_read}')
                # tasks.append(to_read[sock])
                tasks.append(to_read.pop(sock))  # правильней сделать его через поп

            for sock in ready_write:
                """аналогичным способом делаем для ready_write"""
                print('+++++',sock)
                tasks.append(to_write.pop(sock))

        # Важно! Задача №2
        # Как запускать функции и наполнять словари to_read, to_write с нужными нам парами (yield 'read',сокет)
        try:  # мы в это условие попадем только тогда, когда в таске будут элементы
            print(f"0.0.в вписке генераторов tasks наш генератор - это tasks[0]={tasks[0]}")
            task = tasks.pop(0)  # получили первый элемент списка и в переменной таск у нас теперь генераторы
            print(f'0.1.Взяли из списка всех генераторов наш генератор и поместили его в переменную task={task}')
            # и берем выполннение нашего генератора, который распаковывает наши yield

            # и кидаем наш генератор работать дальше
            reason, sock = next(task)
            print(f"0.3. reason={reason}, sock={sock}")
            if reason == 'read':
                # тогда я создаю в списке нашу пару, которую нужно обработать
                to_read[sock] = task  # создаю ключ с таким сокетом, а в качестве значением - генератора(наша задача)
                print(f"7. converting sock:gen is ... {to_read}")
                # <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 5000)>: <generator object server at 0x7fc3420a1360>
            if reason == 'write':
                to_write[sock] = task

        except StopIteration:
            print('Done')




# Наполняем наш список данными... наполняем его генераторами
tasks.append(server())  # если передать sver  его вызова () [<function server at 0x7eff2e17fa60>],
# с вызовом - [<generator object server at 0x7f2b10935308>]
event_loop()