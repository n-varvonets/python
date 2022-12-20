# Задача: написать свой кастомньій итератор с помощью класса,
# которьій бьі при итерации умножал очередное значение на 10

class MyIteratorForIterableCustomData:
    def __init__(self, some_object):
        self.object = some_object
        self.cursor = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor < len(self.object):
            result = self.object[self.cursor] * 10
            self.cursor += 1
            return result
        raise StopIteration


class MyIterableCustomData:
    def __init__(self):
        self.obj_list = []

    def __iter__(self):
        return MyIteratorForIterableCustomData(self.obj_list)

my_custom_data = MyIterableCustomData()
my_custom_data.obj_list.append(1)
my_custom_data.obj_list.append(30)
my_custom_data.obj_list.append('2')
my_custom_data.obj_list.append([2, 3])
my_tricky_collection = [my_custom_data]

for type_of_custom_data in my_tricky_collection:
    for el in type_of_custom_data:
        print(el)

