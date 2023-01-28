# __init__ vs __new__
# 1.Что такое магические (dunder) методы в Python?
# 1. - магический(dunder) должньі присутсвовать в спецификации класса. Т.е. если мьі сделаем __свой_метод__ с 2мя
# нижними подчеркиваниеями - єто будет не дандер-метод, потому что ОН НЕ ЗАРЕЗЕРВИВОВАННЬІЙ в пайтоне.
class T:
    def __init__(self, name):
        self.name = name
        print(self.name)


a = T("Alex")  # >>> Alex ? т.к. принт есть
b = T("Bob")  # >>> Bob
# фишка класса:
#  - два єтих езкмпляра будут независимьі(запускать в разньіз процессах, наследовать другой класс и получить его методьі тоже)

# 2. Способ создания экземпляра в обход init метода
# данная запись позволяет напрямую обратиться к метода класса  __new__ , обходя конструктор __init__
exm = T.__new__(T)
print(exm)  # <__main__.T object at 0x107e05bb0> - получаем только адресс на наш обьект. данньій обход инита может пригодится для синглтона


# 3.Паттерн Singleton, магический метод call + Метаклассы

class Singleton(type):
    """
    синглтон - мьі можем создать только один екземпляр класса,
    при попьітке создать новьій - нас вернет старьій. Зачем?
    например, создаем подключение к бд, логер для записи инфьі в файл

    __call__ - работает тогда, когда мьі вьізьіваем наш класс как функцию, и
    т.к. Singleton(type) - єто метаклас и его поведение переходит в логер.
    """
    _instances = {}  # {<class '__main__.Logger'>: <__main__.Logger object at 0x108581640>}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]  # cls._instances[cls] =  <class '__main__.Logger'>


class Logger(metaclass=Singleton):
    pass


print(Singleton.__class__, type(Singleton), Singleton.__mro__)  # <class 'type'> <class 'type'> (<class '__main__.Singleton'>, <class 'type'>, <class 'object'>)
print(Logger.__class__, type(Logger), Logger.__mro__)  # <class '__main__.Singleton'> <class '__main__.Singleton'> (<class '__main__.Logger'>, <class 'object'>)


class Logger_not_single():
    pass

# инстанс с синглтоном(одним айдишником)
single_log_1 = Logger()
single_log_2 = Logger()
print(single_log_1)  # <__main__.Logger object at 0x103cea250>
print(single_log_2)  # <__main__.Logger object at 0x103cea250>

# инстансьі БЕЗ синглтона(разньіе айдишники)
not_single_logger_1 = Logger_not_single()
not_single_logger_2 = Logger_not_single()
print(not_single_logger_1)  # >>> <__main__.Logger_not_single object at 0x103cea2b0>
print(not_single_logger_2)  # >>> <__main__.Logger_not_single object at 0x103cea2e0>

# --------------------------
class T:
    def __int__(self, name):
        self.name = name
        print(self.name)
exm = T.__new__(T)
print(exm)
exm1 = T()
print(exm.name)
print(exm.name)

# ----------selfedu----------------
# super()

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"


class Styles:
    def __init__(self, color="red", width=1):
        print('Konstructor Styles')
        self._color = color
        self._width = width


class Pos:
    """будет содержать позиции наших линий"""

    def __init__(self, sp: Point, ep: Point):
        print("Konctuctor Positions")
        self._sp = sp
        self._ep = ep


class Line(Pos, Styles):
    def draw(self):
        print(f"Drawing the line: {self._sp}, {self._ep}, {self._color}, {self._width}")

# l = Line(Point(10,10), Point(100, 100), 'green', 5)  #  __init__() takes 3 positional arguments but 5 were given :
# 1. дочерний класс Line вьзівает конструктор Pos, которьій принимает 2 аргумента.. , а мьі через Line передаем ему 4.
l0 = Line(Point(10, 10),
          Point(100, 100))  # - так будет работать, но нам хотелось бьі что бьі єта программа работала с 4мя параматрами

# Как вариант решения можно:
#  - 1)добавить остаточньіе аргументьі;
#  - 2)потом явно вьізвать конструтор(__init__) базового класса Styles
class PosV1:
    def __init__(self, sp: Point, ep: Point, *args):  # 1)добавили остаточньіе аргументьі
        print("Konctuctor Positions")
        self._sp = sp
        self._ep = ep
        Styles.__init__(self, *args)  # 2)явно віьзвав метод другого баового класса
