import time

import gevent
from gevent.event import Event


"""здесь есть две асинхронные задачи:
- 1. waiter() и emitter() - их синхронизируем через обьект ивент Event()
- 2 endless() - базис vent_loop, но только spawn(гринлет)...
"""

def waiter():
    print('I am waiting for event')
    # ожидание события с блокировкой дальнейшего исполнения кода функции
    event.wait()
    print('Waiter done')


def emitter():
    print('Emitter is sleeping')
    # засыпаем на 3 секунды
    gevent.sleep(3)
    # устанавливаем событие
    event.set()
    print('I kill endless task!')
    # останавливаем бесконечный greenlet принудилеьно
    # endless_task.kill()


def endless():
    """это совершенно другая задача, ивент_лупа, которая выполнятся
    независимо от двух выше асинхронных через ивент обьект"""
    while True:
        print('Endless Task will be working forever!')
        gevent.sleep(2)


# создаем Event, который импортировали из модуля gevent.event
event = Event()

endless_task = gevent.spawn(endless)  # получаем обьект, без запуска
# проверяем что нет печати >>> 'Endless Task will be working forever!'
print('--1--')
time.sleep(2)

jobs = [
    gevent.spawn(emitter),  # эта функция(гринлет-корутина) 1 раз выполнится
    gevent.spawn(waiter),  #  эта функция(гринлет-корутина) 1 раз выполнится
    endless_task,  #  эта функция(гринлет-корутина) будет постоянно выполняться, пока не kill её
]

gevent.wait(jobs)
