class ListInt:
    def __init__(self, limit):
        self.__num = limit
        self.__limit = 0

    # it = MyIter(10)
    def __iter__(self):
        return self

    # for i in it:
    def __next__(self):
        if self.__num <= self.__limit:
            raise StopIteration
        self.__num -= 1
        return self.__num + 1


it = ListInt(10)
for i in it:
    print(i)

print("""-------------------------  обратный отсчет    -----------------------------------""")


class MyIter:
    def __init__(self, limit):
        self.__num = 0
        self.__limit = limit

    # it = MyIter(10)
    def __iter__(self):
        return self

    # for i in it:
    def __next__(self):
        if self.__num >= self.__limit:
            raise StopIteration
        self.__num += 1
        return self.__num


it = MyIter(10)
for i in it:
    print(i)

print(' +---------- next task ------------------------')


class Persons_values:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instace, owner):
        return instace.__dict__[self.__name]


class Persons:
    name = Persons_values()
    surname = Persons_values()
    middle = Persons_values()

    def __init__(self, invite: list, strip=' '):
        self.name = []
        self.surname = []
        self.middle = []
        for i in invite:
            self.name.append(i.split(strip)[0])
            self.surname.append(i.split(strip)[1])
            self.middle.append(i.split(strip)[2])


po = Persons(['Кто-то там зовут', 'Меня вот так', 'Тебя по другому'])
for i in po.name:
    print(i)
