import gevent
from gevent import monkey
import time

# import requests

# из блокирующих операций I/O делаем неблокирующие.
# мы как бы прошиваем стандартные I/O, используя gevent
# теперь в сумме, запросы будут выполняться быстрее за счет отсутствия
# блокировки при ожидании ответа
monkey.patch_all()   # метод читаерский в данной библотеке, пот что если его вначале применить, то он сам
# определяет какие функции блокирующие,а какие просто выполнить код и переключается между ними...
# смотри результат с ним и без него - последовательность принтов отличается делая асинхронное вычисление

import requests

urls = [
    'https://www.google.com/',
    'https://itvdn.com/',
    'https://www.python.org/'
]


def fetch_url(url):
    print('Starting %s' % url)
    data = requests.get(url).text
    print('{} done'.format(url))


def sync_executor():
    # просто для примера как это выглядело бы просто синхронно
    for url in urls:
        data = requests.get(url).text


jobs = [
    gevent.spawn(fetch_url, _url)
    for _url in urls
]

started = time.time()
gevent.wait(jobs)
print('Spent: {}'.format(time.time() - started))
