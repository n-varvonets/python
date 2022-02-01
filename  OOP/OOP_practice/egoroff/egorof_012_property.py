"""~~~ Вычисляем property ~~~"""


class Square:
    def __init__(self, s):
        self.side = s

    def area_ploschad(self):
        # площадь квадрата это возведение сторон в квадрат
        return self.side**2

a = Square(5)
print(a.area_ploschad())  # прикол в том что area должно быть атрибутом(свойством класса)... а не вызывать его(вставлять в конце круглые скобки)
print('---------1---------')

"""
1) для того что бы сделать area как аттр, а не метод - навесим на него property
"""

class Square2:
    def __init__(self, s):
        self.side = s

    @property
    def area_ploschad(self):
        # площадь квадрата это возведение сторон в квадрат
        return self.side**2

a2 = Square2(3)
print(a2.area_ploschad)
a2.side = 5
print(a2.area_ploschad)  #  и площаль сама при вызове - пересчиталась и выдала 25 - то что нужно
print('---------2---------')

