
def subgen():
    message = yield
    print('Subgen recieved:', message)


g = subgen()  # создам объект генератора
# 1.1)прежде чем в него что-то передать - его нужно проинициализировать
# т.е. если передать в него что-то, то будет ошибка:
# g.send('saasdas')  >>> TypeError: can't send non-None value to a just-started generator

# 1.2)что бы увидеть в каком состоянии находится генератор, то можно импортировать функцию
from inspect import getgeneratorstate
print(getgeneratorstate(g))  # >>> GEN_CREATED

# 1.3) Сделаем так как этого хочет пайтон и передадим в него сначала None, а потом посмотрим его состояние
# g.send(None)  # это первоначальная инициализация генератора корутины (обязательное и оно предписано в документации)
print(getgeneratorstate(g))  # >>> GEN_SUSPENDED - состояние изменилось

next(g)  # вместо send можно использовать next()
print(getgeneratorstate(g))  # >>> GEN_SUSPENDED - состояние изменилось

# 1.4) Теперь(после инициализации генератора помощью send или next) можно передать туда данные
# g.send('My data')
#  >>> Subgen recieved: My data
# Traceback (most recent call last):
#   File "/home/nick/PycharmProjects/python/Advanced/3_async_threading/Molchanov/5_coroutin.py", line 24, in <module>
#     g.send('My data')
# StopIteration

"""2.теперь сделаю так что бы генератор не только принимал, а еще и отдавал бы что-то"""


def subgen2(some_val):
    x = f'Ready to accept message {some_val}'
    message = yield x
    print('Subgen2 recieved:', message)

g2 = subgen2(some_val='my_str')
print(getgeneratorstate(g2))
print(g2.send(None))  # >>> Ready to accept message - генератор вернул нам переменную X
# если второй раз уже что-то передать, то
print(getgeneratorstate(g2))
g2.send('my_sended_data')




