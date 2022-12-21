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


print(' --- second option in SINGLE class --- ')


class SingleCustomIterator:
    def __init__(self, some_objects):
        self.some_objects = some_objects
        self.cursor = 0

    def to_start(self):
        self.cursor = 0

    def to_current(self, val):
        if val >= len(self.some_objects) or val < 0:
            print("Неверное значение для курсора!")
        else:
            self.cursor = val

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor < len(self.some_objects):
            result = self.some_objects[self.cursor] * 10
            self.cursor += 1
            return result
        raise StopIteration


my_custom_objects_list = SingleCustomIterator([2, "3"])
# my_custom_objects_int = SingleCustomIterator(1)  # TypeError: object of type 'int' has no len()
my_tricky_collection = [my_custom_objects_list, ]
for one_elem_of_list in my_tricky_collection:
    for el in one_elem_of_list:
        print(el)
# 20
# 3333333333

print("ВАЖНО!!!: т.е. __iter__ нужен, когда в нашем классе есть аттрибут типа коллекция \
 и нам нужно по єтим значениям проєтерироваться")


