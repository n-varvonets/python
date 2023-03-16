import sys
import time

"""Open-cloesed - наш класс можно расширять, но напрямую их не модифицировать"""

print('-------------- Before -------------')
# проблема - можем что-то изменить, а єто повлечет измения в других местах - поєтому для доп функционала -
# проше отнаследоваться, а и дать новьіе метод.
# т.е. в исходньій класс не вносить изменения, а его расширять путем наследования

class Logger:

    def log(self, message):
        current_time = time.localtime()
        sys.stderr.write(f"{time.strftime('%Y-%b-%d %H:%M:%S', current_time)} --> {message}\n")


logger = Logger()
logger.log('An error has happened!')


print('-------------- After -------------')

import sys
import time


class Logger:
    def __init__(self):
        self.format = '%Y-%b-%d %H:%M:%S -->'

    def log(self, message):
        prefix = time.strftime(self.format, time.localtime())
        sys.stderr.write(f"{prefix} {message}\n")


class CustomerLogger(Logger):
    def __init__(self):
        super().__init__()
        self.format = '%Y-%b-%d ::'


logger = Logger()
logger.log('An error has happened!')

c_logger = CustomerLogger()
c_logger.log('Custom logged message!')