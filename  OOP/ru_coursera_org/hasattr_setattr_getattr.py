class Example:
    pass

e = Example()
"""1) т.е. можно в глобальном неймспейсе добавить аттр и получить это значение"""
# 1)добавляем аттрибут
e.test = 1
print(e.test)

# 2)добавляем метод обьекту как аттр
def foo():
    print('Test')

e.f = foo
e.f()
print(dir(e))
# 1
# Test
# ['__class__', ... , 'f', 'test']
# --------------------------------------------------------------------------------------------------------------

"""1) но если в цикле(не локальном неймсаейсе) мы захотим создать атрибут глобальной для глобального обьекта """
# while True:
#     attr = input('Give media attr name ')
#     val_of_attr = input('Give me value of attr ')
#
#     # то напчеатать мы их просто можем... а вот обьекту е назнаичть аттрибут с определенным значение - нет, вот почему..
#     """т.е. если я захочу добавить аттрибут и назначить значение как методомо выше(глоб. неймспейс, а не локал), то
#     можно только хардкодить ОДИН РАЗ название аттрибута, а не динамически его подставлять"""
#     e.attr = list(attr)
#     e.value = val_of_attr
#     print(dir(e))  # ['__class__', ...  '__weakref__', 'attr', 'f', 'test', 'value']
#
#     e.attr.append('qwe')
#     print(e.value, e.attr)  # 2 ['1', 'qwe']


"""2.) setattr позволить указать обьект, задать МНОЖЕСТВО имен атрибута и их значение В ЦИКЛЕ"""
# while True:
#     attr = input('Give media attr name ')
#     val_of_attr = input('Give me value of attr ')
#     setattr(e, attr, val_of_attr)
#     print(dir(e))
#     # Give media attr name name_1
#     # Give me value of attr val_1
#     # ['__class__', ... , 'f', 'name_1', 'test']
#     """и теперь можно обратиться к его новому аттрибуту(name_1) что бы получить его занчение(val_1) """
#     print(e.name_1)  # ИМЕННО здесь возникает другая проблема,и то пайчарм будет ругаться,
#     # потому в runtime при выполнения скрипта имя данного атрибута(name_1) еще не задано, ДЛЯ ЭТОГО используем getattr
#
#     print(getattr(e, attr))  # и нормально обработает какое бы динамическое имя аттрибута не пришло
#
#     # если придет другое имя
#     print(getattr(e, "name_attr"))  # то упадет ошибка AttributeError
#     print(getattr(e, "name_attr", 'стандартный ответ если нет указанного имя атрибута или None'))  # можно задать что ответить если не будет указанного аттрибута

"""3)можно проверить есть ли атрибут в обьекте hasattr"""
# while True:
#     attr = input('Give media attr name ')
#     val_of_attr = input('Give me value of attr ')
#     setattr(e, attr, val_of_attr)
#
#     if hasattr(e, "test"):  # передаем обьект и то название аттрибу, которые хотим проверить на наличии в обьекте
#         print("Object {} has attribute 'test' with value {}".format(e, getattr(e, "test")))  #  можем использовать метод getattr что бы взять наш аттрибут и вставвить в наше смс
#     else:
#         print("Object {} does not hav attribute 'test' with value".format(e))

"""т.е. как это может быть нам полезно?   """
class  Example1:

    def foo(self):
        print('Foo func')

    def bar(self):
        print('Bar func')

e1 = Example1()

call_function = input('What func you want to call')

if hasattr(e, call_function):
    getattr(e, call_function)()
else:
    print('No func "{}" in object {}'.format(call_function, e1))



