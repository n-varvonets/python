head = None
cnt_nodes = 1
class Node:

    element = None
    next_element = None

    def __init__(self, element, next_element=None):
        self.element = element
        self.next_element = next_element


def append(current_element):
    global head
    global cnt_nodes

    if not head:
        head = Node(current_element, next_element=None)
    else:
        recurse_links_head_nodes = head

        """Ошибка бьіла в том, что я не раскручивал рекурсивно єлемент"""
        # new_last_node = Node(current_element)
        # while head_node.next_element:
        #     head_node.next_element = new_last_node


        # print(f"currnet node({recurse_links_head_nodes}: {recurse_links_head_nodes.element}) has link to next node({recurse_links_head_nodes.next_element}: {recurse_links_head_nodes.next_element.element})")
        while recurse_links_head_nodes.next_element:
            """
            1. типо нужно получить последний єлемент, а если єлемент не последний, то из текушего нода, достаем ссьілку на следищий
            2. и работаем уже со следующим, призначиви его как устарьій єдемент пока в нем не найдем єлемент с аттрибутом None """

            recurse_links_head_nodes = recurse_links_head_nodes.next_element

        "цикл прошел и мьі уже на последнем ноде находимся в которьій нужно поместить ссьідку на только что созданньій"

        new_last_node = Node(current_element)
        recurse_links_head_nodes.next_element = new_last_node

        print(f"node #{cnt_nodes} was added")
        cnt_nodes += 1


def show_result_print():
    print("\nlist of:")
    recurse_links_head_nodes = head
    while recurse_links_head_nodes.next_element:
        print(recurse_links_head_nodes.element)
        recurse_links_head_nodes = recurse_links_head_nodes.next_element
    print(recurse_links_head_nodes.element)


append(10)
append(432)
append(2456)
append(12412)
append(22215)

show_result_print()










