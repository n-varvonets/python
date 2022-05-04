import threading
import time

# разделю задачу сумирования от нуля до 2**24: (и потом сравню время)
# 1й кейс - сделаю два потока(0-2**12, 2**12-2**24) и потом сложу сумму
# 2й кейс - просто одним поток

def handler(started=0, finished=0):
    """
    Данная функция будет запускать цикл по диапазону чисел (starter, finished).
    Передавая достаточно большие числа, выполнение цикла будет достаточно
    затратным по времени.
    """
    result = 0
    for i in range(started, finished):
        result += i
    results.append(result)


results = []

"""1) произведем замеры и сравним скорость двух потоков, против одного"""
task1 = threading.Thread(
    target=handler,
    kwargs={'finished': 2 ** 12}
)
task2 = threading.Thread(
    target=handler,
    kwargs={'started': 2 ** 12, 'finished': 2 ** 24}
)  # 0 - 2^24

started_at = time.time()

# запустили по отдельности потоки
task1.start()
task2.start()

# присоеденили наши треды к основному потоку, что бы дождаться результаты выполнения
task1.join()
task2.join()

print('RESULTS 1')
print('Time: {}'.format(time.time() - started_at))
print('Value: ', sum(results))

"""2) аналогичный тест для одного основного потока выполнения"""
results = []
started_at = time.time()
handler(finished=2 ** 24)
print('RESULTS 2')
print('Time: {}'.format(time.time() - started_at))
print('Value: ', sum(results))
