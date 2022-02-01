import numpy

value1 = numpy.array([1, 2, 3, 4], dtype=numpy.float16)
value2 = numpy.array([1, 2, 3, 4], dtype=numpy.int8)
value3 = numpy.array([0, 2, 1, False], dtype=numpy.bool_)
value4 = numpy.array([[1, 2, 3], [3, 4, 5]], dtype=numpy.float16)
value5 = value4 > 2.5

print(value5)

print(value4.ndim)
print(value4.shape)
print(value4.size)
print(value4.dtype)
print(value4.itemsize)
print(value4.data)
print(value4.dtype.itemsize)
