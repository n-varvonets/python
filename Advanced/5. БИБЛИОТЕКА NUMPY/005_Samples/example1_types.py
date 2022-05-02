import numpy

value1 = numpy.int8(8)
print(value1, f'int8=2**8={2**8} - это диапзон чисел (-128, 127). До 127 - потому что 0 включительно')

value2 = numpy.int16(16)
print(value2, f'int16=2**16="{2**16}"=2**15+2**15="{2**15+2**15}" - это диапзон чисел (-{2**15}, {2**15-1}). -1 потому что 0 включительно')

value3 = numpy.uint8(2 ** 8 - 1)
print(f"{value3} - максимальное число uint8. Потому это сайн положительный и от нуля до 255 - ноль не забываем включать и отнимать его от общей суммы")

value4 = numpy.uint16(2 ** 16 - 1)
print(value4)

value5 = numpy.uint8([1, 3, 4, 10])
print(value5)

value6 = numpy.int_(2**63-1)
print(f"type(int_)=type(value6)={type(value6)},max_value={value6}, because 2**64=2**63+2**63={2**64}={2**63+2**63}")

value7 = numpy.int_(8)
print(value7)

value7 = numpy.bool_(8)
print(value7)

print(numpy.dtype('f4'))  #  создать флаоат
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
