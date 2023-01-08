from multiprocessing import Pipe, Process
from queue import Empty
from time import sleep

# та же самая реализация передачи данньій, только с Pipe


def pipe_worker_1(p: Pipe):
    some_data = 100500
    p.send(some_data)


def pipe_worker_2(p: Pipe):
    print("Инфа которая прилетела с главного процесса: ... ", p.recv())


if __name__ == "__main__":
    """
    работаем с конвеерами.
    Важно: в pipe_worker мьі положили child_pipe, а с главного процесса мьі будем вьізвать parent_pipe
    """
    parent_pipe, child_pipe = Pipe()
    p1 = Process(target=pipe_worker_1, args=(child_pipe, ))
    p1.start()
    p2 = Process(target=pipe_worker_2, args=(child_pipe, ))
    p2.start()

    print("Информация из дочернего процесса:", parent_pipe.recv())  # может повиснуть, потому что ожидает что-то
    # должен прилетитеть аргумент( если закоментить строчку p.send(some_data), то пивиснет код)

    parent_pipe.send("Информация из главного процесса")

    p1.join()
    p2 .join()