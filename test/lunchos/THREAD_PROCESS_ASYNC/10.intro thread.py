print("  -  1.Чем потоки отличаются от процессов?  - ")
# 1.0. Процесс является контейнером для потоков
# 1.1. потоки - более легковескньі, чем процессьі
# 1.2. потоки - делять между собой ресурсьі. И как следствие используеют общее адресное пространство(русерсьі)
# 1.3. Т.к. у кождого процесса свое собственное пространство ресурсов и дочерние копируют ресурсьі родительского
# процесса. Из-за єтого приходится с помощью pipe или queue обмениваться данньіми.
# 1.4. GIL - актуальньій только для ПОТОКОВ
print("  -  2.Потоки и процесьі ОС  - ")
# когд говорят Процессьі и Потоки в пайтон - єто не СОВСЕМ правильно говорить, потому что єто потоки и процессьі
# на стороне ОС, а мьі лишь с поощью обьектов на стороне питона и системньіх вьізове  прокидьіваем ей задачи.
print("  -  3.Когда что юзать  - ")
# Thread - для I/o bound задач, когда "вемя ожидания/простоя" - маленькое (напрмер:множество легких sql запросов или бд находится находится на том жехочте что и прилажуха)
# async - для I/o bound задач, когда "вемя ожидания/простоя" - большая.
# multiprocessing - віьоская нагрузка на CPU bound задачи.
print("  -  4.Practice  - ")

import time
import threading
import os
from datetime import datetime
from threading import Thread
from concurrent.futures import ThreadPoolExecutor


def func_i_o_bound_waiting():
    """Функция с имитацией I/O bound задачи"""
    print(f"єто поток {threading.get_ident()} из процесса {os.getgid()}")
    time.sleep(2)


def func_CPU_bound_task():
    """Функция с имитацией CPU задачи(hard perfomance)"""
    cnt = 0
    for _ in range(50_000_000):
        cnt += 1
    print(f"єто поток {threading.get_ident()} из процесса {os.getgid()}")


CNT = 0
def func_thread_share_resources():
    """
    Данная функция, показьівает, что thread используюют общее адресное пространство(русерсьі)
    в данному кейсе: глобаляная пересенная изменится если ее будет изменять каждьій поток.
    """
    global CNT
    CNT += 1
    print(f"єто поток {threading.get_ident()} из процесса {os.getgid()}: {CNT}")


# if __name__ == "__main__":
#     """
#     Usual single process of working our app in one proces and one thread
#     # Заметь внмание, что вьівали три функции, а поток и процесс один и тот же
#     """
#     start_time = datetime.now()
#     func_i_o_bound_waiting()
#     func_i_o_bound_waiting()
#     func_i_o_bound_waiting()
#     print(f"Total time for execution of function is {datetime.now() - start_time}")
#     # >>> єто поток 4414899712 из процесса 20
#     # >>> єто поток 4414899712 из процесса 20
#     # >>> єто поток 4414899712 из процесса 20
#     # >>> Total time for execution of function is 0:00:06.009340


# if __name__ == "__main__":
#     """
#     Usual single process of working i/o with one proces and many threads
#     """
#     start_time = datetime.now()
#     th1 = Thread(target=func_i_o_bound_waiting)
#     th2 = Thread(target=func_i_o_bound_waiting)
#     th3 = Thread(target=func_i_o_bound_waiting)
#     for thread in [th1, th2, th3]:
#         """начинаем работу наших потоков"""
#         thread.start()
#     for thread in [th1, th2, th3]:
#         """ожидаем завершения работьі наших потоков"""
#         thread.join()
#     print(f"Total time for execution of function is {datetime.now() - start_time}")
#
#     # >>> єто поток 123145398472704 из процесса 20
#     # >>> єто поток 123145415262208 из процесса 20
#     # >>> єто поток 123145432051712 из процесса 20
#     # >>> Total time for execution of function is 0:00:02.005260


# if __name__ == "__main__":
#     """
#     Лайфхак - точно точно также как для процессов - есть Pool и для потоков(убрать join-ьі и strat-ьі)
#     """
#     start_time = datetime.now()
#     with ThreadPoolExecutor(max_workers=1) as t:
#         [t.submit(func_i_o_bound_waiting) for _ in range(3)]
#     print(f"Total time for execution of function is {datetime.now() - start_time}")
#
#     # при 2 воркеров i/o:
#     # єто поток 123145584340992 из процесса 20
#     # єто поток 123145601130496 из процесса 20
#     # єто поток 123145584340992 из процесса 20
#     # Total time for execution of function is 0:00:04.002238
#
#     # при 3 воркеров i/o:
#     # єто поток 123145581551616 из процесса 20
#     # єто поток 123145598341120 из процесса 20
#     # єто поток 123145615130624 из процесса 20
#     # Total time for execution of function is 0:00:02.004590
#
#     # как итог: 3 задачи , а воркеров
if __name__ == "__main__":
    """в данному кейсе: глобаляная пересенная изменится если ее будет изменять каждьій поток"""
    start_time = datetime.now()
    with ThreadPoolExecutor(max_workers=1) as t:
        [t.submit(func_thread_share_resources) for _ in range(3)]
    print(f"Total time for execution of function is {datetime.now() - start_time}")
    # >>> єто поток 123145529405440 из процесса 20: 1
    # >>> єто поток 123145529405440 из процесса 20: 2
    # >>> єто поток 123145529405440 из процесса 20: 3
    # >>> Total time for execution of function is 0:00:00.000805



