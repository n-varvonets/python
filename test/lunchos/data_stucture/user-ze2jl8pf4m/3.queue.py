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
        next_node: Optional = None

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
        if not self.head:
            self.head = self.Node(element)
        else:
            node = self.head
            while node.next_node:
                node = node.next_node

            node.next_node = self.Node(element)

    def pop(self) -> Any:
        """
        Вернуть первьій елемент из очереди
        :return:
        """
        try:
            element = self.head.element
        except AttributeError:
            raise AttributeError('Нельзя взять аттрибут из пустой очереди')
        self.head = self.head.next_node
        return element

    @property
    def is_empty(self) -> bool:
        """
        property - потмоу никаких параметров он не принимает
        и по сути является скорее свойством, чем методом
        Если головьі не будет, то будет  None, а None для bool - єто false,
        а по лгике - наоборот: если список пуст, то нужно возращать true
        """
        return not bool(self.head)

    def show_result_print(self):
        list_els = []
        first_or_working_node = self.head
        while first_or_working_node.next_node:
            list_els.append(first_or_working_node.element)
            first_or_working_node = first_or_working_node.next_node
        list_els.append(first_or_working_node.element)
        print(list_els)


def main():
    queue = Queue()
    queue.add(123)
    queue.add("my_string")
    queue.add({"my_key": 4444})
    queue.add(["my_list_string", 666666])
    queue.show_result_print()

    first_element = queue.pop()
    print(f'\nfirst element = {first_element}and now aur list looks like')
    queue.show_result_print()

    # проврка обработки исклчения пустой очереди
    queue.pop()
    queue.pop()
    queue.pop()
    # queue.pop()  # AttributeError: Нельзя взять аттрибут из пустой очереди

    print(queue.is_empty)  # -> True


if __name__ == "__main__":
    main()