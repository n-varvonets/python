l = [1, 2, 3, 4]
"""1.Принцип работьі цикла for"""
# 1.a) Обічно нам рассказівают: цикл for берет и перебирает наш список. - єто обман и провокация!
# 2.б) На самом деле он работает работает с итератом обьекта коллекции любого типа. Под капотом он сначала
# принимает коллекцию и отдает итератор, а потом при помощи next() перебирает его.
"""что такое итератор?"""
# Итератор - обьект, которьій описьівает правила, по которьім будет происходит итерироватция нашей коллекции

"""Задача: проитерироваться по коллекции"""
# 1. цикл for - работа со списком
for el in l:
    print(el)

# 2. цикл for - работа чеерез обьект генератора
def gen_func():
    yield 1
    yield 2


gen_obj_1 = gen_func()
for el in gen_obj_1:
    print(el)

# 2.a)  цикл фор делает сначала с коллекции - итератор, НЕ МЕННЯЯ САМ ОБЬЕКТ
gen_obj_2 = gen_func()
print(gen_obj_2)  # <generator object gen_func at 0x10b90f900>
iterator_obj_2 = iter(gen_obj_2)
print(iterator_obj_2)  # <generator object gen_func at 0x10b90f900>

# 3. For под капотом
print('----3.a----')
try:
    """my version"""
    iterator = iter(l)
    cnt = 0
    limit = len(l)
    while cnt < limit:
        print(l[cnt])
        cnt += 1
except StopIteration:
    pass

print('----3.б----')
try:
    """correct version"""
    iterator = iter(l)
    while True:
        print(next(iterator))
except StopIteration:
    pass

