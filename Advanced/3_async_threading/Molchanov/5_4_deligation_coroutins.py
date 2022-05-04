from inspect import getgeneratorstate

"""
усложним задачу и превратим наши генераторы в корутины
Задача: из вызывающего кода передавать на обработку данные в подгенератор через делегирующий генератор
"""

def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        print('initial')
        g.send(None)
        return g
    return inner


class BlaBlaException(Exception):
    pass

@coroutine
def subgen():
    while True:
        try:
            print('before subgen')
            message = yield
            print('afet subgen')

        except BlaBlaException:
            print('ku-ku!')
        else:
            print('----------', message)


@coroutine
def delegator(sg):
    """ делегирующий генератор должен сначала принять наши значения, а потом передать в сабген"""
    while True:
        try:
            print('before delegator')
            data = yield  # принимаем наши значения
            print('middle delegator')
            sg.send(data)  # передаем в сабген
            print('after delegator')

        except BlaBlaException as e:
            """если пошла какая-то ошибка(например наша кастомная или любая другая(типов,итерации и т.д.)), то
            отлавливаем её и пробрасываем в делегатор"""
            print('-------- err before subgen')
            sg.throw(e)


sg = subgen()
d = delegator(sg)
d.send('first_data')
d.throw(BlaBlaException)

# Это довольно много писанины в ко торой мы даже return  не использовали.
# Обработка исключений делается в обьекте StopIteration, которую так же нужно обработать в делегаторе.
# это можно сократить контсрукцией yield from