"""1) magic_methods зачем нужньі?"""
# - єто соглашение между програмистами "мол давайте (1)исользовать одни и те же методьі для (2)похожьіх операций"


class MyInfoClass:
    def show_info(self):
        print(f"Инфрпмирую из {self}")


class MySecondInfoClass:
    def show_info_2(self):
        print(f"Инфрпмирую из {self}")


class MyOtherClass:
    def show_other_info(self):
        print(f"Инфрпмирую из {self}")


def show_info():
    print(f"Инфрпмирую из show_info")


def show_info_2():
    print(f"Инфрпмирую из show_info_2")


def show_other_info():
    print(f"Инфрпмирую из show_other_info")


ex_1 = MyInfoClass()
ex_2 = MySecondInfoClass()
ex_3 = MyOtherClass()

ex_1.show_info()  # >>> Инфрпмирую из <__main__.MyInfoClass object at 0x102420490>
ex_2.show_info_2()  # >>> Инфрпмирую из <__main__.MySecondInfoClass object at 0x10244ef70>
ex_3.show_other_info()  # >>> Инфрпмирую из <__main__.MyOtherClass object at 0x10244efd0>

# Здесь идет вьізов функции  -  ()   - прикрепив к функции кнопку(сделав ее вьізьіваемой)
show_info()  # >>> Инфрпмирую из show_info
show_info_2()  # >>> Инфрпмирую из show_info_2
show_other_info()  # >>> Инфрпмирую из show_other_info

# Здесь принтим сам обьект функции
print(show_info, show_info_2, show_other_info)  #  >>> <function show_info at 0x1013e11f0> <function show_info_2 at 0x1015b10d0> <function show_other_info at 0x1015b1160>
# т.к. єто обьект, то его можно положить в список
notifications = [show_info, show_info_2, show_other_info]
for el in notifications:
    print('--------')
    print(el)
    el()

print("--------2---------")
"""2)все работает, но если миксануть вьізов функций и метод класса?
Логика: прикрутить к фунциям еше вьізов скласса со сторонніх бібілотек.
Задача: как использовать єто все вместе, что бьі не (1)код при єтом не разростался и не следить за названиеми
внутренними функциями, а вдруг в импортированной ибилитеке таких 100 классов оповещений?"""

notifications_with_class_methods = [show_info, show_info_2, show_other_info, ex_1.show_info, ex_2.show_info_2, ex_3.show_other_info]
for el in notifications_with_class_methods:
    el()

# Оно все работает, НО следить за всеми названями функций классов(их хз сколько) - єто ужасно

print("--------3---------")
"""3) Поєтому есть соглашение - 
'Давайте ми внутри классов придумаем такой метод,
в котором пропишем ту логику, 
которая вьізьівалось бьі, если бьі мі вьізвали наши екземпляр класса, как функцию(через кнопку - () )'"""

"""Важно!"""  # обьект_функции() - такие обьектьі с кнопками назьіваются CALLABLE
#  Допустим, не хочу запоминать методьі классов, а просто создавать екземпляр класса, докидьівать их в список,
#  дальше крутить в цикле и просто жать кнопку () , а там логика уже логика пуска сама отрабатьівает
notifications_as_instance = [show_info, show_info_2, show_other_info, ex_1, ex_2, ex_3]
for el in notifications_as_instance:
    # el()  # TypeError: 'MyInfoClass' object is not callable
    pass

print("--------4---------")
"""!!!!!!!!!Проблема - как сделать обьект класса вьізіваемьім как обісную функции"""
"""------------- РЕШЕНИЕ - дандер метод __call__ -----------------"""
# дандер метод - dubble under - два нижних подчеркивания. У них уже есть зарезервирваннньіе именна - первое
# соглашение(сделать одни методьі и с похожим функционалом)


class MyCallableInfoClass:

    def show_info(self):
        print(f"Инфрпмирую из {self}")

    def __call__(self, *args, **kwargs):
        print('int __call__')
        self.show_info()


ex_4 = MyCallableInfoClass()

notif = [show_info, ex_4, MyCallableInfoClass()]  # MyCallableInfoClass() - при нажатии на кнопку () - создается инстанс обьекта класса
for el in notif:
    el()



