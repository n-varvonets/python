head = None
class Node:

    element = None
    next_element = None

    def __init__(self, element, next_element=None):
        self.element = element
        self.next_element = next_element


def append(current_element):
    global head

    if not head:
        head = Node(current_element, next_element=None)
    else:
        recurse_links_head_nodes = head

        # new_last_node = Node(current_element)
        # while head_node.next_element:
        #     head_node.next_element = new_last_node

        while recurse_links_head_nodes.next_element:
            print(recurse_links_head_nodes, " | | ", recurse_links_head_nodes.next_element)
            # типо нужно получить последний єлемент, а если єлемент не последний,
            # то предедущему - текущим из атрибута посл_нода.next_element
            recurse_links_head_nodes = recurse_links_head_nodes.next_element

        # цикл прошел и мьі уже на последнем усщле находимся
        # в которьій нужно поместить ссьідку на только что созданньій
        # т.е ошибка бьіла в том, что я не раскручивал рекурсивно єлемент

        new_last_node = Node(current_element)
        recurse_links_head_nodes.next_element = new_last_node


def show_result_print():
    recurse_links_head_nodes = head
    while recurse_links_head_nodes.next_element:
        print(recurse_links_head_nodes.element)
        recurse_links_head_nodes = recurse_links_head_nodes.next_element
    print(recurse_links_head_nodes.element)


append(10)
append(432)
append(2456)
append(12412)

show_result_print()