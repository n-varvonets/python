# from sSt import StringIO
from io import BytesIO, StringIO

import numpy

data1 = '1 2 3\n4 5 6'
results1 = numpy.genfromtxt(StringIO(data1))
print(results1)

data2 = b'1, 2, 3\n4, 5, 6'
results2 = numpy.genfromtxt(BytesIO(data2), delimiter=',')
print(results2)

data3 = '1, 2, 3\n4, 5, 6'
results3 = numpy.genfromtxt(StringIO(data3), delimiter=',', dtype=numpy.int16)
print(results3)

data4 = ' 1 2 3\n4 5 6'
results4 = numpy.genfromtxt(StringIO(data4), delimiter=2, dtype=numpy.int16)
print(results4)

data5 = '190 2 3\n 40 5 6'
results5 = numpy.genfromtxt(StringIO(data5), delimiter=(3, 2, 2))
print(results5)

data6 = '190 2 3\n 40 5 6'
results6 = numpy.genfromtxt(StringIO(data6), delimiter=(3, 2, 2),
                            usecols=(0, 2))
print(results6)

data7 = """
# it's comment
190 2 3
40 5 6"""
results7 = numpy.genfromtxt(StringIO(data7),
                            comments="#")
print(results7)

data8 = """
it's header
190 2 3
40 5 6"""
results8 = numpy.genfromtxt(StringIO(data8),
                            skip_header=2)
print(results8)

data9 = """
190 2 3.45
40 5 6.98"""
results9 = numpy.genfromtxt(StringIO(data9),
                            dtype=(numpy.uint8, numpy.uint8, numpy.float16))
print(results9)

numpy.savetxt('test.csv', results9, fmt='%s')
