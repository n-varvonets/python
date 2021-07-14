"""дескриптор - любой класс, в котором переопределчяем методы set,get,delete"""

class ImportantValues:
    def __init__(self, amount):
        self.amount = amount

    def __get__(self, obj, obj_type):
        return self.amount

    def __set__(self, obj, value):
        with open('log.txt', 'a') as f:  # 'w' - rewrite file, 'a' - add value to file, 'r' - read
            f.write(str(value))

        self.amount = value


class Account:
    amount = ImportantValues(100)

bobs_account = Account()
bobs_account.amount = 150

with open('log.txt', 'r') as f:
    print(f.read())

# 1)---------------------------------------------------------------------------------
"""один тот же метод возвращает разные обьекты, в зависимости от того как/кто ним обращается - это и есть ПОВЕДЕНИЕ ДЕСКРИПТОРА"""
class Class:
    def method(self):
        pass

obj = Class()

print(obj.method)  # <bound method Class.method of <__main__.Class object at 0x7f6f28d3fcf8>>
print(Class.method)  # <function Class.method at 0x7f6f28d342f0>

# 2)---------------------------------------------------------------------------------
"""@property - позволяет использовать"""

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} "qwe" {self.last_name}'

my_name = User("Nick", "Varvonets")

print(my_name.full_name) # >>> Nick "qwe" Varvonets... при вызове от обьекта, у нас вызывается ФУНКЦИЯ фул_нейм
print(User.full_name) # >>> <property object at 0x7f2963a6e458>... но когда обращаемся от класа, то у нас получиться обьект  типа property

# property -  реализован с помощью дескриптора

# 3)---------------------------------------------------------------------------------
"""можно написать свой @property"""

class Property:
    def __init__(self, getter): # сохраняем функцию, которую проперти получает
        self.getter = getter

    def __get__(self, obj, obj_type=None):
        if obj is None:  #  если обьект вызван от класса, то возвращаем самого себя
            return self

        return self.getter(obj)  # а если вызван наш атрибут с обьектом, то вызываем функцию

"""таким образом можно определить класс и использовать новый только что созданный декортатор проперти, так же.. - 
как и стандартный"""

class Class:
    @property
    def original(self):
        return 'original'

    @Property
    def custom_sugar(self):
        return 'custom sugar'

    def custom_pure(self):
        return 'custom pure'

    custom_pure = Property(custom_pure)

obj = Class()

#  и окажеться что они работают  едентично, потмоу что @property реализован как раз таки с помощью дескрипотора
print(obj.original)  # >>> original
print(obj.custom_sugar)  # >>> custom sugar
print(obj.custom_pure)  # >>> custom pure

# 4)---------------------------------------------------------------------------------
"""таким же образом можно написать свою реализацию  Staticmethod and ClassicMethod"""
class StaticMethod:
    def __init__(self, func):  # статик метод просто сохраняет функцию и...
        self.func = func

    def __get__(self, obj, obj_type):  # ... когда она вызывается - мы просто её возвращаем, потому что это  static method и не нужно передавать туда ни селф, ни класс
        return self.func

class ClassicMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, obj_type):  # когда мы вызываем нашу функцию от обьекта, т.е. obj_type == None
        if obj_type is None:
            obj_type = type(obj)

        def new_func(*args, **kwargs):
            return self.func(obj_type, *args, **kwargs)

        return new_func()




