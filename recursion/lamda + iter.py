foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

filter1 = list(filter(lambda x: x % 3 == 0, foo))
print(filter1)

print(list(map(lambda x: x*3+20, foo)))

# ---------------------------------------------------------------------------------------------------

class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration

simple_iter = SimpleIterator(3)

for i in simple_iter:
    print(i)

# ----------------------------------------------------------------------------------------

numbers = range(10)
squared = [n ** 2 for n in numbers if n % 2 == 0]
print(squared)   # [0, 4, 16, 36, 64]

print(hash(3.7))
print(hash(3.7))
print(hash(3.71))

"""# Генератор списка vs Выражения - генераторы"""
# [] = () - визуально
# Генератор списка [] or list comprehansion  - используются для создания и заполнения списка более сложными значениями.
gen_list = [i ** 2 for i in range(1, 6)]         #  for i in range(1, 6) - > __open__, __close__, __next__ -> next()
print(gen_list)  # [1, 4, 9, 16, 25]

gen_list1 = [(i, j) for i in 'abc' for j in [1, 2, 3]]
print(gen_list1)  # [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]

def gen_fee():
    """Фунцци генератори"""
    for i in 'abc':
        for j in [1, 2, 3]:
            yield (i, j)
s = gen_fee()
print(next(s))
print(next(s))

print(list(gen_fee()))  # [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]

gen_list3 = [i * j for i in [2, 3, 4, 5] for j in [1, 2, 3] if i * j > 10]
print(gen_list3)  # [12, 15]  - 5*2 и 5*3

# ----------------------------------------------------
"""# ВЫРАЖЕНИЯ - ГЕНЕРАТОРЫ не хранят в памяти все свои элементы, а выдают их по одному по мере надобности"""
gen_expression = (i ** 2 for i in range(1, 6))
print(gen_expression)  # <generator object <genexpr> at 0x102faeb30>

"""# Генератор - итератор, єлементами которого можно 1)итерироваться и 2)только один раз
# Итератор - обьект, которий 1)поддерживает функию next() и 2)помнит какой будет следующий єелемент коллекции"""

"""# Итерируемий обьект (range(1, 6) или list,dict,...))  - обьект по которому можно 1)поочердно  пройтись и 2)может бить преобразован к итератору:"""
list_iter_obj = [1, 2, 3]
# next(list_iter_obj)  # - упадет ошибка что не не итеоратор, хоть и итерируемьій обьект
gen_expression1 = iter(list_iter_obj)  # 2)НО может бить преобразован к итератору:
print(next(gen_expression1))  # 1
# print(next(gen1))  # 2
"""# ПОЄТОМУ итеруемий обьект - НЕ итератор, но его можно СПОКОЙНО сделать прокниув в iter().
# Генератор СРАЗУ является итератором и к нему СРАЗУ можно вьізвать функцию next()."""

"""ВАЖНО! Выражения - генераторы не хранят в памяти все свои элементы, а выдают их по одному \
# по мере надобности избегая MemmoryError. ПОЄТОМУ можно итерироваться только один раз."""
# c = list(range(1000000000000000))  # сразу видаст MemoryError. Питону не хватает помяти что би сохранить СРАЗУ такое большое кол-во єелементов внутри списка
# с1 = [i for i in range(1000000000000000)]  # через ГЕНЕРАТОР СПИСКА НЕСРАЗУ но вьідаст ошибку MemmoryError
# с2 = (i for i in range(1000000000000000))  # через ВЫРАЖЕНИЯ - ГЕНЕРАТОРЫ будет отдавать значения по одному, какой бьі єлемент не бил
# for i in с2:
#     print(i)

#  add info:
# 1. Взаимозаменяемость. [gen_list] == list((gen_expression))
if [i * 2 for i in range(1, 3)] == list((i * 2 for i in range(1, 3))):
    print('they are equal')
# 2. Нельзя узнать длину генератора:  len((gen_expression))
# 3. к генератору нельзя применить индекс: (gen_expression)[4]










# корутина - генератор, только в который можно посылать данные с помощью метода сенд




