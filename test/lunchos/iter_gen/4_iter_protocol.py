l = [1, 2, 3, 4]

try:
    """correct version"""
    iterator = iter(l)
    while True:
        print(next(iterator))
except StopIteration:
    pass

"""Задача: написать кастомньій класс и что бьі он поддерживал итерацию"""
#  Условие: У нас есть склад с разніми отделами(логистика і др серисьі) куда мьі будем запихвать нашу технику(принтерьі, ксероксьі, сканерьі).
# Что делать? Я хочу сощдавть обьектьі техники и запихивать их по обьектам складов.
class Printer:
    pass


class Scaner:
    pass


class Xerox:
    pass


class WareHouse:
    def __init__(self):
        """в моем обьекте склада будет изначально пустой список техники, которьій будем заполнять"""
        self.storage = []

    def add_one_tech_to_storage(self, tech):
        """метод для добавления еденицьі техники в обьект склада"""
        self.storage.append(tech)

    def add_multi_tech_to_storage(self, list_of_tech):
        self.storage.extend(list_of_tech)


printer_tech_list = [Printer() for _ in range(10)]  # create 10 printers
scaner_tech_list = [Scaner() for _ in range(5)]
xerox_tech_list = [Xerox() for _ in range(2)]
ware_house = WareHouse()

# добавим в наш обьект склада нашу технику:
ware_house.add_multi_tech_to_storage(printer_tech_list)
ware_house.add_multi_tech_to_storage(scaner_tech_list)
ware_house.add_multi_tech_to_storage(xerox_tech_list)
for tech in ware_house.storage:
    print(tech)

# Проблема: да оно работает, но я бьі хотел итерироваться именно по обьекту ware_house, а не по его переменной типа лист.
#  єто нужо для импользования одних  и тех же интерфейсов(т.е. обращаться к обьекту напрямую и использовать одни и те же методьі),
"""Т.е. иметь возможность работать с 4мя типами коллеций в цикле + добавить свой кастомньій обьект как колекцию.
Т.е. не скармливать поле коллекции (ware_house.storage), а сам обьект(ware_house)"""
# Для єтого в кастомном класссе нужно создать метод иткоратора, которьій бі принимал коллекцию и возращал бі ИТЕРАТОР.


class WareHouseIterator:
    def __init__(self):
        """в моем обьекте склада будет изначально пустой список техники, которьій будем заполнять"""
        self.storage = []

    def add_one_tech_to_storage(self, tech):
        """метод для добавления еденицьі техники в обьект склада"""
        self.storage.append(tech)

    def add_multi_tech_to_storage(self, list_of_tech):
        self.storage.extend(list_of_tech)

    def __iter__(self):
        return iter(self.storage)

warehouse_iterable = WareHouseIterator()
warehouse_iterable.add_multi_tech_to_storage(printer_tech_list)
warehouse_iterable.add_multi_tech_to_storage(scaner_tech_list)

for tech in warehouse_iterable:
    print(tech)