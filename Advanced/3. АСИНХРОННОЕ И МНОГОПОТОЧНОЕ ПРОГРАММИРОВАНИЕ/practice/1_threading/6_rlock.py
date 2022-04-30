# DEAD LOCK
import threading
import time


def producer():
    print('Set locking')
    with lock:
        # поток, взявший блокировку может взять её бесконечное количество раз.
        # но другой поток будет ждать
        with lock:
            print("It's great")
            time.sleep(3)
    print('Locking release!')


# пример аналогичен 5_lock.py, но решает проблему DEAD LOCK в рамках
# одного потока.
lock = threading.RLock()  #  позволит вызывать самого себя рекрсивно, но не дасть вызвать другому потоку

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=producer)

task1.start()
task2.start()

task1.join()
task2.join()
