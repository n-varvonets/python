import os
import socket

"""можно не использовать ip and port  в качестве точки обмена, а использовать к примеру
какой-то файл в рамках одного компьютера бнз общения с внешним миром... - подобным образом работает докер... 
да и множество других сервисов запущенных на компе используют unix сокеты """

unix_sock_name = 'unix.sock'  # название нашего файла в качестве точки обмена
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)  # AF_UNIX - отдельный вид сокета, который использует \
# в кочестве точки входа - отдельный файл

if os.path.exists(unix_sock_name):
    """проверяем был ли создан файл,
    если - да, то удалеям его"""
    os.remove(unix_sock_name)

# резервируем сокету строковое представление файл.. если бы мы не укзалаи выше AF_UNIX, то была б ошибка
sock.bind(unix_sock_name)

while True:
    """только сейчас мы уже запускаем на чтение внутри нашей директории - файл,
     который появится после запуска данной строчки"""
    try:
        result = sock.recv(1024)
    except KeyboardInterrupt:  # выйти из цикла и закрыть порт можно будет при ctl+c - keyboard
        sock.close()
        break
    else:
        print('Received message "in loop" from udp client is ...', result.decode('utf-8'))
