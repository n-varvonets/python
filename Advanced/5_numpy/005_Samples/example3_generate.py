import numpy

value1 = numpy.arange(1, 20)
print(value1)

value2 = numpy.arange(0, 20, 5)
print(value2)

value3 = numpy.arange(20, 0, -5)
print(value3)

value4 = numpy.linspace(1, 5, 20)  # от единицы до пяти берет числа с вычисляемым
# шагом что бы было 20 ть шагов в этом диапазоне
print(value4)

value7 = numpy.linspace(1, 5, 9, dtype=numpy.int8)
print(value7)

value8 = numpy.random.random_integers(1, 100, 10)  # берем 10ть чисел от нуля до ста
print(value8)

value9 = numpy.random.rand(3, 4)  # генерирует матрицу три на четыре со случайными числами
print(value9)