class LineV1(PosV1, Styles):
    def draw(self):
        print(f"Drawing the line: {self._sp}, {self._ep}, {self._color}, {self._width}")
l_V1 = LineV1(Point(10, 10), Point(100, 100), 'green', 5)
l_V1.draw()  # >> Drawing the line: (10, 10), (100, 100), green, 5

# Работает! НО если мьі поменяем наследование class LineV1(Styles, PosV1) - то программа поламется
# Хорошо, тогда в уже в первом по очереди конутрукторе Styles - тоже добавим явньій віьзов другого базового конструктора...

class StylesV2:
    """
    думонстрация "проблемьі рекурсии mro"
    сейчас взаимдействуем с PosV1 и явно передаем, тем самьім получается,
    что каждьій конструтор будет вьізвать другой конструктор до бесконечности
    """
    def __init__(self, color="red", width=1, *args):
        print('Konstructor Styles')
        self._color = color
        self._width = width
        PosV2.__init__(self, *args)
class PosV2:
    def __init__(self, sp: Point, ep: Point, *args):  # 1)добавили остаточньіе аргументьі
        print("Konctuctor V1 Positions")
        self._sp = sp
        self._ep = ep
        StylesV2.__init__(self, *args)
class LineV2(PosV2, StylesV2):
    def draw(self):
        print(f"Drawing the line: {self._sp}, {self._ep}, {self._color}, {self._width}")
# l_v2 = LineV2(Point(10, 10), Point(100, 100), 'green', 5)



"""super() - решает данную с появлением "проблемьі рекурсии mro" (какой
класс вьізвать первьім и как передать остаточньіе агрументьі второму)"""
print('--- решение супер(с учетом порядка наследования) ----')
class StylesV3Super:
    def __init__(self, color="red", width=1, *args):
        print('Konstructor Styles')
        self._color = color
        self._width = width
        super().__init__(*args)
class PosV3Super:
    def __init__(self, sp: Point, ep: Point, *args):  # 1)добавили остаточньіе аргументьі
        print("Konctuctor V12 Positions")
        self._sp = sp
        self._ep = ep
        super().__init__(*args)
class LineV3Super(PosV3Super, StylesV3Super):
    def draw(self):
        print(f"Drawing the line: {self._sp}, {self._ep}, {self._color}, {self._width}")
l_V3Super = LineV3Super(Point(10, 10), Point(100, 100), 'green', 1)
l_V3Super.draw()


# Но и  данньій метод тоже не очень хорош, потосму что мьі должньі помнить порячдок наследования и передачи аргументов.
# - в базовьіх класах убрать аргументьі
# - в дочернем классе прописать контруктор
# - в конструкторе дочернего класса определить пременньіе
# - и дальше в конструкторе дочернего класса метод через функцию супер вьізвать конструктор __инит__ базового класса.(какого именно - супер определить сам поочередно)

print('--- решение супер(БЕЗ учетом порядка наследования) ----')
class StylesV4Super:
    def __init__(self):
        print('Konstructor Styles')
        super().__init__()
class PosV4Super:
    def __init__(self):
        print("Konctuctor Positions---")
        self._atrr = None or self._width/10
        print(self._atrr)
        super().__init__()
class LineV4Super(PosV4Super, StylesV4Super):  # StylesV4Super, PosV4Super
    def __init__(self, sp: Point, ep: Point, color="red", width=1):
        self._color = color
        self._width = width
        self._sp = sp
        self._ep = ep
        super().__init__()  # без єтой строки не попадем в базовьіе классьі и не отпринтует конструктор
    def draw(self):
        print(f"Drawing the line: {self._sp}, {self._ep}, {self._color}, {self._width}, {self._atrr + 2}")
l_V4Super = LineV4Super(Point(10, 10), Point(100, 100), 'green', 2)
l_V4Super.draw()

# т.е. что бьі не перезагружать/оверврайтить родительский метод, а віьвзвать его работу,
# с учтом актуальной инфьі, которую собрали в дочернем классе

"""Hom/Work - https://ibb.co/Smt71yw"""
class AMD:
    pass
class Intel:
    pass
class Nvidia:
    pass
class GeForce:
    pass
class CPU(AMD, Intel):
    pass
class GPU(Nvidia, GeForce):
    pass
class Memory:
    pass
class MotherBoard(CPU, GPU, Memory):
    pass