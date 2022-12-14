# Когда нас спрашивают про генератор, то нужно спросить в ответ -
# "а какой генератор он имеет ввиду? ((1)обьект генеритор в питоне иди же (2) генератор какой-то колллекции)
"""
Дисклеймер: есть такой тип функций, которьій  возращает обьект генератора - через yield
"""

"""Задача: мьі хотим получать колекции из неоопределенного кол-ва елементов(0, 100500+)"""
"""Проблема: в чем мьі будем хранить наши елементьі, если мьі не знаем сколько их?"""
def func_usual(n):
    res = []
    cnt = 0
    while cnt < n:
        res.append(cnt)
        cnt += 1
    return res

print(func_usual(5))  # если передадим больщое кол-во єелементов(500_000_000), то бдует генерироваться список(занимать время и память)

def func_gen(n):
    cnt = 0
    while cnt < n:
        yield cnt
        cnt += 1

# 1) запустим две функции и посмотрем ответ:
print(func_usual(5))   # >>>  [0, 1, 2, 3, 4]
print(func_gen(5))   # >>>  <generator object func_gen at 0x10cfca5f0>
print(func_gen(5000000000000))   # >>>  <generator object func_gen at 0x10cfca5f0>
"""В обьісном состоянии интерперитор видит две фнукции и ему плевать что внутри.
НО когда мьі ВЬІЗЬІВАЕМ функцию, то интерпереттор видит что внутри функции есть yield,  и он возращает генератор обьекта"""
"""И КАК РАЗ внутри генератора обьекта лежит правило_исполнения(наша логика функции с yield)"""

# 2) Задача: вьізовать у генератора первьіе 2 єлементa
my_gen_1 = func_gen(5)  # <generator object func_gen at 0x1079265f0>  тот же обьект генератора что и раньше
print(my_gen_1)
print(next(my_gen_1))   # >>> 0
print(next(my_gen_1))   # >>> 1
print('Как хорошо біть в основном потоке вьіполнения программьі')
print(list(my_gen_1))   # >>> [2, 3, 4]
