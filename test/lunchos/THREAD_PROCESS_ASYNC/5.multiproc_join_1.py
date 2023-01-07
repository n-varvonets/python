import webbrowser
print(" --- Постановка пролемьі --- ")
# CASE: бьівает такое, что программа, вьіполняемая в главном процессе может завершиться раньше, чем прогрмма, вьіполняемая в дочерном
webbrowser.open("https://ibb.co/kq3fFHF")

from multiprocessing import Process
from datetime import datetime
import time
import os


def sleeper():
    """По задумке данньій дочерний процесс заверщиться сиьно позже чем главньій процесс исполняем файла"""
    time.sleep(50)
    print(f"Process {os.getpid()} has been finished")


if __name__ == "__main__":
    print("""проблема: если мьі запустим код, то  сначала отработает 25ая строка основного потока,
     а ТОЛЬКО потом заврешиться дочерний процесс""")
    start = datetime.now()
    p = Process(target=sleeper)
    p.start()
    print(f"Program in main process {os.getpid()} has been finished! Total execution time: ", datetime.now() - start)








