print("-----Универсальньій вид 'ДЕКОРАТОРА БЕЗ параметров'")
def outer(func):
    def inner(*args, **kwargs):
        print('наша одна и та же логика для всех прокинутьіх сюда функций')
        return func(*args, **kwargs)
    return inner


def div(a, b):
    return a / b

# 1.1)первьій пример вьізова декоратора
print(outer(div)(2, 3))
# 1.2)второй пример вьізова декоратора
my_var = outer(div)
print(my_var(1, 3))
# 1.3)третий пример вьізова декоратора - как синтаксический сахар (что бьі не записвать длинньій вьізов функции или
# помещать обьект функцию в переменную)
@outer
def div(a, b):  #  ВАЖНО понимать! @ сделал его не как функцию, а уже как переменную в которой храниться наш outer
    return a * b
print(div(2, 2))

"""2.1.) Задача: а как проинициалировать декорать? Допусим я хочу в логике измений прокинуть свой аргумент?"""
# 2.2.) Проблема: декоратор @outer ожидает функцию получить, а получает КАКОЙ_ТО параметр
# def outer(func, param):
#     def inner(*args, **kwargs):
#         print(param)
#         return func(*args, **kwargs)
#     return inner
# @outer("моя новая логика полученная как аргумент в декоратор")
# def div(a, b):  #  ВАЖНО понимать! @ сделал его не как функцию, а уже как переменную в которой храниться наш outer
#     print(my_new_logic)
#     return a * b
# print(div(2, 2))
# 2.3.) Решение: нужно обернуть наш декоратор во второй внешний декоратор
# def outer_second_decorator(param_for_my_dec_logic):
#     def outer(func):
#         def inner(*args, **kwargs):
#             print(param_for_my_dec_logic)
#             return func(*args, **kwargs)
#         return inner
#     return outer

# @outer_second_decorator('new logic')
# def div(a, b):  #  ВАЖНО понимать! @ сделал его не как функцию, а уже как переменную в которой храниться наш outer
#     return a * b
# print(div(2, 2))


print("-----Универсальньій вид 'ДЕКОРАТОРА С параметрами'")
def outer_second_decorator(*dargs, **dkwargs):
    def outer(func):
        def inner(*args, **kwargs):
            print(*dargs, **dkwargs)
            return func(*args, **kwargs)
        return inner
    return outer

def div_1(a, b):  #  ВАЖНО понимать! @ сделал его не как функцию, а уже как переменную в которой храниться наш outer
    return a / b

print('--- вьізов параметр декоратора через собачку, как синт сахар ---')
@outer_second_decorator('new logic')
def div_1(a, b):  #  ВАЖНО понимать! @ сделал его не как функцию, а уже как переменную в которой храниться наш outer
    return a * b
print(div(3, 3))



