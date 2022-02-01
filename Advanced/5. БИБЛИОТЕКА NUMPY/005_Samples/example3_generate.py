import numpy

value1 = numpy.arange(1, 20)
print(value1)

value2 = numpy.arange(0, 20, 5)
print(value2)

value3 = numpy.arange(20, 0, -5)
print(value3)

value4 = numpy.linspace(1, 5, 20)
print(value4)

value7 = numpy.linspace(1, 5, 9, dtype=numpy.int8)
print(value7)

value8 = numpy.random.random_integers(1, 100, 10)
print(value8)

value9 = numpy.random.rand(3, 4)
print(value9)
