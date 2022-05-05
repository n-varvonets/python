import math

# в примере видно, что одна функция использует табы, а другая пробелы - это может привести к ошибкам
# Code -> ReformatCode изменить все табы на пробелы и будет норм


def foo(value):
	if value == 10:
		raise ValueError('Incorrect value: {}'.format(value))
	return pow(10, value)


def bar(value):
    return pow(10, value)
