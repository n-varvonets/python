def quick_sort(array: list or str, reverse: bool=False) -> list:
    """
    основная идея заключается в том что:
        - берем мнаш массив любо длиньі
        - в єтом массиве берем опорньій елемент(наугад или как захочется - его значение не важно, главное позиция(индекс));

        - формируешься из исходного массива - еще 3 масива:
            1. в первьій кладешь все елементьі, что МЕНЬШЕ опроного єелемента;
            2. во второй кладешь все елементьі, что БОЛЬШЕ опроного єелемента;
            3. в тертий кладешь все елементьі, что РАВНЬІ опроному єелемента;

        - потом полученньіе массивьі сортируем таким же способом до победного конца(т.е. пока
         в пришедшую нашу функцию не осанется один єлемент)

         - собирать по порядку:
            - возрастанию:
                1) сначала массив с меньшими єелментами;
                2) потом пропсто массив с єелементами равному опрному(не сортируем его - потмоу что там
                и так лежат одни и те же значения);
                3) затем массив у которого елементьі больше опорного;
            - убьіванию:

    :param array:
    :reverse: reverse=True - сортировка в обратном порядке
    :return: sorted arrays of value
    """
    sorted_array = array[:]

    if len(sorted_array) == 0:
        # если список пуст, то єто пустое просто его возращаем обратно для принта(как и обьічно бьівает)
        return sorted_array

    pivot_core_el = sorted_array[0]

    lower_array = [element for element in sorted_array if element < pivot_core_el]
    higher_array = [element for element in sorted_array if element > pivot_core_el]
    # print(f"\n пришедший массив в функцию {sorted_array}\n"
    #       f"массивьі не его основе: опорньій елемент '{pivot_core_el}', НИЖЕ{lower_array}, ВЬІШЕ {higher_array}")

    # учтем вьібранньій клиентом - порядок сортировки
    if not reverse:
        # 1. case: от меньшего к большему
        return (
            quick_sort(lower_array)
            + [element for element in sorted_array if element == pivot_core_el]
            + quick_sort(higher_array)
        )
    if reverse:
        # 1. case: от большего к меньшему
        return (
            quick_sort(higher_array, reverse=True)
            + [element for element in sorted_array if element == pivot_core_el]
            + quick_sort(lower_array, reverse=True)
        )


array = [1, 30, -30, 4, 2, 8, -6, 10]
print(quick_sort(array))
print(quick_sort(array, reverse=True))

sting_as_array = "my array"
print(quick_sort(sting_as_array))

