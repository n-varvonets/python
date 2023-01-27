class DoubleLinkedList:
    class Node:
        """
        Блаодаря previous_node будет намного удобней:
            - удалять
            - вставлять: два узла разьеденить и вставить туда єлемент
        """
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
            """
            если head is None, тогда  список еще пуст,
            добавим первьій наш елемент в начало списка на место head.
            у первого елемента не будет ссіьлок на предеущий и следующий  нод 
            """
            self.head = self.Node(element)
        elif not self.tail:
            """
            если нет хвоста, то у нас УЖЕ ЕСТЬ ОДИН ЕЛЕМЕНТ в списке, тогда
            создадим новьій елемент,поместим его воторьім в список как последний елемент в списк - наш tail:
                - у єтого нода будет ссьілка на первьій елемент;
                - нужно первому ноду указать ссьілку next_node на только чт  созданньі второй елемент

            єто нужно для поиска последнего узла:
                - бістрее будет через условия узнать посл елемент,
                - чем проводить поиск перебором сначалала
            """
            self.tail = self.Node(element, previous_node=self.head)
            self.head.next_node = self.tail

        else:
            """
            во всех осталььіх случаях у нас список не пуст и содержит
            как минимум два елемента - наши head, tail.
            
            т.к. по нашей логике мьі НЕ вставляем(т.е. НЕ insert-им в середину списка),
            а добавляем(add() в конец списка), то реализация будет следуюшая:
                - к нашему хвосту добавим ссьілку на только что созданньій єелемент и теперь о будет нашим хвостом 
            """
            prev_node = self.tail
            self.tail = self.Node(element, previous_node=prev_node)
            prev_node.next_node = self.tail

    def __iter__(self):
        first_or_working_node = self.head

        print(f"first_or_working_node = {first_or_working_node}, first_or_working_node.next_node = {first_or_working_node.next_node}")
        # while first_or_working_node.next_node:

        while first_or_working_node:
            yield first_or_working_node.element
            first_or_working_node = first_or_working_node.next_node


if __name__ == "__main__":
    double_linked_list = DoubleLinkedList()

    double_linked_list.add(123)
    double_linked_list.add(3888)
    double_linked_list.add("my_string_type_data")
    double_linked_list.add([1, 2, "3", 4])

    for el in double_linked_list:
        print(el)

