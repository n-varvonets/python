import os
import threading


def exec_watcher():
    # запускаем функцию print_files каждые 5 секунд в отдельном потоке
    timer = threading.Timer(5.0, print_files)
    timer.start()


def print_files():
    """функция выводит список все файлов текущей директории"""
    for i in os.listdir('.'):
        print(i)
    exec_watcher()  # если хочу постоянно каждые 5ть сек выводить список всех файлов (мониторить за изменением)


exec_watcher()
