import threading
import time


def producer():
    """основной поток будет уведомлять всех слушателей, что он что-то сделал"""
    print(' --- before producer()')
    time.sleep(10)
    print('Product found!')
    # устанавливаем событий
    product.set()  # уведомляет  всех слушателей, что событие произошло
    """
    - после product.set() управление перейдет к другому потоку
    - как только поток с  wait отработает, то придем обратно и очистим список событий, что бы нашу данную функцию
    кто-то вызвал и опять установили set  - wait - clear
    """
    print(' ---  between set() and .clear()')

    product.clear()  # очищаем событие и нужно опять его ждать


def consumer():
    """данная функция будет ожидать пока какой-то поток не"""
    print('product wait')
    # ожидаем события ровно столько, пока не вызовется product.set в любом из потоков
    product.wait()  # говорим что ожидаем событие из другого потока и интерпретатор не даст дальше пойти до тех пор
    # пока какой-нибудь из потоков не вызовет product.set
    print('Product exists!')


# создаем событие, которое будем использовать в потока- ожидать и устанавливать
# создадим блокировку потока до появления события product
product = threading.Event()

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=consumer)

task1.start()
task2.start()

print('--- before join()')

task1.join()
task2.join()
