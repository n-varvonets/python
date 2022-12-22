"""
1.Декораторов может бьіть несколько.
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


# print(div(3, 0))

print(' ---- ВАЖНО. Последовательность вьіплнения декоратора  ---- ')
# моммент.№1. Когда у нас есть параметризованньій декоратор(@second_decorator(tempts=my_var_for_dec)),
# то перьім делом запускается то что в скобках - (tempts=my_var_for_dec).
# моммент.№2. Ее результатом должен бьіть обькт функции(return outer), которьій уже декорирует
# нашу целевую функцию(div). Т.е. если переписать ее после вьіполнения, то вьіглядит будет примерно так:
# @simple_decorator
# @outer
# def div(a, b):
#     return a / b
# моммент.№3. Дальше наш outer принимает нашу целевую функцию div: def outer(func):
# моммент.№4. Область видимости: def inner(*args, **kwargs) уже знает что мьі внутри используем нашу
# функцию. Все что осталось сделать - єто принять параметрьі и добавить нашу логику
# моммент.№5. Резуьтатом работьі будет inner как обьект(не запущен). И єтот inner  передается внутрь  декоратра
# def simple_decorator(func): и будет иметь примерно такой вид:
# @simple_decorator
# def inner(div  ):

@second_decorator(tempts=my_var_for_dec)
@simple_decorator
def div(a, b):
    """В целевой функции в качстве ошибки можно взять деление на ноль: zerro divizion"""
    return a / b
print(div(3, 0))

