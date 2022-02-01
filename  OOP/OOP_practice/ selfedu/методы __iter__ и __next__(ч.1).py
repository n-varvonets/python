class CoordValue(Exception):
    pass

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

        if not (0 <= coord[0] < self.__width) or  not(0 <= coord[1] < self.__height):
            raise CoordValue("Значение координаты выходит за пределы изображения")

    def __setitem__(self, coord, color):
        # print(coord, color)  # >>> (1, 1) *
        self.__checkCoord(coord)  # поределяем корректность нашей координаты

        if color == self.__background:  # если цвет равен цвету фона, то...
            self.__pixels.pop(coord, None)  # удаляем соответсвующий пиксель нашего словаря, а если его внутри нет, то юзаем None что бы  удаления несуществющиего пикселя не бросило ошибку
        else:  # если условие не  сработало, то значит цвет отличается от цвета фона, то ...
            self.__pixels[coord] = color  # то тогда в словарь пиксель мы добавляем пиксель с соответствующей координатой и цветом
            # print("self.__pixels after is", self.__pixels)  # >>> self.__pixels after is {(1, 1): '*'}
            self.__colors.add(color)

    def __getitem__(self, coord):
        self.__checkCoord(coord)
        return self.__pixels.get(coord, self.__background)  # из нашего словаря пикселей мы получаем(get) её значение, а если вдрг её нет, то возращаем бэкграунд



img = Image(20, 4)
img[1, 1] = "*"
img[2, 1] = "*"
img[3, 1] = "*"
for y in range(img.height):
    for x in range(img.width):
        print(img[x, y], sep="", end="")
    print()
    """Но для того что бы сделать обьект img  итерирумеым, т.е. что бы реализовался ниже код необходимо... см. часть 2"""
for row in img:
    for pixel in row:
        print(pixel, sep="", end="")
    print()
