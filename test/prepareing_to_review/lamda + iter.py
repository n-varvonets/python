
class MyCustomNotIterClass:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __iter__(self):
        # return self
        yield self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration

iterator = iter(MyCustomNotIterClass(6))
print(iterator)  # при ретерн  - <__main__.MyCustomNotIterClass object at 0x10c005070>
print(iterator)  # при йєлде - <generator object MyCustomNotIterClass.__iter__ at 0x105516a50>


not_iter_obj = MyCustomNotIterClass(2)
# print(next(not_iter_obj))
# 1)что бьі сделать итерируемьій КАСТОМНЬІЙ обьект - нужно доавить итер
iterator = iter(not_iter_obj)
# 2) что бьі сделать генератор - нужно ему придать функцию __next__ - наврное єто и делать yield
print(next(iterator))


class SimpleIteratorV1:
    """For integer"""

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration


simple_iter = SimpleIteratorV1(3)

for i in simple_iter:
    print(i)


class SimpleIteratoSrtV2:
    """For String"""

    def __init__(self, my_str: str):
        self.counter = 0
        self.my_str = my_str
        self.limit = len(self.my_str)

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.my_str[self.counter - 1]
        else:
            raise StopIteration


simple_iter_str = SimpleIteratoSrtV2('sqe')
for i in simple_iter_str:
    print(i)


class MyGenerator:

    """
    обьект генератора должен иметь метод реализована next()
    """

    def __init__(self, my_str: str):
        self.counter = 0
        self.my_str = my_str
        self.limit = len(self.my_str)

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.my_str[self.counter - 1]
        else:
            raise StopIteration


class MyIterator:
    """
    Итерируемьій обьект - не итератор, так как не поддерживает функцию __iter__,
    но его можно спокойно сделать таковьім, давбив в класс метод __итер_ или прокинуть
    итерируемьій обект в iter()
    """

    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        return self.obj


gen_obj = MyGenerator('wwe')
iter_method = MyIterator(gen_obj)

print(next(iter(iter_method)))

for i in iter_method:
    print(i)


raw_l = [1, 2, 3]
l = iter(raw_l)
print(next(l))
print(next(l))
print(next(l))

my_gen_1 = MyGenerator(raw_l)
print(next(my_gen_1))
print(next(my_gen_1))


# ----------------------------------------------------------------------------------------

"""# Генератор списка vs Выражения - генераторы"""
# 0. [] = () - визуально
gen_list3 = [i * j for i in [2, 3, 4, 5] for j in [1, 2, 3]]
gen_expr3 = (i * j for i in [2, 3, 4, 5] for j in [1, 2, 3])
print(gen_list3)  # [2, 4, 6, 3, 6, 9, 4, 8, 12, 5, 10, 15]
print(gen_expr3)  # <generator object <genexpr> at 0x108920dd0>
print(list(gen_expr3))  # [2, 4, 6, 3, 6, 9, 4, 8, 12, 5, 10, 15]
# 1. Взаимозаменяемость. [gen_list] == list((gen_expression))
if [i * 2 for i in range(1, 3)] == list((i * 2 for i in range(1, 3))):
    print('they are equal')
# 2. Нельзя узнать длину генератора:  len((gen_expression))
# 3. к генератору нельзя применить индекс: (gen_expression)[4]

"""Главное отличие"""  # Выражения - генераторы не хранят в памяти все свои элементы, а выдают их по одному \
# по мере надобности избегая MemmoryError. ПОЄТОМУ можно итерироваться только один раз.
# c = list(range(1000000000000000))  # сразу видаст MemoryError. Питону не хватает помяти что би сохранить СРАЗУ такое большое кол-во єелементов внутри списка
# с1 = [i for i in range(1000000000000000)]  # в конце конво получим такую же ошибку
# с2 = (i for i in range(1000000000000000))  # через ВЫРАЖЕНИЯ - ГЕНЕРАТОРЫ будет отдавать значения по одному, какой бьі єлемент не бил
# for i in с2:
#     print(i)

"""Генератор списка [] or list comprehansion"""  # - используются для создания и заполнения списка(c более сложными значениями).
gen_list = [i ** 2 for i in range(1, 6)]  # for i in range(1, 6) - > __open__, __close__, __next__ -> next()
print(gen_list)  # [1, 4, 9, 16, 25]

n, m = 3, 6
a = [[0]*m for i in range(n)]
print(a)  # >>> [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
a[1][3] = 100
print(a)  # >>> [[0, 0, 0, 0, 0, 0], [0, 0, 0, 100, 0, 0], [0, 0, 0, 0, 0, 0]]
for i in a:
    print(i)
# >>> [0, 0, 0, 0, 0, 0]
# [0, 0, 0, 100, 0, 0]
# [0, 0, 0, 0, 0, 0]

gen_list1 = [(i, j) for i in 'abc' for j in [1, 2, 3]]
print(gen_list1)  # [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]
gen_list1[5] = ("my_key", 50)
print(list(gen_list1))  # >>> [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('my_key', 50), ('c', 1), ('c', 2), ('c', 3)]

"""ВЫРАЖЕНИЯ-ГЕНЕРАТОРЫ"""  # - не хранят в памяти все свои элементы, а выдают их по одному по мере надобности.
# Нельзя обратиться по индексу,потому что упадет ошибка
gen_expr = ((i, j) for i in 'abc' for j in [1, 2, 3])
print(next(gen_expr))  # >>> ('a', 1)
def gen_expression():
    """Фунцци генератори"""
    for i in 'abc':
        for j in [1, 2, 3]:
            yield (i, j)

s = gen_expression()
print(next(s))  # >>> ('a', 1)
print(next(s))  # >>> ('a', 2)
print(next(s))  # >>> ('a', 3)
print(next(s))  # >>> ('b', 1)
print(list(gen_expression()))  # [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]

"""add info gen/iter/iter object"""
# - Генератор - итератор, єлементами которого можно 1)итерироваться и 2)только один раз. Т.е. в генераторе обьекта должна бьіть функция реализована next()
# - Итератор - обьект, которий 1)поддерживает функию next() благодаря методу __итер__ и 2)помнит какой будет следующий єелемент коллекции"""
# - Итерируемий обьект (range(1, 6) или list,dict,...))  - обьект по которому можно 1)поочердно  пройтись и 2)может бить преобразован к итератору:
list_iter_obj = [1, 2, 3]
print(type(list_iter_obj))  # <class 'list'>
print(list_iter_obj)  # [1, 2, 3]
# next(list_iter_obj)  # - упадет ошибка что не не итеоратор, хоть и итерируемьій обьект
gen_expression1 = iter(list_iter_obj)  # 2)НО может бить преобразован к итератору:
print(type(gen_expression1))  # <class 'list_iterator'>
print(gen_expression1)  # <list_iterator object at 0x10a290730>
print(next(gen_expression1))  # 1
# print(list(gen1))  # 2
# - ПОЄТОМУ итеруемий обьект - НЕ итератор, но его можно СПОКОЙНО сделать прокниув в iter().
# - Генератор СРАЗУ является итератором и к нему СРАЗУ можно вьізвать функцию next()."""
# - Корутина - генератор, только в который можно посылать данные с помощью метода сенд
