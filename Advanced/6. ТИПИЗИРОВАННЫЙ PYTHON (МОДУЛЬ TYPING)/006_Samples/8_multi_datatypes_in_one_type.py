from typing import Union, Tuple, Iterable

# если нам нужно принимать кортеж подмножеством значений -- т.е. либо то, либо то
# т.е. в отличии от TypeVar мы можем брать неоднородные, а четке указанные


def handler1(name: str, coefficient: Union[float, str]) -> None:
    print(name)
    print(coefficient)


def handler2(name: str, coefficient: Tuple[Union[float, str], ...]) -> None:  # все эелементы нашего кортежа
    # будут либо float либо str -мы определил с помощью ", ..." - т.е. неограниченное кол-во элементов (31,47 rows)
    print(name)
    print(coefficient)


def handler3(name: str, coefficient: Iterable[Union[float, str]]) -> None:
    """
    :param name:
    :param coefficient: в качестве коефа нам придет любой элемент, который будет типа [float, str]
    :return:
    """
    print(name)
    print(coefficient)


handler1("Test string", 10)
handler1("Test string", "10")
handler1("Test string", 10.2)
# handler1("Test string", 10.2, 10)  # дальше не пойдем, т.к. мы не указали ... в функции
# handler1("Test string", [])
# handler1("Test string", {})
# handler1("Test string", ())


handler2("Test string", (10,))
handler2("Test string", ("10", 12))
handler2("Test string", (10.2, 10))
handler2("Test string", (10.2, 10, "100"))  # нограниченное кол-во эелементов
handler2("Test string", (10.2, 12.0))

handler3("Test string", (10,))
handler3("Test string", ("10", 12))
handler3("Test string", [10.2, 10])
handler3("Test string", {10.2, 12.0})
handler3("Test string", "test")  # даже строка подходит, т.к. она итерируема
