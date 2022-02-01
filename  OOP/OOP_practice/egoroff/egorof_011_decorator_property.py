class BankAccount:
    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом ')
        self.__balance = value

    # balance = property(fget=get_balance, fset=set_balance)

    my_balance = property()
    my_balance = my_balance.getter(get_balance)
    my_balance = my_balance.setter(set_balance)


acc1 = BankAccount("Ivan", 100)
print(acc1.my_balance)
acc1.my_balance = 200
print(acc1.my_balance)
print('---------1---------')

# сократим код property
class BankAccount2:
    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом ')
        self.__balance = value

    # balance = property(fget=get_balance, fset=set_balance)

    # класс property может принимать в себя сразу getter
    my_balance = property(get_balance)


acc2 = BankAccount2("Ivan2", 200)
print(acc2.get_balance())
print(acc2.my_balance)
print('---------2---------')

# навесим декоратор на property
class BankAccount3:
    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance

    @property
    def my_balance(self):
        return self.__balance

    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом ')
        self.__balance = value

    # т.к. get_balance - теперь свойство, то к свойству можно применить  setter
    my_balance = my_balance.setter(set_balance)  # свойство сеттера сохраняем в ту же переменную

acc3 = BankAccount3("Ivan3", 300)
print(acc3.my_balance)
acc3.my_balance = 100  # отлично - работает, но нам дотсупен так же метод set_balance
print(acc3.my_balance)
acc3.set_balance(150)  # и это плохо.. надо отсавить свойство для того что бы изменять значение...
print(acc3.my_balance)
### т.е. set_balance нужно сделать свойством
print('---------3---------')

"""
2) создам property  как декоратор с сеттером и убиранием функции
"""

class BankAccount4:
    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance

    @property
    def my_balance(self):
        return self.__balance

    #  1)мы уже имеем my_balance как свойство и назначим ему другое имя, что не избежать конфликта имен
    my_property_get_balance = my_balance

    # 2) и теперь делаем set_balance  в свойсвтво my_balance

    # def set_balance(self, value):
    #     if not isinstance(value, (int, float)):
    #         raise ValueError('Баланс должен быть числом ')
    #     self.__balance = value

    def my_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом ')
        self.__balance = value

    my_balance = my_property_get_balance.setter(my_balance)


acc4 = BankAccount4("Ivan4", 400)
print(acc4.my_balance)
acc4.my_balance = 444
print(acc4.my_balance)
# прикол в том что теперь отстствует метод set_balance и можем получать и менять значение balance
# acc4.set_balance = 555
print('---------4---------')

"""
3) но мы можем сократить код, навешав декоратор на метод setter, при этом избежав конфликта имен...
оно будет работать точно таким же образом
"""

class BankAccount5:
    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance

    @property
    def my_balance(self):
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом ')
        self.__balance = value


acc5 = BankAccount5("Ivan5", 500)
print(acc5.my_balance)
acc5.my_balance = 555
print(acc5.my_balance)
print('---------5---------')
