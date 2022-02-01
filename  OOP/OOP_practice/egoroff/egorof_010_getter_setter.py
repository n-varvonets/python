
"""   ~~~ Property. getter-метод и setter-метод~~~
1) Хотим предоставить неуий интерфейс длоя того что получить доступ к нашей переменной
"""

class BankAccount:
    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        self.__balance = value


acc1 = BankAccount("Nick", 100)
print(acc1.get_balance(), acc1.__dict__)
acc1.set_balance(50)
print(acc1.get_balance(), acc1.__dict__)
print("--------------1-------------")

# но есть момент если в баланс передать строку, а не число, то он корректно отработает
acc1.set_balance("balance - string, not int")
print(acc1.get_balance(), acc1.__dict__)
print('--------------2--------------')

# это решается тем что бы добавить isintance  перед  setter-ом
class BankAccount2:
    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            return print('the value should be int, float')  # можно запринтовать.. а можно и вызвать ошибку  raise-ом.
            # Но лучше использовать raise, потому что fget  не долджно возращать значение(смю стр. 69 )
            # raise ValueError('Баланс должен быть числом ')
        self.__balance = value


acc2 = BankAccount2("Nick2", 200)
print(acc2.get_balance(), acc2.__dict__)
acc2.set_balance('balance - string, not int')
print(acc2.get_balance(), acc2.__dict__)
print('------------3-------------')

# но проблема в том что вызывать такие методы get_balance и set_balance - интуитивно непонятно.. поэтому есть метод property

"""
2) первый простой способо property
"""


class BankAccount3:
    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            # return print('the value should be int, float')  #  таким образом property будет кидать ошибку
            raise ValueError('Баланс должен быть числом ')
        self.__balance = value

    balance = property(fget=get_balance, fset=set_balance)


acc3 = BankAccount3("Nick3", 300)
print(acc3.balance)  # сейчас уже заработает, потому что мы уже будет обращаться не к атрибуту __balance, а к свойству balance(стр.73).
# Таким образом мы получим доступ к защищенному аттрибуту + мы обращаемся как к атрибуту(без скобок)
acc3.balance = 333
print(acc3.get_balance(), acc3.__dict__)
print('------------4-------------')



