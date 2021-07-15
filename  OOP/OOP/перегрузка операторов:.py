"""http://i.imgur.com/LZ7SFSX.png """

class Point3D:
    def __init__(self, x: int, y: int, z: int):
        if not isinstance(x and y and z, (int, float)):
            raise ValueError("Кординаты должны быть целым числом")
        self.__x = x
        self.__y = y
        self.__z = z

    def getPointOther(self):
        return [self.__x, self.__y, self.__z]

    def check_and_coors(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("Правый опранд должен быть типом Point3D")
        return [self.__x, self.__y, self.__z]

    def __add__(self, other):
        coors_cur_instance = self.check_and_coors(other)
        rez = []
        for i in range(3):
            rez.append(coors_cur_instance[i] + other.getPointOther()[i])
        return Point3D(*rez)

    def __sub__(self, other):
        coors_cur_instance = self.check_and_coors(other)
        rez = []
        for i in range(3):
            rez.append(coors_cur_instance[i] - other.getPointOther()[i])
        return Point3D(*rez)

    def __truediv__(self, other):
        coors_cur_instance = self.check_and_coors(other)
        rez = []
        for i in range(3):
            rez.append(coors_cur_instance[i] / other.getPointOther()[i])
        return Point3D(*rez)

    def __eq__(self, other):
        coors_cur_instance = self.check_and_coors(other)
        rez = []
        for i in range(3):
            rez.append(coors_cur_instance[i] == other.getPointOther()[i])
        if False in rez:
            return False, f"Координаты не совпадают"
        return True

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой")
        if item == "x":
            return self.__x
        if item == "y":
            return self.__y
        if item == "z":
            return self.__z

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Ключ должен быть строкой")
        if not isinstance(value, (int, float)):
            raise ValueError("Значение должно быть целым числом")
        if key == "x":
            self.__x = value
            return self.__x
        print(self.__x)
        if key == "y":
            self.__y = value
            return self.__y
        if key == "z":
            self.__z = value
            return self.__z

    def __str__(self):
        return f"Coordinates of certain instance is (x = {self.__x}, y = {self.__y}, z = {self.__z})"


p1 = Point3D(6, 1, 6)
p2 = Point3D(7, 3, 2)
print(p1+p2)
print(p2 - p1)
print(p2/p1)
print(p2 == p1)
p1["x"] = 1
print(p1["x"], p2["z"])

"""1.пример преоброзования"""
# a = [1, 2, 3]
# b = [5, 7, 6]
# for i in range(3):
#     print(a[i], b[i])
# >>>
# 1 5
# 2 7
# 3 6

"""2.а теперь как это работает с зип фанк"""
# rez = zip(a, b)
# print(rez)  # >>> <zip object at 0x7fa0bf110dc8>
# print(list(rez))  # >>> [(1, 5), (2, 7), (3, 6)]
# lst1 = [1, 2, 3]
# lst2= [8,6,7]
# print(list(zip(lst1,lst2)))


