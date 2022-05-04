from inspect import getgeneratorstate

def a():
    """простой пример работы yield from для понимания - просто yield-ит нам результат из любого итер-го обьекта """
    yield from 'nick'
g = a()
print(next(g))
print(next(g))
print(next(g))

"""
усложним задачу и превратим наши генераторы в корутины
Задача: из вызывающего кода передавать на обработку данные в подгенератор через делегирующий генератор

Обработка исключений делается в обьекте StopIteration, которую так же нужно обработать в делегаторе.
это можно сократить контсрукцией yield from
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

# @coroutine  - уже не нужен т.к. yield from содержит в себе инициализацию подгенератора
def subgen():
    while True:
        try:
            print('before subgen')
            message = yield
            print('afet subgen')

        except StopIteration:
            print('ku-ku!')
            break # здесь прирываем цикл
        else:
            print('----------', message)

    return 'Some important value as common result of subgen()'


@coroutine
def delegator(sg):
    """
    делегирующий генератор должен сначала принять наши значения, а потом передать в сабген
    + yield from помагает сократить ниже код + обрабатывать StopIter
    """
    # while True:
    #     try:
    #         print('before delegator')
    #         data = yield  # принимаем наши значения
    #         print('middle delegator')
    #         sg.send(data)  # передаем в сабген
    #         print('after delegator')
    #
    #     except BlaBlaException as e:
    #         """если пошла какая-то ошибка(например наша кастомная или любая другая(типов,итерации и т.д.)), то
    #         отлавливаем её и пробрасываем в делегатор"""
    #         print('-------- err before subgen')
    #         sg.throw(e)
    """
    Вопрос: нафига тогда делгатор нужен, если все выполняется на стороне сабгена?
    Ответ: делегатор может получить результатирующее значение с помощью слова return в самом subgen и сохранить её
    в переменную что бы как-то прооперировать им
    """
    common_result_subgen = yield from sg
    print(common_result_subgen)


d = delegator(subgen())
d.send('first_data')
d.send(235)
d.throw(StopIteration)

# т.е. конструкция yield from не только заменяет цикл, который проворачивает подгенератор..
# yield from берет на себя:
# - передачу данных в подгенератор
# - передачу исключений  в подгенератор
# - получает возвращаемый с помощью return результат работы сабгена
#
# yield from в других языках называется await. Смысл await в том что вызываЮЩИЙ код(делегатор) напрямую
# упраляет работой подгенератора вызываЕМОГО(сабгенератора) и пока это происходит ДЕЛЕГАТОР ОСТАЕТСЯ ЗАБЛОКИРОВАННЫМ.
# т.е. он вынужден ожидать (await) когда подгенератор закончит свою работу.
# ВАЖНО: подгенратор должен содержать в себе механизм заверщающий работу, потому что если этого не сделать, то
# делегаьтор будет навечно заблокирован








