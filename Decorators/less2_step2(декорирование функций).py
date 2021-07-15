"""Декорирование методов Один из важных фактов, которые следует понимать, заключается в том, что
функции и методы в Python'e — это практически одно и то же, за исключением того, что методы всегда
ожидают первым параметром ссылку на сам объект (self). Это значит, что мы можем создавать декораторы
 для методов так же, как и для функций, просто не забывая про self."""

def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3  # действительно, дружелюбно - снизим возраст ещё сильней :-)
        return method_to_decorate(self, lie)

    return wrapper

class Lucy(object):

    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print("Мне %s, а ты бы сколько дал?" % (self.age + lie))

l = Lucy()
l.sayYourAge(0)  # выведет: Мне 29, а ты бы сколько дал?
# в аргументе передали вопзраст на которой мы лично хотим обмануть (- , =0 , +)
print('----------------------------------------------------')

"""Конечно, если мы создаём максимально общий декоратор и хотим, чтобы его можно было
применить к любой функции или методу, то стоит воспользоваться тем, что *args распаковывает
список args, а **kwargs распаковывает словарь kwargs:"""


def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # Данная "обёртка" принимает любые аргументы
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("Передали ли мне что-нибудь?:")
        print(args)
        print(kwargs)
        # Теперь мы распакуем *args и **kwargs
        function_to_decorate(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("Python is cool, no argument here.")

function_with_no_argument()  # выведет:
# Передали ли мне что-нибудь?:
# ()
# {}
# Python is cool, no argument here.
print('----------------------------------------------------')

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)

function_with_arguments(1, 2, 3)  # выведет:
# Передали ли мне что-нибудь?:
# (1, 2, 3)
# {}
# 1 2 3
print('----------------------------------------------------')

@a_decorator_passing_arbitrary_arguments
def function_with_named_arguments(a, b, c, platypus="Почему нет?"):
    print("Любят ли %s, %s и %s утконосов? %s" %(a, b, c, platypus))

function_with_named_arguments("Билл", "Линус", "Стив", platypus="Определенно!")  # выведет:
# Передали ли мне что-нибудь?:
# ('Билл', 'Линус', 'Стив')
# {'platypus': 'Определенно!'}
# Любят ли Билл, Линус и Стив утконосов? Определенно!
print('----------------------------------------------------')

class Mary(object):

    def __init__(self):
        self.age = 31

    @a_decorator_passing_arbitrary_arguments
    def sayYourAge(self, lie=-3):  # Теперь мы можем указать значение по умолчанию
        print("Мне %s, а ты бы сколько дал?" % (self.age + lie))


m = Mary()
m.sayYourAge()  # выведет:
# Передали ли мне что-нибудь?:
# (<__main__ .Mary object at 0xb7d303ac>,)
# {}
# Мне 28, а ты бы сколько дал?


