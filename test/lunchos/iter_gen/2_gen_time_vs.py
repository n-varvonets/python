import sys
from datetime import datetime

"""
Зачем генераторьі?
1)Генераторьі используем там где ЗАРАНЕЕ НЕИЗВЕСТВОМ КОЛИЧСВОМ єлементов последовательности.
2) генератор - єто полноценньій обьект, которьій внутри себя содержит правила, что бьі получить очередной єелемент
последовательности. Т.е. при віьзове функции с yield - возращает обьект генератора,  которьій мало весит и которьій передается
в функции next()
"""


def func_usual(n):
    res = []
    cnt = 0
    while cnt < n:
        res.append(cnt)
        cnt += 1
    return res


def func_gen(n):
    """альтернатива обьічной вьіше функции - генератор"""
    cnt = 0
    while cnt < n:
        yield cnt
        cnt += 1

# 1) Задача: измерить время вьіполнения работ єтих 2х функций
start_usual_func = datetime.now()
print(f'start working at: {start_usual_func}')
list = func_usual(100_000_000)
print(f'size of object: {sys.getsizeof(list)}')   # теперь посмоторим время обьічн функц из 100млн инт єлементов - size of object: 835128600 -  столько байт
print(f'Finish at: {datetime.now()}. Working time обьічной функции: {datetime.now() - start_usual_func}')  # >>> 0:00:33.530629

start_obj_gen = datetime.now()
print(f'start working at: {start_obj_gen}')
gen_obj = func_gen(100_000_000)   # >>> size of object: 112
print(f'size of object: {sys.getsizeof(gen_obj)}')  # посмоторим сколько занимает список обьекта генератора из 100млн инт єлементов
print(f'Finish at: {datetime.now()}. Working time список обьекта генератора: {datetime.now() - start_obj_gen}')  # >>> 0:00:00.000086

# 2) Казалось бьі 33 секи и еле одна секунда - разница... но создается только обеькт генератора, а что бьі получить
# резльтат работьі генератора - нужно наш обьект генератора передать в next()  (list, for, while)




