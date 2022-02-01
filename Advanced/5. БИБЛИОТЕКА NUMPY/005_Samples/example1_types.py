import numpy

value1 = numpy.int8(8)
print(value1)

value2 = numpy.int16(16)
print(value2)

value3 = numpy.uint8(2 ** 8 - 1)
print(value3)

value4 = numpy.uint16(2 ** 16 - 1)
print(value4)

value5 = numpy.uint8([1, 3, 4, 10])
print(value5)

value6 = numpy.int_(65536)
print(value6)

value7 = numpy.int_(8)
print(value7)

value7 = numpy.bool_(8)
print(value7)

print(numpy.dtype('f4'))
print(numpy.dtype('f8'))
print(numpy.dtype('f'))

print(numpy.dtype('i1'))
print(numpy.dtype('i2'))
print(numpy.dtype('i4'))
print(numpy.dtype('i8'))
print(numpy.dtype('i'))

print(numpy.dtype('u1'))
print(numpy.dtype('u2'))
print(numpy.dtype('u4'))
print(numpy.dtype('u8'))

print(numpy.dtype('U3'))
print(numpy.dtype('?'))

print(numpy.uint8(-1))
print(numpy.uint8(-2))
print(numpy.uint8(-10))
