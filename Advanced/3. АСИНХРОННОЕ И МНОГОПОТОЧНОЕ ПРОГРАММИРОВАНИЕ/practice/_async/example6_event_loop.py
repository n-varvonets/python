import asyncio
"""Кейс если мы хотим запустить ивент луп и постоянно работать  до тех пока мы сами не захотим прервать работу"""

# ниже две разные задач(по две подзачачи каждая(корутины)), которые выполняются последовательно  что бы показать 2 вариант работы event_loop:
# - async_worker(), stop_event_loop() - показывают вызов функций(как корутин) передавая в них данные
# -resolve_future(), wait_for_future() - показывают работу event_loop передавая в коруитны обьект future в две
# запускаемые функции, одна из которых ожидает выполнения другой(set)

async def async_worker(seconds):
    print('Sleep using {}'.format(seconds))
    await asyncio.sleep(seconds)
    print('Done sleep: {}'.format(seconds))


async def stop_event_loop(loop, seconds):
    print('Stop in {}s'.format(seconds))
    await asyncio.sleep(seconds)
    loop.stop()
    print('Stopped')


async def resolve_future(future):
    """
    Если мы прокинем один и тот же обьект(future) в эту функцию, что и в wait_for_future, то
    - в resolve_future мы установим значение future через .set_result()
    - а в wait_for_future получим эту значение в  переменную result
    Т.е. если мы не запустим resolve_future, то результат никогда не придет в wait_for_future
    """
    print('---before await----')
    await asyncio.sleep(5)  # здесь мы типо сделали сложный запрос в сеть и отдали управление
    print(f'Future set_result - ОК. future="{future}"')
    future.set_result(10)  # здесь мы устанавливаем результат нашего запроса пулу future типо нашей работы для  await future


async def wait_for_future(future):
    result = await future  # здесь мы ожидаем от пула future пока кто-то не установит значение set_result().
    # т.е. await дет ждать ровно столько времени, сколько нужно установки результата для данного футера(future)
    print('Future result: {}'.format(result))


event_loop = asyncio.get_event_loop()
# добавляем в цико событий две задачи
event_loop.create_task(async_worker(3))
event_loop.create_task(async_worker(5))

# останавливаем цикл событий, независимо от успещности завершения в нём задач.
event_loop.create_task(stop_event_loop(event_loop, 13))


print('2ая задача')

# создаем футур и передадим его в корутину. в другой корутине будем дожидаться рещультата от данного футура.
# fut = event_loop.create_future()
fut = asyncio.Future()  # создам тот же самый обьект в который мы будем
# прокидывать в наши 2 сопрограммы(wait_for_future и resolve_future)
# в этой задаче мы установим результат футура
event_loop.create_task(resolve_future(fut))

# в этой задаче мы будем ждать результата футура
event_loop.create_task(wait_for_future(fut))

# запускаем бесконечный цикл событий, но так как выше мы добавили задачу
# для его остановки, то через 13 секунд мы выйдем из него.
event_loop.run_forever()
print('end')
event_loop.close()
