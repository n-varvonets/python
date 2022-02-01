import numpy

value1 = numpy.ones([3, 4], dtype=numpy.uint8)
value2 = numpy.ones_like(value1)
value3 = numpy.ones_like(
    [
        [1, 2, 3],
        [3, 2, 1]
    ]
)
print(value1)
print(value2)
print(value3)

value4 = numpy.zeros([3, 4], dtype=numpy.uint8)
value5 = numpy.zeros_like(value4)
value6 = numpy.zeros_like(
    [
        [1, 2, 3],
        [3, 2, 1]
    ]
)
print(value4)
print(value5)
print(value6)

value7 = numpy.empty([3, 4], dtype=numpy.uint8)
value8 = numpy.empty_like(value7)
print(value7)
print(value8)

value9 = numpy.eye(4)
print(value9)

value10 = numpy.eye(3)
print(value10)

value11 = numpy.eye(4, k=-1)
print(value11)
