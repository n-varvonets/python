from typing import TypeVar, List, Tuple, Sequence, Iterable

IntOrStr = TypeVar('IntOrStr', int, str, float)  # можем определить свой тип, который включает
# свои типы - обязательно однородные типы(либо все int, либо все str, либо же все float)
T = TypeVar('T')  # говорит что используют всевозможные значения. Он нужен, что бы можно
# было достучаться до какого-то вложенного элемента, как в copy_list()


def copy_list_0(sequence: Iterable[IntOrStr]) -> List[IntOrStr]:
    # тип Iterable - означает что мы можем итерировать по какой-то последовательности,
    # а каждый элемент будет одним из типов(int, str, float) созданного типа Iterable
    new_list: List[IntOrStr] = []
    for elem in sequence:
        new_list.append(elem)
    return new_list


def copy_list(sequence: Iterable[Tuple[str, T]]) -> List[T]:
    new_list: List[T] = []
    for elem in sequence:
        new_list.append(elem[1])
    return new_list


test_value1 = copy_list_0([1, 2, 3])
test_value2 = copy_list_0([1, 2, 9])
test_value3 = copy_list_0([1.3, 2.1, 3])
test_value4 = copy_list_0(["srt", "rts", "str"])
test_value5 = copy_list_0(("srt", 5, "s tr"))  # только здесь mypy кинет ошибку, т.к. не однородные данные
test_value6 = copy_list_0({"srt", "5", "[]"})

test_data = [
    ('1', 10),
    ('1', 10),
    ('1', '1'),
]
test_value0 = copy_list(test_data)

