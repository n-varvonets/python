class CoordValue(Exception):
    pass


class ImageYIterator:
    def __init__(self, img):
        self.__limit = img.height
        self.__img = img
        self.__y = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__y >= self.__limit:
            raise StopIteration

        self.__y += 1
        # print(ImageYIterator)
        return ImageXIterator(self.__img, self.__y-1)


class ImageXIterator:
    def __init__(self, img, y: int):
        self.__limit = img.width
        self.__img = img
        self.__x = 0
        self.__y = y

    def __iter__(self):
        return self

    def __next__(self):
        if self.__x >= self.__limit:
            raise StopIteration

        self.__x += 1
        return self.__img[self.__x-1, self.__y]

class Image:
    def __init__(self, width, height, background="_"):
        self.__background = background
        self.__pixels = {}
        self.__width = width
        self.__height = height
        self.__colors = {self.__background}

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def __checkCoord(self, coord):
        if not isinstance(coord, tuple) or len(coord) != 2:
            raise CoordValue('Кординаты точки должны быть двухмерным кортежом')

        if not (0 <= coord[0] < self.__width) or not (0 <= coord[1] < self.__height):
            raise CoordValue("Значение координаты выходит за пределы изображения")

    def resize(self, width=None, height=None):
        # здесь должна быть проверка на корректность введенных данных
        # Назначаем новые значения (ширина и высота),  если  новые параметры =None, параметры оставляем без изменения
        self.__width = width if width is not None else self.__width

        self.__height = height if height is not None else self.__height
        # обходим словарь с координатами удаляем точки которые выходят за новые границы
        # print(self.__pixels)  # >>> {(1, 1): '*', (2, 1): '*', (3, 1): '*'}
        for (width, height) in self.__pixels.copy():
            if (width > self.width) or (height > self.height):
                self.__pixels.pop((width, height))

    def __setitem__(self, coord, color):
        # print(coord, color)  # >>> (1, 1) *
        self.__checkCoord(coord)  # поределяем корректность нашей координаты

        if color == self.__background:  # если цвет равен цвету фона, то...
            self.__pixels.pop(coord,
                              None)  # удаляем соответсвующий пиксель нашего словаря, а если его внутри нет, то юзаем None что бы  удаления несуществющиего пикселя не бросило ошибку
        else:  # если условие не  сработало, то значит цвет отличается от цвета фона, то ...
            self.__pixels[
                coord] = color  # то тогда в словарь пиксель мы добавляем пиксель с соответствующей координатой и цветом
            # print("self.__pixels after is", self.__pixels)  # >>> self.__pixels after is {(1, 1): '*'}
            self.__colors.add(color)

    def __getitem__(self, coord):
        self.__checkCoord(coord)
        return self.__pixels.get(coord,
                                 self.__background)  # из нашего словаря пикселей мы получаем(get) её значение, а если вдрг её нет, то возращаем бэкграунд

    # --------------------------------Таким образом работает итератор нехт--------------------
    # class MyIter:
    #     def __init__(self, limit):
    #         self.__num = 0
    #         self.__limit = limit
    #
    #     # it = MyIter(10)
    #     def __iter__(self):
    #         return self
    #
    #     # for i in it:
    #     def __next__(self):
    #         if self.__num >= self.__limit:
    #             raise StopIteration
    #         self.__num += 1
    #         return self.__num
    #
    # it = MyIter(10)
    # for i in it:
    #     print(i)

    #  ------------------------ реализуем итератор в нашем классе, как в примере выше ---------------
    def __iter__(self):
        return ImageYIterator(self)  # пердаем новый вызов класса с нашим обьектом для ссылки на поиск словаря пикселей


img = Image(20, 4)
img[1, 1] = "*"
img[2, 1] = "*"
img[3, 1] = "*"
# img.width = 4
# img.height = 4
print(img.resize(None,9))
print(img.width ,img.height)

for row in img:
    for pixel in row:
        print(pixel, sep=" ", end="")
    print()
