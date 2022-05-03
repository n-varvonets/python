from typing import List

"""конкретизируем типы элементы во вложенных данных(list). Разберем 2 примера:"""


class User:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name


def create_users_v1(first_names: list, last_names: list) -> list:  # мы не знаем какие типы элементов содержит list
    users = []
    items = zip(first_names, last_names)
    for first_name, last_name in items:
        # first_name.?????
        users.append(User(first_name, last_name))
    return users


def create_users_v2(first_names: List[str],
                    last_names: List[str]) -> List[User]:   # указываем что list т содержать элементы с типом str
    users = []
    items = zip(first_names, last_names)
    for first_name, last_name in items:
        # first_name.AUTOCOMPLETE
        users.append(User(first_name, last_name))
    return users


users1 = create_users_v2(['f1', 'f2'], ['l1', 'l2'])
users2 = create_users_v2(['f1', '10'], ['10.5', 'l2'])
# users2 = create_users_v2(['f1', 10], [10.5, 'l2'])
users3 = create_users_v2(['f1', 'f2'], ['[]', 'l2'])
print(users2[0].get_full_name())
