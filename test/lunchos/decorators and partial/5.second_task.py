"""
1.Декораторов может бьіть несколько.
2.Декорировать можно не только функции, но и классьі
"""

print("1.Декорирование нескольких декораторов.")
def second_decorator(*dargs, **dkwargs):
    def outer(func):
        def inner(*args, **kwargs):
            tempts = dkwargs['tempts']
            while tempts > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    print(f'Erorr: {err}, attempts left : {tempts} Func name - {func.__name__}')
                    tempts -= 1
        return inner
    return outer


my_var_for_dec = 4


def simple_decorator(func):
    def inner(a, b):
        print('---- ЗДЕСЬ логика для еще одного декоратора ----')
        return func(a, b)
    return inner


@simple_decorator
@second_decorator(tempts=my_var_for_dec)
def div(a, b):
    """В целевой функции в качстве ошибки можно взять деление на ноль: zerro divizion"""
    return a / b


print(div(3, 0))

