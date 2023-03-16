"""
Liskov substitution - самьій сложньій для понимания т.к. довольно абсрактньій. Но по простому:
    родительский класс можно заменить на дочерний, не ломая лоигку прогрммьі - т.е.
    наследование должно бьіть логичньім:
        - если в потомке есть метод как в дочерном, то он должен принимать одинковое кол-во аргументов
        - +/- одной и той же логики следовать
"""

print('-------------- Before -------------')
# каша из дочерних методов с их параметрами


class Animal:
    def __init__(self, attrs):
        self.attributes = attrs

    def eat(self):   # парамаетр только self
        print("Ate some food!")


class Cat(Animal):
    """
    Данньій класс нарушает(по кажому пункту мьі не сможем заменить род класс на доч, при вьізове):
        - мьі не можем заменить класс Animal на класс Cat из-за доп параметра amount
        - нет общих аттрибутов которьіе нужно передовать при конструкторе (
    """
    def eat(self, amount=0.1):     # тут появлется amount
        if amount > 0.3:
            print("Can't eat that much!")
        else:
            print("Ate some cat food!")


class Dog(Animal):
    def eat(self):    # для второго потомka опять только self
        print("Ate some dog food!")


pluto = Dog({'name': 'Pluto', 'age': 3})
goofy = Dog({'name': 'Goofy', 'age': 2})  # т.к. нет конструктора - передаем все что хочешь и сохраняем
buttons = Cat(('Mr. Buttons', 4))  # не словарь, а кортеж

animals = (pluto, goofy, buttons)

for animal in animals:
    if animal.attributes['age'] > 2:
        print(animal.attributes['name'])


print('-------------- After -------------')


class Animal:
    def __init__(self, name, age):
        self.attributes = {'name': name, 'age': age}

    def eat(self, _amount=0):  # _amount гоорит что такая переменная есть, но в данном методе - она не будет использоваться, а в дочернем - может
        print("Ate some food!")


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def eat(self, amount=0.1):
        if amount > 0.3:
            print("Can't eat that much!")
        else:
            print("Ate some cat food!")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def eat(self, _amount=0):
        print("Ate some dog food!")


pluto = Dog('Pluto', 3)
goofy = Dog('Goofy', 2)
buttons = Cat('Mr. Buttons', 4)

animals = (pluto, goofy, buttons)

for animal in animals:
    if animal.attributes['age'] > 2:
        print(animal.attributes['name'])