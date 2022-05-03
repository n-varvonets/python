from typing import TypeVar, Dict, ClassVar


class User:
    meta: ClassVar[Dict[str, int]]

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


user = User('test1', 'test2')
# user.meta = {}  # неверно потому что нельзя через экземпляр присваивать значение атрибута класса
User.meta = {}   # а через сам класс - можно присвоить новое значение аттрибута ClassVar -КЛАСС


""" обрамляем в кавычки если данный тип не определен, то обрамляем их в кавычки и IDE это поймет"""
class A:
    def foo(self, instance: 'B'):  #  что бы избежать момента определения класса ниже, то может взять в кавычки, тем
        # самым сказать что инстанс класса B т определен ниже
        pass


class B:
    def foo(self, instance: 'A'):
        pass


a1 = A()
b1 = B()

b1.foo(a1)
a1.foo(b1)
# a1.foo(a1)
