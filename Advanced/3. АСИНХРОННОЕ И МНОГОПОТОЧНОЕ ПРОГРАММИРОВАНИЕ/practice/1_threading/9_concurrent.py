from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

"""
выше мы рассмотрели в модуле threading:
- как запускать
- как использовать виды блокировок (join(),set(),wait(),realise(),lock)
- как использовать потоко-безопасное хранилище
- GIL
"""

#  concurrent.futures использует два вида PoolExecutor потоков и процессов.

def handler(started=0, finished=0):
    """будем использовать всё ту же функцию для подсчета суммарных значений, что и в прошлых примерах"""
    # print('VALUES', started, finished)
    result = 0
    for i in range(started, finished):
        result += i
    return result

# Ниже реализовал два способа использования наших пулов(Thread и Process)

def run_by_executor(executor_class, max_workers=4):
    executor = executor_class(max_workers=max_workers)  # создаю екземпляр нашего пула(неважно executor_class - это
    # ThreadPoolExecutor или ProcessPoolExecutor - интеофейс у них один и тот же)
    started = time.time()
    # создаем футуры и выполняем параллельно (не забываем про GIL + threads).
    # executor.submit позволяет отправить функцию на выполнение в pool.
    future1 = executor.submit(handler, started=0, finished=2 ** 26)
    future2 = executor.submit(handler, started=2 ** 26, finished=2 ** 28)

    result = future2.result() + future1.result()
    print('Result: {result}. Time for {executor}: {spent_time}'.format(
        result=result,
        executor=executor_class.__name__,
        spent_time=time.time() - started
    ))


def run_by_executor_map(executor_class, max_workers=4):
    executor = executor_class(max_workers=max_workers)
    started = time.time()
    params = [
        [0, 2 ** 26],
        [2 ** 26, 2 ** 28]
    ]
    # используя map, запускам функцию handler на наборах данных params
    # в результате executor.map вернет нам список результатов, который мы можем
    # просуммировать.
    # Удобнее, чем executor.submit в том случае, если нам не нужна футуры
    # для отдельных наборов данных.
    result = sum(executor.map(handler, *params))

    print('Result: {result}. Time for {executor}: {spent_time}'.format(
        result=result,
        executor=executor_class.__name__,
        spent_time=time.time() - started
    ))

# run_by_executor_map и run_by_executor просто используют разные способы(map и submit) взаимодействия с Executor-ами

# сравним многопоточное выполнение и многопроцессное
print('Execute using map...')
run_by_executor_map(ThreadPoolExecutor)
run_by_executor_map(ProcessPoolExecutor)

print('Execute using submit...')
run_by_executor(ThreadPoolExecutor)
run_by_executor(ProcessPoolExecutor)


"""
В рамках двух процессов будет один механизм GIL, работа которого никак не связана
между друг друг, т.е. условно можно представить что два.  В отличи от четкого
последовательного выполнения потоков в процессе.
 
Процесс - тяжеловесней потока, его тяжелей запустить по времени, ресурсозатратней, НО..
если есть какая-то ТЯЖЕЛАЯ ЗАДАЧА, то пачка процессов дадут нам больше прироста, чем пачка тредов
"""
