class DoubleLinkedList:
    class Node:

        index = None
        previous_node = None
        next_node = None
        element = None

        def __init__(self, element, next_node=None, previous_node=None):
            self.element = element
            self.next_node = next_node
            self.previous_node = previous_node

            self.index = DoubleLinkedList.length
            DoubleLinkedList.length += 1

    head = None
    tail = None
    length = 0

    def add(self,   element):
        if not self.head:
            self.head = self.Node(element)

        elif not self.tail:
            self.tail = self.Node(element, previous_node=self.head)
            self.head.next_node = self.tail

        else:
            prev_node = self.tail
            self.tail = self.Node(element, previous_node=prev_node)
            prev_node.next_node = self.tail

    def __next__(self):
        print('here')
        return self

    def __iter__(self):
        first_or_working_node = self.head
        while first_or_working_node:
            yield first_or_working_node.element
            first_or_working_node = first_or_working_node.next_node


    # def show_result_print(self):
    #     first_or_working_node = self.head
    #     while first_or_working_node.next_node:
    #         print(f"index: {first_or_working_node.index}, element: {first_or_working_node.element}")
    #         first_or_working_node = first_or_working_node.next_node
    #     print(f"index: {first_or_working_node.index}, element: {first_or_working_node.element}")


if __name__ == "__main__":
    double_linked_list = DoubleLinkedList()

    double_linked_list.add(123)
    double_linked_list.add(3888)
    double_linked_list.add("my_string_type_data")
    double_linked_list.add([1, 2, "3", 4])

    """
    Проблема вопроса и почему:
    1. Можно вьівести значения єлементов функции с помощью специальнго метода,
    2. А можно сделать из нашего списка - крутой список с обходом(итерабилностью) нашего обьекта
    списка не через while, а через for и next() - т.е. НЕ через специ метода из п.1.
    """
    # double_linked_list.show_result_print()

    """Момент.№1: __next__
    метод __next__ в классе - єто то делать, когда к обьекту класса кто-то применил функцию next()"""
    # print(next(double_linked_list))

    """Момент.№2: __iter__
    Логика реализации: 
          1) сначала реализуется логика в методе __итер__ при пробросе нашего инстанса_класса в метод iter() 
          2) теперь наш инстанса_класса становится генератором, т.е. к нему можно применять метод next() 
          3) при вьізове метода next() в него пробрасьівается аргумент возращенньій из __iter__"""
    # iter_db_list_linked = iter(double_linked_list)
    # try:
    #     while True:
    #         next_val = next(iter_db_list_linked)
    #         print("Очередное значение:", next_val)
    # except StopIteration:
    #     # явно напечатаем сообщение об окончании итерации,
    #     # хотя цикл for этого не делает и ошибка просто подавляется
    #     print("Итерация закончена")
    # print("Программа завершена")

    """Момент.№3: Собасна и результат  реализации __iter__  использовать его в цикле for"""
    for el in double_linked_list:
        print(el)



