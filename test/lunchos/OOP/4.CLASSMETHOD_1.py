from uuid import uuid4
print(" --- 0.о CLASSMETHOD:\n"
      " - pачем он вообще нужен \n"
      " - где он используется и где его лучше не использовать\n "
      " - рассмотрим примерьі где лучше использовать обьічньій (1)метод класса, где (2)static, а где - classmethod  ---\n  ")


print(" --- 1) Заблуждение о CLASSMETHOD: --- ")
# как правило, при собесеодвании, позитивньій ответ - єто декоратор, которьій
# покрьівает метод нашего класса и єтот метод можно вьізвьівать как из самого класса, так и из его єкземпляра... - ВАЛИДНО, НО не понятно!!!
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

print("\n   --- 2. Задача 1 --- ")  # : предстаим, что мьі хотим знать, сколько єкземпляров класса, біло созданно.
# Т.е. при каждой инициализации нашего обькета в классе счетчик увеличивался на еденицу.
# 2.2) Вариан 1: создать глобальную переменную счетчика и потом ее увеличивать:
tmb_cnt = 0
class Tumbochka_1(Tumbochka):
    """cоздадим точно такую же тумбочку что и віьше, но дабавим в инит глобальную переменную для счета єкз"""
    def __init__(self, id):
        super().__init__(id)

        global tmb_cnt
        tmb_cnt += 1

# и при создании екхмпляра - глабальная переменная юудет меняться
print(tmb_cnt)   # >>> 0
tumbochka_2 = Tumbochka_1(uuid4())
print(tmb_cnt)   # >>> 1
[Tumbochka_1(uuid4()) for _ in range(15)]  # создадим еще 15 єкземпляров
print(tmb_cnt)   # >>> 16  - все работает и замечательно!!! НО..

print("\n   --- 2.3.) ПРОБЛЕМА  --- ")  # если импортнуть єту тумбочку в другой модуль, ТО для корректной работьі с ним НУЖНО ПОМНИТЬ И ЕЩЕ ПРО
# ОДИН ИМПОРТ єтой глобальной переменнньі - єто плохо и можно забьіть или не знать про нее.
# 2.4) Решение №1(не очень хорошее). Занести глобальную в наш класс и потом ВЬІЗВАТЬ ЕЕ НАПРЯМУЮ через имя нашего КЛАССА
class Tumbochka_2(Tumbochka):
    class_tmb_cnt = 0
    def __init__(self, id):
        super().__init__(id)
        Tumbochka_2.class_tmb_cnt += 1

[Tumbochka_2(uuid4()) for _ in range(11)]
print(Tumbochka_2.class_tmb_cnt)  # >>> 11 - Замечательно, теперь мьі можем обращатсья к нашему аттрибуту - напрямую через класс
# 2.4) Решение №1 - не очень хорошее, потому что по правилам хорошего тонна, к аттрибутам нельзя обращаться
# напрямую что бьі их изменить, а только через ЕГО методьі класса. - создадим интерфейс для работьі с атрибутом
class Tumbochka_3(Tumbochka):
    class_tmb_cnt = 0
    def __init__(self, id):
        super().__init__(id)
        Tumbochka_2.class_tmb_cnt += 1

    # @classmethod
    def show_me_total_tumb_count(cls):
        return cls.class_tmb_cnt

# Что бьі вьізвать метод show_me_total_tumb_count(), то нам нужен єкземпляр
# print(Tumbochka_3.show_me_total_tumb_count())  # TypeError: show_me_total_tumb_count() missing 1 required positional argument: 'cls'

# 2.4) Решение №2 - использовать к нему staticmethod, НО тогда явно нужно класс тогоаттрибута, которьій мьі возращаем.
class Tumbochka_4(Tumbochka):
    """родительский класс для Tumbochka_5"""
    class_tmb_cnt = 0
    def __init__(self, id):
        super().__init__(id)
        Tumbochka_4.class_tmb_cnt += 1

    @staticmethod
    def show_me_total_tumb_count():
        return Tumbochka_4.class_tmb_cnt

print(Tumbochka_4.show_me_total_tumb_count())
print("\n   --- 2.5.) ПРОБЛЕМА_2  --- ")  # ЄТО ПЛОХО С СЛУЧАЕМ НАСЛЕДОВАНИЯ, потому что класс задается хардкорно, а не
# динмаически. И если мьі переопрделить єтот арртибут в отнаследованном клаасе со своим значением используя
# интерфейсьі(т.е. через метод переопределить аттрибут в нашем отнаследованном классе), то его значение измениться
# ТОЛЬКО в родительском(т.к. харкорно в методе задали в каком классе будем взаимдействовать с аттрибутом),
# А МЬІ ХОТЕЛИ бьі что бьі он изменялся  ТОЛЬКО В НАНШЕМ отнаследованном КЛАССЕ. переопределять метод в отналедованнмо
# классе - не варик, потому что будет простьіня из похожего кода.
class Tumbochka_5(Tumbochka_4):
    """Созаддим дочерний класс от Tumbochka_4 со своим переопределленньім аттрибутом под логику данного класса"""
    class_tmb_cnt = 0

print(Tumbochka_5.show_me_total_tumb_count())  # отобразится аттрибут с Tumbochka_4,
# а не Tumbochka_5 из-за 69ой строки(return Tumbochka_4.class_tmb_cnt)... как отобразить аттрибут нашего класса,
# не переопределяя метод в дочернем?

print("\n   --- 2.4) Решение №3 - исользовать classmethod, куда мьі будем при его вьізове передавть\n"
      " именно тот класс как обьект вместе и КОНРЕТНО  С ЕГО АТТРИБУТАМИ, с которого он бьіл вьізван.")

class Tumb:
    """Какой-то родетельский класс с его переенной class_tmb_cnt"""
    class_tmb_cnt = 0
    def __init__(self, id):
        self.tumb_id = id
        Tumb.class_tmb_cnt += 1

    def open_door(self):
        print(f"Открили дверь тумбочки с id {self.tumb_id}")

    @staticmethod
    def cut_by_scissors(smth):
        print(f"Режим ножницами {smth}")

    @classmethod
    def show_me_total_tumb_count(cls):
        return cls.class_tmb_cnt

# create a few instances for changing Tumb.class_tmb_cnt
[Tumb(uuid4()) for _ in range(13)]
print(Tumb.show_me_total_tumb_count())  # >>> 13
class ProTumbChild(Tumb):
    """Какой-то родетельский класс с его переенной class_tmb_cnt"""
    class_tmb_cnt = 100500


[ProTumbChild(uuid4()) for _ in range(2)]
print(ProTumbChild.show_me_total_tumb_count())  # >>> 100500  - Почему не 2? Важно!
print(Tumb.show_me_total_tumb_count())  # 13 >>> - Почему не 11? Важно!

