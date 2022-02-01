import math


def foo(value):
	if value == 10:
		raise ValueError('Incorrect value: {}'.format(value))
	return pow(10, value)


def bar(value):
    return pow(10, value)
