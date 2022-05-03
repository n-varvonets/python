from typing import Dict, Tuple, List

# функция по примеру с прошлой задачей, но только здесь мы указываем типы
# при создании интсанса, а не в функции,т.к. по какой-то из причин мы не можем её изменить(пример лежит она в библотеке)

def generate_tuple(data) -> list:
    result = []
    for key, value in data.values():
        result.append((key, value))
    return result


test_data1 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
test_data2 = {'k1': 'v1', 'k2': 'v2', 'k3': 10}
test_data3 = {'k1': 'v1', 'k2': 'v2', 'k3': 10.4}
test_data4 = {'k1': 'v1', 'k2': 'v2', 'k3': []}

# ниже подсвечивается желтым, потому что результат функции должен вовзращаться в list
test_value1 = generate_tuple(test_data1)  # type: Tuple[str, str]
test_value2 = generate_tuple(test_data2)  # type: Dict[str, int]
test_value3 = generate_tuple(test_data3)  # type: List
test_value4 = generate_tuple(test_data4)  # type: dict

# ниже тоже пример присваивания строки, хотя указали что тип должен быть int
another_value = '10'  # type: int
# test_value1.???
# test_value2.???
# test_value3.???
# test_value4.???
