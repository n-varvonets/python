# http://i.imgur.com/GBpftox.png - задание

#1
class Calendar:
    __slots__ = ["__day", "__month", "__year"]

    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

c = Calendar(4, 4, 4)
# c.ye1ar = 10
# print(c.year, c.ye1ar)
print(c._Calendar__year)  # >>> 4

#2
class PointValue:
    # def __init__(self, name):
    #     self.__name = name
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value

class Rectangle:
    __pointX = PointValue()
    __pointY = PointValue()

    def __init__(self, x, y):
        self.__pointX = x
        self.__pointY = y

p1 = Rectangle(4, 1)
p2 = Rectangle(3, 3)
# print(p1.__dict__, PointValue.__dict__)
p1._Rectangle__pointX = 8
# print(f"left-right point is ({p1._Rectangle__pointX}, {p1._Rectangle__pointY}) and point of right-but is ({p2._Rectangle__pointX}, {p2._Rectangle__pointY})")  #  работает и выводит защищенные аттрибуты
print(f"left-right point is ({p1._Rectangle__pointX}, {p1._Rectangle__pointY}) and point of right-but is ({p2._Rectangle__pointX}, {p2._Rectangle__pointY})")  #  работает и заменяет защищенный аттрибут
# но нужно сделать атрибуты защищенным - пока хз как
