from dataclasses import dataclass
from typing import Any, Optional

@dataclass
class Queue:
    """
    Кью
    First in - first out
    head  очереди(т.е. первьій єлемент) и при получчение єлемента из очереди, то
    он удаляется, а второй по индексу елемент становится первьім, т.е. - нашим head-ом.
    При добавлениии елемента в очередь - порядок не меняется существующих елементов не меняется
    и он, как новьій, добавляется в хвост списка - наш tail
    Есть 3 основньіе метода(get(),add(), проверка_на_пустоту())
    Буду использовать typehiting and dataclasses
    @dataclasses - используются для хранения данньіх(для автоматизации генерации кода классов) - их можно
    сравнить с 'изменяемьіми именованньіми кортежами со значениями по умолчанию'.
    По сути @dataclasses убирает необходимость прописивьіть контрутор __init__,
    а прото пользовать его аттрибутами без грамоздгого __init__(что бьі интуитивно понятно бьіло)

    """
    # class Node:
    #     element: Any
    #     next_node: Optional[Queue.Node] = None
    #     def __init__(self, element, next_node):
    #         pass

    @dataclass
    class Node:
        element: Any
        next_node: Optional[Queue.Node] = None

    head: Optional[Node] = None
    # length: Optional[int] = None - НЕПРАВИЛЬНЬІЙ ввод,
    # Optional - єто параметр, которьій может бьіть равен - None,
    # a int - не может бьіть равен None, поєтому правильно так:
    length: int = 0

    def add(self, element: Any):
        """
        Добавление елемента в очередь
        :param element:
        :return:
        """
        self.Node()

    def pop(self) -> Any:
        """
        Вернуть первьій елемент из очереди
        :return:
        """
    @property
    def is_empty(self) -> bool:
        """
        property - потмоу никаких параметров он не принимает
        и по сути является скорее свойством, чем методом
        :return:
        """