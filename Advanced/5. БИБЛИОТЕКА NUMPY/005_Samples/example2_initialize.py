import numpy

value1 = numpy.array([1, 2, 3, 4], dtype=numpy.float16)
value2 = numpy.array([1, 2, 3, 4], dtype=numpy.int8)
value3 = numpy.array([0, 2, 1, False], dtype=numpy.bool_)
value4 = numpy.array([[1, 2, 3], [3, 4, 3]], dtype=numpy.float16)
value5 = value4 > 2.5  # сранивает каждое число в массиве больше ли 2,5 или нет

print(value5)

print(value4.ndim)  # вывовдить кол-во измерений. не путать с кол-вом рядков. это скорее вложений [3, 4, [1, 2], 8]
print(value4.shape)  # мерность (строк, столбцов)
print(value4.size)  # кол-во елементов в массиве
print(value4.dtype)
print(value4.itemsize)  # бАЙтовый размер занимаемого файла. float16 = 16 бит = 16/8 байта = 2 байта
print(value4.data)
print(value4.dtype.itemsize)
