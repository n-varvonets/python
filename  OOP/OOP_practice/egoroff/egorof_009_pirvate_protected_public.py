"""
1) обычные функции/методы/атрс ничем не отличаются от protected...
только дают понять прогеру что луше к ним обращаться с класса, а не с интанса
"""

class BankAccount:
    def __init__(self, name, age, balance, passport):
        self._name = name
        self._age = age
        self._balance = balance
        self._passport = passport

    def print_protected_info_account(self):
        print(f"name is {self._name}, age is {self._age}, balance is {self._balance}, passport is {self._passport}")


# acc0 = BankAccount("Tom", 18, 100000, 7894325146)
# acc0.print_protected_info_account()
# print(acc0.__dict__, BankAccount.__dict__, acc0._name)  # хоть и статус  protected, то все равно обратиться
# с инстанса - нарушет правило сокрытия данных и возможностью изменять аттрибуты класса только методами класса


"""
2) ~~~ private - инкапсуляция ~~~
"""

class BankAccount1:
    def __init__(self, name, age, balance, passport):
        self.__name = name
        self.__age = age
        self.__balance = balance
        self.__passport = passport

    def print_private_info_account(self):
        print(f"name is {self.__name}, age is {self.__age}, balance is {self.__balance}, passport is {self.__passport}")


# acc1 = BankAccount1("Jack", 24, 44444, 645645654)
# acc1.print_private_info_account()
# print(acc1.__name)  # - в данном случае уже будет выдавать ошибку, потому что __name - уже приватная - ИНКАПСУЛЯЦИЯ в деле

"""
3) ~~~ private - инкапсуляция  с методами~~~
"""

class BankAccount_methods:
    def __init__(self, name, age, balance, passport):
        self.__name = name
        self.__age = age
        self.__balance = balance
        self.__passport = passport

    def print_protected_data(self):
        self.__print_private_info_account()

    def __print_private_info_account(self):
        print(f"name is {self.__name}, age is {self.__age}, balance is {self.__balance}, passport is {self.__passport}")


acc_meth = BankAccount_methods("Jack", 24, 44444, 645645654)
acc_meth.print_protected_data()

"""
4) ~~~ но все же есть возможность получить скрытые аттрибуты ~~~ 
"""

print(dir(acc_meth))  # >>> ['_BankAccount_methods__age', '_BankAccount_methods__balance', ...
print(acc_meth._BankAccount_methods__balance)
print(acc_meth._BankAccount_methods__print_private_info_account())




