def second_decorator(*dargs, **dkwargs):  # ПАРАМЕТРЬІ ДЕКОРАТОРА
    def outer(func):  # САМА ДЕКОРИРУЕМАЯ ФУНКЦИЯ
        def inner(*args, **kwargs):  # ПАРАМЕРЬІ ФУНКЦИЙ
            print(*dargs, **dkwargs)
            print('Наша логика. СЮДА все поведение для изменений!!!!')
            return func(*args, **kwargs)
        return inner
    return outer


my_var_for_dec = 'my tricky var for decortor as parametr'


print("\n---------- 1. Первьій способ через ПАТТЕРН проектирования")
def div(a, b):
    return a / b
print(second_decorator(my_var_for_dec)(div)(2, 3))


print("\n---------- 2.Второй способ - через синтаксический сахар")
@second_decorator(my_var_for_dec)
def div_1(a, b):  #  ВАЖНО понимать! @ сделал его не как функцию, а уже как переменную в которой храниться наш outer
    return a * b
print(div_1(3, 3))


