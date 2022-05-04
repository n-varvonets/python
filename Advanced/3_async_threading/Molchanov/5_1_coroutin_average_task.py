"""
задача
Условие: есть сайт с какой-то посещаемостью и мо получаем ежедневную статистику о кол-ве просмотров, посетителей и т.д.
Задание: нужно получить среднее значение этих параметров. Т.е. создаем корутину и брасаем туда данные, которая будет
уже отдавать срелнее арифм по всем дням"""

from inspect import getgeneratorstate

class BlaBlaException(Exception):
    print("instructions from class Exception")

def average():
    """т.к. сред.арифм. - это сумма всех элементов разделенные на их кол-во"""
    count = 0  # изначально у нас нет никаких эелементов
    summ = 0  # изначально сумма будет 0
    average = None

    count_loop = 0

    while True:
        try:
            print(f'in before {count_loop}')
            x = yield average
            count_loop += 1
            print(f'in after {count_loop}')
        except StopIteration:  #  войдет в этот код, когда прирвем итерацию
            print("Done")
        except BlaBlaException:
            print("My intructions in generator exception")
        else:  # то что будет происходить после try
            print(f'out before {count_loop}')
            count += 1
            summ += x  # в общую сумму добавляю отправленное число через метод send
            average = round(summ / count, 2)

            count_loop += 1
            print(f'out after {count_loop}')

g = average()
print(getgeneratorstate(g))
print(g.send(None))  # вели из состояния GEN_CREATED в GEN_CREATED
print(getgeneratorstate(g))
print(g.send(5))
print(getgeneratorstate(g))
print(g.send(10))

# так же можно кидать в генератор исключения(кстомные в том числе) рез метод  throw:
g.throw(BlaBlaException)