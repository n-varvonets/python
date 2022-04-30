# DEAD LOCK
import threading


def producer():
    print('Set locking')
    # берем блокировку
    with lock:
        print('done')
        # попытка взять блокировку в рамках текущего потока дает нам DEAD LOCK
        # Из данной блокировки накак не выйти, так как мы ожидаем завершения самого себя(1го with lock),
        # чтобы взять блокировку(2гоwith lock).
        # А второй тред никогда не зайдет в (1ый with lock), потому что первый тред его занял
        with lock:
            print("It's great")
    print('Locking release!')


# блокировка, позволяющая отметить какой участок кода атомарным.
lock = threading.Lock()  # БЛОКИРУЕТ РЕКУРСИЮ, Т.Е. ВЫЗОВ САМОГО СЕБЯ
# __enter__ => lock.acquire()  # мы можем захватить блокировку этим методом.. потом выполнить какие-то действия...
# __exit__ => lock.release()  # , а потом освободить тред
# т.е. захватываем управления -> атомарно внутри тела блокировки выполняем(никто не может влезть внутрь), а потом освобождаем:
lock.acquire()
print(1)
print(1)
print(1)
print(1)
lock.release()

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=producer)

task1.start()
task2.start()

task1.join()
task2.join()
