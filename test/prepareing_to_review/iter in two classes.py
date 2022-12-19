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


class MyIterObjectClass:
    """
    Итерируемьій обьект - не итератор, так как не поддерживает функцию __next__,
    но внутри должен иметь метод __iter__,
    Итерируемьій обьект можно спокойно сделать итератором - прокинуть итерируемьій обект в iter()
    """

    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        return self.obj


gen_obj = MyGenerator('1we')
iter_obj_1 = MyIterObjectClass(gen_obj)

print(next(iter_obj_1)) #  хоть даже если и будет иметь обьект своего кастомньій класса внутри метод __итер__ - то он
# все равно не будет считаться итератором
print(next(iter(iter_obj_1)))

for i in iter_obj_1:
    print(i)