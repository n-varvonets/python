from inspect import getgeneratorstate


def coroutine(func):
    def inner(*args, **kwargs):
        g = func()
        g.send(None)
        return g
    return inner


class BlaBlaException(Exception):
    print("instructions from class Exception")


@coroutine
def average():
    count = 0  # изначально у нас нет никаких эелементов
    summ = 0  # изначально сумма будет 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print("Done")
            break  # ВАЖНО: нужно поставить брейк, что бы при выполенение метода throw  данный код выбивал
            # в контроле управление StopIteration  и потом мы смогли перехватить его для  RETURN value
        except BlaBlaException:
            print("My intructions in generator exception")
            break
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)

    return average


g = average()
"""тем самым вызов send(None)  отходит на сторой план из-за декоратора"""
# print(getgeneratorstate(g))
# print(g.send(None))  # вели из состояния GEN_CREATED в GEN_CREATED
print(getgeneratorstate(g))
print(g.send(5))
print(getgeneratorstate(g))
print(g.send(10))

# так же можно кидать в генератор исключения(кстомные в том числе) рез метод  throw:
try:
    g.throw(StopIteration)
except StopIteration as e:
    print("Average is ...", e.value)