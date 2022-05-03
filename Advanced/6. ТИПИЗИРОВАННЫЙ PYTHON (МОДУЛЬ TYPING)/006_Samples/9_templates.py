from typing import TypeVar, Dict

# шаблонные типы

T = TypeVar('T')  # это как [Any], но мы даем ему имя

TemplateDict = Dict[str, T]  # даем наш темплейт
IntDict = TemplateDict[int]  # Dict[str, int] - темплейт кт от интов
StrDict = TemplateDict[str]  # Dict[str, str]


def handler1(value: TemplateDict[T]) -> T:  # абсолютно любой тип для значений дикта
    return list(value.values())[0]


def handler2(value: IntDict) -> int:
    return list(value.values())[0]


value1: int = handler1({'test': 10})
value2: str = handler1({'test': 'str'})
value3: list = handler1({'test': []})
value4: int = handler2({'test': 10})
# value5: int = handler2({'test': 'str'})
