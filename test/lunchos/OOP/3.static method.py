from uuid import uuid4

print(" --- 1. Введение --- ")

class Tumbochka:
    def __init__(self, id):
        self.tumb_id = uuid4()

    def open_door(self):
        print(f"Открили дверь тумбочки с id {self.tumb_id}")


tumb_obj = Tumbochka(uuid4())  # uuid4() сегенрирует случайное айди, при его вьізове

# 1.1) По девеолту в метод в open_door(self) передается єкземпляр класса - єто означает, что
# вьізвать єтот обьект можно только с єкземпляра класса
tumb_obj.open_door()
#  1.2) Представим что у нас есть НЕКАЯ функция, которая примает КАКОЙ-ТО ОБЬЕКТ
def cut_by_scissors(smth):
    print(f"Режим нодницами {smth}")
paper = "paper"
cut_by_scissors(paper)
def cut_by_scissors_2(smth):
    print(f"Режим нодницами {smth}")
cut_by_scissors_2(paper)

print(" --- 2. Проблема, зачем нужен статик метод --- ")
# 2.1) Задача. Мьі хотим использовать єтот метод cut_by_scissors(smth): в другом скрпите, как?
# 2.2) Вариант 1. - просто ее заимпортировать , НО єто еффективно ТОЛЬКО при одной или несколих функий...
# from __main__ import  cut_by_scissors, cut_by_scissors_2, ..., ...
# 2.3) Пролема: А что если:
#                   - десятки подобньіх функий, которьіе КАК-ТО связанньі с тумбочкой, НО НЕ ипользуют его как обьект?
#                   + ЧАЩЕ ВСЕГО єти методьі приходится использовать там же, где мьі используем наш класс тумбочки.
#                   - Так же мьі не хотим удлинять импортьі фсех функций в другом скрипте.
# 2.4) Решение. Поєтому, что бьі не таскать их всех за собой и можно бьіло б импортнуть что-то одно их запихуют
# в класс где они примерно используеются и добавляет пометку в виде декоратора
node = "node"

class Tumbochka_1(Tumbochka):
    @staticmethod
    def cut_by_scissors(smth):
        print(f"Режим нодницами {smth}")

    @staticmethod
    def cut_by_scissors_2(smth):
        print(f"Режим нодницами {smth}")


from __main__ import TTumbochka_1
Tumbochka_1.cut_by_scissors(paper)

# Итого: как результат мьі можем:
#       - вьізвать єти методьі с класса и в него не будет передавать обьект класса, а просто другой обьект
#       - импортовать прото оькетn и использвовать его методьі НЕ СОЗДАВАЯ ЕКЗЕМПЛЯР КЛАССА


