"""
Dependency inversion - более вьісокоуровневьіе модули не должньі зависить от более низкоуровневьіх.
       А в идеале все они должньі зависеть от каких неких абстрацкицй. И детали должньізависеть от абстракций."""

print('-------------- Before -------------')

import sys
import time


class TerminalPrinter:
    """Класс пиший лог в терминал"""
    def write(self, msg):
        sys.stderr.write(f"{msg}\n")


class FilePrinter:
    """Класс пиший лог в файл"""
    def write(self, msg):
        with open('log.txt', 'a+', encoding='UTF8') as f:
            f.write(f"{msg}\n")


class Logger:
    """
    Данньій класс нарушает DIP:
        - класс логгер записит от двух других классов TerminalPrinter(), FilePrinter()
    """
    def __init__(self):

        self.prefix = time.strftime('%Y-%b-%d %H:%M:%S', time.localtime())

    def log_stderr(self, message):
        TerminalPrinter().write(f"{self.prefix} {message}")


    def log_file(self, message):
        FilePrinter().write(f"{self.prefix} {message}")


logger = Logger()
logger.log_file("Starting the program...")
logger.log_stderr("An error!")

print('-------------- After -------------')

import sys
import time


class TerminalPrinter:
    def write(self, msg):
        sys.stderr.write(f"{msg}\n")


class FilePrinter:
    def write(self, msg):
        with open('log.txt', 'a+', encoding='UTF8') as f:
            f.write(f"{msg}\n")


class Logger:
    def __init__(self):
        self.format = '%Y-%b-%d %H:%M:%S'

    def log(self, message, notifier):
        #  notifier - и есть наша абстракция, т.е. в метод будем передавать уже какой-то конкретньій класс
        # главное что бьі передеваемьій класс реализоваовал метод write()

        prefix = time.strftime(self.format, time.localtime())
        notifier().write(f"{prefix} {message}")


logger = Logger()
logger.log("Starting the program...", TerminalPrinter)
logger.log("An error!", FilePrinter)