"""ЗАДАЧА"""
# Условие: напишите прамтризованньій доекратор, которьій принимат произвольное число аргументов и..
# в случае возникновения ошибки, он пьітается перезапустить еще функию n раз, где n -  параметр функции.


def second_decorator(*dargs, **dkwargs):
    def outer(func):
        def inner(*args, **kwargs):
            tempts = dkwargs['tempts']
            while tempts > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    print(f'Error: {err}. Left attempts {tempts}')
                    tempts -= 1
        return inner
    return outer


my_var_for_dec = 40


@second_decorator(tempts=my_var_for_dec)
def div(a, b):
    """В целевой функции в качстве ошибки можно взять деление на ноль: zerro divizion"""
    return a / b


print(div(3, 0))

