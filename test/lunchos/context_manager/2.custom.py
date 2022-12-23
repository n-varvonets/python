# 1.1) Задача: создадим свой кастомньій контекстньій менеджер.
# 1.2) Если в своем кастомном классе не реализовать __enter__, то контекстньій менеджер при его вьізове прокинет ошибку  __enter__.

class MyClass:
    def __enter__(self):
        print("метод __enter__")

    def __exit__(self, exc_type, exc_val, exc_tb):  #  exc_val - смс искоючения, exc_tb - трейсбек обьекта
        print("метод __exit__")


my_o = MyClass()

with my_o:
    print('context')
    raise ZeroDivisionError

