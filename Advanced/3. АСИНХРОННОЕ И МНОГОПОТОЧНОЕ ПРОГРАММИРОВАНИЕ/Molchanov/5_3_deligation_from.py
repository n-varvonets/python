from inspect import getgeneratorstate

"""
делегирующий генератор - это тот генератор, который вызывает другой генератор
подгенератор - вызываемый генератор
Зачем? Нужно когда нам один генератор нужно разбить на несколько генераторов
"""


def subgen():
    """создам ситающий генератор. он что-то читает из файла/сокета"""
    for i in 'nick':
        print('in subgen')
        yield i
        print('out subgen')


def delegator(g):  # транслятор, т.е. делегатор принимает генератор
    for i in g:
        print('in del')
        yield i
        print('out del')

sg = subgen()
d = delegator(sg)
print(next(d))
print(next(d))
print(next(d))