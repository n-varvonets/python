print('Задача.1')  # перед каждьім созданием екземпляра класса у нас вьіводилась приветсвие
def greeting_decorator(my_class):
    def inner(*args, **kwargs):
        print('Hello world')
        return my_class(*args, **kwargs)
    return inner

class MyClass:
    print('s')
greeting_decorator(MyClass)()

@greeting_decorator
class MyClass2:
    print('q')
MyClass2()

print('Задача.2')  # Зачем нам єто нужно?
# Предствим, что мьі хотим поставимть пароль на создание єкземпляров класса.
# Пускай у нас будет секретньій пароль, которьій будем передавать в декоратор для проверки на валидность

client_pass = input()

def check_password_for_access(*dargs, **dkwargs):
    def decorator(my_class):
        def inner(*args, **kwargs):
            valid_secret_pass = "password_ololo"
            received_pass = dkwargs['password_for_checking']
            if received_pass == valid_secret_pass:
                print('Instance was created')
                return my_class(*args, **kwargs)
            else:
                raise ValueError(f'Password is NOT incorrect')
        return inner
    return decorator


@check_password_for_access(password_for_checking=client_pass)
class ClassUnderPass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


inst = ClassUnderPass(1, 2)
print(inst.a)