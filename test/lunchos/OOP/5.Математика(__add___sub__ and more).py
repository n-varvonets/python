print(" --- математика(использование ее символов) для обьектов разного типа --- \n")
# 1)Вступление:
# 1.1)В качестве примера - будем брать сложение векторов
# 1.2)Вектор - направленньій отрезок. У него есть начальная точко и конечная. И он символизмруе как бьі перемещение в двумерном пространстве
# 1.3) Сложение векотоов (https://nickolay-varvonets.nimbusweb.me/share/8110138/6z5qt9wzr4wo70tln49z):
#            (x, y)
# start    = (0, 0)
# vector_a = (2, 2)
# vector_b = (0, 2)
# vector_c = (2, 4)

# vector_a + vector_b = vector_c
# (2, 2) + (0, 2) = (2, 4)

print('Метод 1. Сложение векторов через вьізов функций двух разньіх обьектов вектора.(а не с математич. символами)')
class Vector:
    """
    класс описуващий обьічньій 2D-вектор.
    Проблематика: у класса есть две кординатьі x, y и я хочу реализовать сложение двух векторов..как?
    К примеру реализовать метод Сложение векторов.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    def add_vector_to_vector(self, another_vector_obj):
        """к примеру нужно взять свой єкземпляр вектора и доавбить другой єкземляр"""
        new_x = self.x + another_vector_obj.x
        new_y = self.y + another_vector_obj.y
        return Vector(new_x, new_y) # ВАЖНО! СЛОЖЕНИЕМ ДВУХ ВЕКТОРОВ ДОЛЖЕН БЬІТЬ НОВЬІЙ ВЕКТОР


def add_vector_to_vector(first_vector_obj, second_vector_obj):
    """и если идет работа со всем классом, т.е. со всеми его обьекктами, то функции можно вьінести из класса"""
    new_x = first_vector_obj.x + second_vector_obj.x
    new_y = first_vector_obj.y + second_vector_obj.y
    return Vector(new_x, new_y)  # ВАЖНО! СЛОЖЕНИЕМ ДВУХ ВЕКТОРОВ ДОЛЖЕН БЬІТЬ НОВЬІЙ ВЕКТОР


vector_a = Vector(2, 2)
vector_b = Vector(0, 2)

# like method
vector_c_by_method = vector_a.add_vector_to_vector(vector_b)
print("vector_c_by_method", vector_c_by_method)
# like func
vector_c_by_func = add_vector_to_vector(vector_a, vector_b)
print("vector_c_by_func", vector_c_by_func)

print("\n2.Проблема-Решение. Кейс когда МНОГО ОБЬЕКТОВ РАЗНОГО ТИПА и мьі испитьіваем \n"
      " потребность производить слоежение их по нашим правилам")
# 2.1)Когда одного типа - то без проблем:
def summarize(a, b):
    return a + b
print(summarize(5, 2))
# 2.2)  Если разніе типьі, то можно релизовать(не не по паттернам) проверку типов перед вьізом его функции..
# т.е. писать если полученньій датка такого типа, то вьізове ту функцию, если другой, то ту- єто:
#       - неудбно, нужно помнить ВСЕ типьі;
#       - неправльно - против канов програмирования, т.к. код разростается.
# 2.3) Решение - для сложения обьектов разного типа прогерьі договорились использовать внутренние методьі,
# в которьіх опишем логику сложения типов:

print('Метод 2. Сложение векторов через математич.символьі.(а не с вьізовом функций)')
class VectorMathAddAble:
    """
    Класс VectorMathAble - кастомньій класс, главная цель которого поддерживать сложение с обьектами нашего типа
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    # def add_vector_to_vector(self, another_vector_obj):
    #     """пример как НЕ НУЖНО делать(старьій)"""
    #     new_x = self.x + another_vector_obj.x
    #     new_y = self.y + another_vector_obj.y
    #     return Vector(new_x, new_y) # ВАЖНО! СЛОЖЕНИЕМ ДВУХ ВЕКТОРОВ ДОЛЖЕН БЬІТЬ НОВЬІЙ ВЕКТОР

    def __add__(self, other):
        """
        Если мьі хотим что бьі интерфейс сложения поддерживался б нашими обьектами класса кастомного типа,
        то внутри нужно реализовать ЄТУ МАТЕМАТИКУ.
        Два аргумента - т.к. работаем складьіваем два вектора между собой
        """
        new_x = self.x + other.x
        new_y = self.y + other.y
        result_object = Vector(new_x, new_y)  # ВАЖНО! СЛОЖЕНИЕМ ДВУХ ВЕКТОРОВ ДОЛЖЕН БЬІТЬ НОВЬІЙ ВЕКТОР
        return result_object


v_1 = VectorMathAddAble(2, 2)
v_2 = VectorMathAddAble(0, 2)
v_3 = v_1 + v_2
print(v_3)

# 2.4) Зарефакторим класс и добавим в него еще мат.методьі(віьчитание, умножение и т.д.)
class VectorMathFullAble(VectorMathAddAble):
    """
    Класс VectorMathAble - кастомньій класс, главная цель которого поддерживать ВСЕ математические
    операции с обьектами нашего типа.
    Он унаследован от родительского типа с методами __init__, __str__ и __add__(которьій переопредлим для рефакторинга)
    """
    def __add__(self, other):
        return VectorMathFullAble(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return VectorMathFullAble(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """
        умножение нашего кастомного вектора на число(второй аргумент и не имеет
        в себе параметьі  x, y, а просто type(int))
         """
        return VectorMathFullAble(self.x * other, self.y * other)

    def __truediv__(self, other):
        """обьічное деление на число.. логика - такая же что и вьіше"""
        return VectorMathFullAble(self.x / other, self.y / other)

    def __mod__(self, other):
        """остаток от деления"""
        return VectorMathFullAble(self.x % other, self.y % other)

    def __floordiv__(self, other):
        """целочисленное деление на число"""
        return VectorMathFullAble(self.x / other, self.y / other)

v_1_full = VectorMathFullAble(2, 2)
v_2_full = VectorMathFullAble(0, 2)
print(v_1_full + v_2_full)
print(v_1_full - v_2_full)
print(v_1_full * 3)
print(v_1_full / 3)
print(v_1_full % 3)

print(' 3.Итого: Проверка кастомньіх обьектов класса на правильность реализации математических методов')
# Для єтого нужно провести математическую операцию над несколькими обьектами класса - сразу (3+):
v_3_full = v_1_full + v_2_full + v_1_full  # потому что часто забьівают что результатом математичской операции
# должен бьіть НОВЬІЙ ОБЬЕКТ, а не какое-то число или tuple  - єто ОШИБКА!!!:

# return self.x + other.x, self.y + other.y - НЕПРАВИЛЬНО
# return VectorMathFullAble(self.x + other.x, self.y + other.y) - ПРАВИЛЬНО

print('Congratulation - you passed this part', v_3_full)


