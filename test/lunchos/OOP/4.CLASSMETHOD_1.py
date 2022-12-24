from uuid import uuid4

print(" --- 1) Заблуждение о CLASSMETHOD: --- ")
# как правило, при собесеодвании, позитивньій ответ - єто декоратор, которьій
# покрьівает метод нашего класса и єтот метод можно вьізвьівать как из самого класса, так и из его єкземпляра... - НЕ ВЕРНО!!!
# как видим вьіше, то статик метод тоже делает такое... но что же тогда делает CLASSMETHOD?
class Tumbochka:
    def __init__(self, id):
        self.tumb_id = id

    def open_door(self):
        print(f"Открили дверь тумбочки с id {self.tumb_id}")

    @staticmethod
    def cut_by_scissors(smth):
        print(f"Режим ножницами {smth}")


tumbochka = Tumbochka(uuid4())
tumbochka.open_door()
tumbochka.cut_by_scissors("paper from object")
Tumbochka.cut_by_scissors('paper from class')

print(" --- 2. Задача 1 --- ")  # : предстаим, что мьі хотим знать, сколько єкземпляров класса, біло созданно.
# Т.е. при каждой инициализации нашего обькета в классе счетчик увеличивался на еденицу.
# 2.2) Вариан 1: создать глобальную переменную счетчика и потом ее увеличивать:
tmb_cnt = 0
class Tumbochka_1(Tumbochka):
    def __init__(self, id):
        super().__init__(id)
        global tmb_cnt
        tmb_cnt += 1

# и при создании екхмпляра - глабальная переменная юудет меняться
print(tmb_cnt)   # >>> 0
tumbochka_2 = Tumbochka_1(uuid4())
print(tmb_cnt)   # >>> 1
tumbochka_3 = Tumbochka_1(uuid4())
print(tmb_cnt)   # >>> 2