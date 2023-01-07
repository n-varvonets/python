import webbrowser

from multiprocessing import Process
from datetime import datetime
import time
import os

print(" --- Регение пролемьі --- ")
# CASE:  мьі хотим что бьі ПОКА НЕ ЗАВЕРШИТСЯ дочерний процесс, то не перехоить к основному процессу
webbrowser.open("https://ibb.co/TT5Sbq5")
# тЧто делать? Ответ прост! Ипользовать синхронизацию процессов!
# Т.е. сказать главному процессу, что в нужном НАМ МЕСТЕ месте нужно дождать дочерний процесс.
# join() - по сути некая блокировка основного потока


def sleeper(slp_secs: int):
    """По задумке данньій дочерний процесс заверщиться сиьно позже чем главньій процесс исполняем файла.
    slp_secs: нагрузка задач на функцию, которую условно переведем в секундьі віьполнения"""
    time.sleep(slp_secs)
    print(f"Process {os.getpid()} has been finished")


if __name__ == "__main__":
    start = datetime.now()
    p = Process(target=sleeper, args=(10,))
    p.start()
    p_1 = Process(target=sleeper, args=(25,))
    p_1.start()
    # time.sleep(31)  # как ЗАРДКОРНЬІЙ вариант дождаться завершения дочернего потока, а потом зпустить оснвной.. минсусьі - хардкор
    print("Two process have been started")
    p.join()
    p_1.join()

    # основной момент - то что ниже трочка - не отработает, пока не отрабаотает дочерний процесс
    print(f"Program in main process {os.getpid()} has been finished! Total execution time: ", datetime.now() - start)








