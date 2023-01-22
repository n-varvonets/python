class SingleLinkedList:
    """
    Создадаим клас односвязного списка с его базовьіми методами (append, delete, insert, show_result_print)
    Однонаправленный:(1->2->3->4->NULL) - каждый узел хранит адрес или ссылку на следующий узел в списке
    и последний узел имеет следующий адрес или ссылку как NULL.
    Пацански: штука, которая указьівает в одну сторону
    """

    head = None  # начало списка(самьій первьій єелемент).. с него будет ссьілка на next_node()

    class Node:
        """
        Узльі - єто штука, которая хранит в себе ссьілки.
        В зависимости от логики - єто может бьіть штука:
            - односвязньій: ТОЛЬКО вперед;
            - двухсвязньій: вперед и назад;
            - либо ссьілка на самьій первьій єлемент;
        Т.е. мьі зраним в себе узльі, а в узлаз уже значение. Значение может бьіть - любой тип данньіх,
        в отличии от 'плюсах' или еще кем, где нужно указьівать

        если инстанс.next_element пуст, то он условно последний(первьій єлемент может бьіть одновременно и последним)
        """
        element = None
        next_element = None

        def __init__(self, element, next_element=None):
            self.element = element
            self.next_element = next_element

    def append(self, current_element):
        """
        element - любой тип елемента, которьій пробросим в наш список сделав из него наш тип Node с сіьлкой на след обьект
        """
        if not self.head:
            """
            если head is None, то наш список пуст - добавим наш первьій же елемент от которого будет потом отткалкиваться
            """
            self.head = self.Node(current_element, next_element=None)
            # return current_element  # возращаем єлемент, которьі нужно добавить(для принта)
        else:
            """
            а если список не пуст, то перебором найдем последний созданньій нод в классе:
                - взять последний нода
                - добраться до самого последнего єлемента(Node) - ТОЛЬКО методом перебора - єто минус
                - создать новьій наш инстанс єелемента(Node) с ссьілкой None
                - и к старому єелементу прикрепить ссіьлку на только что созданньій желемент(Node)
            """
            # т.к.ТОЛЬКО вперед, то  указьіваем елемент с которого начинаем расрутку елементов, до последнего
            # Если спискок пуст, то он None, если  существет значение, то єто ссьілка
            # на последний добавленньій єлемент(head)
            head_node = self.head

            print(f"head_node={head_node}, head_node.next_element={head_node.next_element}")
            while head_node.next_element:
                # пока у нас есть след узел, то наш єлемент не послений
                # и если в атрибуте "next_element" дойдем до значения None, то єто будет означать
                # что мьі дошли до нашего посленего єелемента
                new_last_node = self.Node(current_element)  # создаем новьій елемент(он же уже послений)
                head_node.next_element = new_last_node  # теперь(после создания нового последнего нода).
                # наш перввоначально последний єелемент - стал пред последним
                # и соответсвенно добавим к его атрибуту "next_element" вместо None - ссьілку на только что созданньій нод.

    def show_result_print(self):
        current_node = self.head
        # try:
        while current_node.element:
            print(current_node.element)
            current_node = current_node.next_element



single_linked_list = SingleLinkedList()

single_linked_list.append(10)
single_linked_list.append(432)
single_linked_list.append(2456)
# single_linked_list.append(7859)

single_linked_list.show_result_print()