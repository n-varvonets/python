import numpy

a = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
a1 = a.reshape((2, 8))
print(a1)

a2 = a.reshape((2, -1))
print(a2)

a3 = a.reshape((4, -1))
print(a3)

a4 = a.reshape((8, -1))
print(a4)

a5 = a.reshape((2, 2, 4))
print(a5)

a6 = a.reshape((2, 2, -1))
print(a6)

print(a)
a.resize((4, 4))
print(a)

a.shape = (2, 8)
print(a)
