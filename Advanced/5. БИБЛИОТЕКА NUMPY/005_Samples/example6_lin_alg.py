import numpy

print(numpy.pi)
print(numpy.sin(numpy.pi / 2))
print(numpy.sin(numpy.pi))
print(numpy.e)  # наверно експонента

print(numpy.absolute(1))
print(numpy.absolute(-10))
print(numpy.absolute(numpy.array([1, -20, 2, -100])))   #  делает положительными все значения

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
print('dot product', numpy.dot(a, a))  # сть особоая формула для перемножения матриц - она реализована в dot()
# dot product [[11 10]
#  [25 26]]
# [1, 2]   *   [1, 2]
# [5, 4]   *   [5, 4]
# [1*1+2*5 1*2+2*8]
# [5*1+4*5 5*2+4*4]

# три варианта транспонировать значения, т.е. сделать перевенуть значения
print('transpose 1', a.T)
print('transpose 2', a.transpose())
print('transpose 3', numpy.transpose(a))

# найти минимальный элемент во всей матрицы и рамках столбца
print('Min', a.min())
print('Min (0)', a.min(axis=0))
print('Min (1)', a.min(axis=1))

print(a.max())
print(a.max(axis=0))
print(a.max(axis=1))

print('det', numpy.linalg.det(a))  # >>> -6, где  det(a) - вычислить модуль матрицы:
# [1, 2],
# [5, 4]
# произведение элементов диагонали и разность между ними: 1*4-5*2 = -6

print('multi dot', numpy.linalg.multi_dot([a, a, a]))  # перемножаем матрицы
# https://docs.scipy.org/doc/numpy/reference/routines.linalg.html
