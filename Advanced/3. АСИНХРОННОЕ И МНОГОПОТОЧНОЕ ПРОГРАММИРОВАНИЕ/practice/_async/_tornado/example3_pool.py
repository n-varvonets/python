import hashlib
from concurrent.futures import ThreadPoolExecutor

import tornado.gen
from tornado.ioloop import IOLoop
from tornado.process import cpu_count

# создаем pool потоков для вычислений, можно указать люое количество
pool = ThreadPoolExecutor(cpu_count())  # cpu_count() - чаем кол-во ядер нашего пк. кол-во ядер передаем в треды


def sync_highload_task(password):
    """
    Создам видимость высоконагруженной таски:
    100к записей поочередно захешировать.
    """
    for i in range(100_000):
        password = hashlib.sha256(password).hexdigest().encode()
    return password


# используя декоратор, помечаем нашу функцию как корутину для возмождности использовать внутри yield.
# NOTE: await использвуем когда есть async def _(): - в примере №4 это показано
@tornado.gen.coroutine
def make_password(password) -> str:
    """
    что бы неблокировать общий поток выполнения, то задачу   sync_highload_task(password) будем запускать в отдельном треде
    """
    # ожидаем результата из pool-а потоков и переключаемся на другую
    # до тех пор, пока не получим результат
    hashed_password = yield pool.submit(
        sync_highload_task,
        password.encode()
    )  # pool - это инстанс ThreadPoolExecutor. Как парамтры передаем высоконагруженной задачу с её  параметрами
    return hashed_password


@tornado.gen.coroutine
def test_cor():
    """
    Так же есть еще одна корутина просто для деманстрации что верхний код работает асинхронно
    :return:
    """
    for i in range(1, 10):
        print('Sleep on {}'.format(i))
        # мы засыпаем и переключаемся на другую сопрограмму
        yield tornado.gen.sleep(i)
    return 2


@tornado.gen.coroutine
def multi():
    """
    этой корутине обьеденям две задачи на выполнение
    :return:
    """
    # ожидаем выполнения нескольких корутин с помощью gen.multi
    result = yield tornado.gen.multi([
        test_cor(),
        make_password('test_pass')
    ])
    print(result)


# запуск корутин в цикле событий - event loop
IOLoop.current().run_sync(multi)
