class CoordValue:
    def __init__(self, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value

class Point:
    coordX = CoordValue("coordX")
    coordY = CoordValue("coordY")

    def __init__(self, x=0, y=0):
        self.coordX = x
        self.coordY = y

pt = Point(1, 2)
pt2 = Point(10, 20)
print(pt.__dict__["coordX"])
print(pt2.coordY, pt2.coordX)


