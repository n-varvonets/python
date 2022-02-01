import numpy

print(numpy.sin(numpy.pi / 2))
print(numpy.sin(numpy.pi))
print(numpy.e)

print(numpy.absolute(1))
print(numpy.absolute(-10))
print(numpy.absolute(numpy.array([1, -20, 2, -100])))

a = numpy.array(
    [
        [1, 2],
        [5, 4]
    ],
    dtype=numpy.uint8
)

print('+', a + 2)
print('-', a - 2)
print('*', a * 2)
print('/', a / 2)
print('pow', a ** 2)
print('mul', a * a)
print('dot product', numpy.dot(a, a))

print('transpose 1', a.T)
print('transpose 2', a.transpose())
print('transpose 3', numpy.transpose(a))

print('Min', a.min())
print('Min (0)', a.min(axis=0))
print('Min (1)', a.min(axis=1))

print(a.max())
print(a.max(axis=0))
print(a.max(axis=1))

print('det', numpy.linalg.det(a))
print('multi dot', numpy.linalg.multi_dot([a, a, a]))
# https://docs.scipy.org/doc/numpy/reference/routines.linalg.html
