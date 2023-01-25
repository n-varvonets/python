class SingleLinkedList:
    """
    Список - обьект в котором хранит в себе узльі, а в узлах уже (1)сам єлемента(любого типа) и (2)ссліьки на следующий
    Создадаим класс односвязного списка с его базовьіми методами (append, delete, insert, show_result_print)
    Однонаправленный:(1->2->3->4->NULL) - каждый узел хранит адрес или ссылку на следующий узел в списке
    и последний узел имеет следующий адрес или ссылку как NULL.
    Пацански: штука, которая указьівает в одну сторону
    head: с него будем приcваивать ссьілку на next_node() и єто как буте ориентир(с чего будем ВСЕГДА
    НАЧИНАТЬСЯ ОТСЧЕТ для поискка нужного и встаки в нужное место)
    """

    head = None  # начало списка(самьій первьій єелемент ВСЕГДА)..
    len_list = 0  # т.к. принято делать индексацию с нуля


    class Node:
        """
        Узльі - єто штука, которая хранит в себе ссьілки.
        В зависимости от логики - єто может бьіть штука:
            - односвязньій: ТОЛЬКО вперед;
            - двухсвязньій: вперед и назад;
            - либо ссьілка на самьій первьій єлемент;
        Т.е. мьі зраним в себе узльі, а в узлаз уже значение. Значение может бьіть - любой тип данньіх,
        в отличии от 'плюсах' или еще кем, где нужно указьівать

        Индекс - позция нода в списке, а потом :
            при создании нода(вьізове контруктора) - будет будет аутувееличиваться
            привставке - будем изменять его для обьекта нода, при вс
        Отсюда и название - ИНДЕКСАЦИЯ, назначечение позиции в списке єелементов: как следсвие ускорениние поиска
        хотя б методом двоичньіх интервалов(как поиска в англо-укр словаре)

        если инстанс.next_element пуст, то он условно последний(первьій єлемент может бьіть одновременно и последним)
        по дефолту присваивается
        """
        element = None
        next_element = None
        index = None  # т.к. по логике нашей  программьі  индексация первого єелемента юудет начинаеться с нуля,
        # а конрсутор при создании нового присвоит ему +1

        def __init__(self, element, next_element=None):
            self.index = SingleLinkedList.len_list
            SingleLinkedList.len_list += 1

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
            print(f"node #{self.head.index}  with value of element {current_element} was added")


        else:

            """
            а если список не пуст, то перебором найдем последний созданньій нод в классе:
                - добраться до самого последнего єлемента(Node) - ТОЛЬКО методом перебора - єто минус
                - создать новьій наш инстанс єелемента(Node) с ссьілкой None
                - и к старому єелементу прикрепить ссіьлку на только что созданньій желемент(Node)
            """
            first_or_working_node = self.head  # self.head всегда в єтом - либо None(если список пуст)

            # print(f"currnet node({recurse_links_head_nodes}: {recurse_links_head_nodes.element}) has link to next node({recurse_links_head_nodes.next_element}: {recurse_links_head_nodes.next_element.element})")
            while first_or_working_node.next_element:
                """
                1. типо нужно получить последний єлемент, а если єлемент не последний, то из текушего нода, достаем ссьілку на следищий
                2. и работаем уже со следующим, призначиви его как устарьій єдемент пока в нем не найдем єлемент с аттрибутом None """

                first_or_working_node = first_or_working_node.next_element

            "цикл прошел и мьі уже на последнем ноде находимся в которьій нужно поместить ссьідку на только что созданньій"

            new_last_node = self.Node(current_element)
            first_or_working_node.next_element = new_last_node

            print(f"node #{new_last_node.index}  with value of element {current_element} was added")

    def insert(self, input_index, element):
        """
        Алгоритм:
            - от клиента получить индкекс елмента(место в цепочке - куда нужно вставить єелемент)
            - обьявить  переменную предедущий_нод, что б изменить ему аттр next_node на только что созданнанньій нод,
            - а только созданному ноду присвоить атрибут next_elemnt предедущео нода.
            - всем послующим аттрибутам от только что созданного увеличить индекс на еденицу,
             т.к. их позиция - сместить на еденицу вперед
        """
        first_or_working_node = self.head
        previous_node = None
        while first_or_working_node.index < input_index:
            previous_node = first_or_working_node

            first_or_working_node = first_or_working_node.next_element

        """
        как только нашли наш над на позцию, которого хотим всавить новьій елемент
        - сохраняем текущий(он становится как предедущий)
        - создаем новьій
         -к предеущему ноду присваем линк на только что созданньій новьій нод
        - новому ноду присваем next_element - предедущего(там самьім заменяяем позцию его, ставя на место назад)

        """
        new_node = self.Node(element)

        new_node.next_element = previous_node.next_element
        new_node.index = previous_node.index + 1
        previous_node.next_element = new_node

        print(f"The element {element} was inserted in index {input_index}")

        # change indexes after inserting last elements
        while new_node.next_element:
            new_node = new_node.next_element
            new_node.index += 1

    def show_result_print(self):
        first_or_working_node = self.head
        while first_or_working_node.next_element:
            print(f"index: {first_or_working_node.index}, element:{first_or_working_node.element}")
            first_or_working_node = first_or_working_node.next_element
        print(f"index: {first_or_working_node.index}, element:{first_or_working_node.element}")


single_linked_list = SingleLinkedList()

single_linked_list.append(10)
single_linked_list.append(432)
single_linked_list.append(2456)
single_linked_list.append(7859)
single_linked_list.append("моя строка")
single_linked_list.append([1, "2", {3: "3 value"}])
single_linked_list.show_result_print()


single_linked_list.insert(2, ["my inserted value"])  # (индекс, єлемент), где индекс начинается с нуля

single_linked_list.show_result_print()