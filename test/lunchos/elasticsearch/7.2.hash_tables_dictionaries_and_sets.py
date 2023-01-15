# 1. создадим пеерменньіе для харенния словаря и множства
data_for_dict = {}
data_for_set = {}
# 2. проверим их типьі
print(type(data_for_dict), type(data_for_set))
# >>> <class 'dict'> <class 'dict'>   - удивительно, но печатеет все диктьі
# 3. Если в переменную_для_множества измением добавив значение без ключа, то его тип изменится на множество:
data_for_set = {"single val without key"}
print(type(data_for_set))
# >>> <class 'set'>

print(' -   2. Очереденость и уникальность ключей в set_dict   - ')
data_for_dict = {'nick': "nicl@email.com", "tolya": "tolya@email.com", "sasha": "sasha@email.com"}
print(data_for_dict)  # обрати внимание что порядок вьівода такой же как мьі и ввели - ЄТО НЕ СТАНДАРТНАЯ ВЕЩЬ ДЛЯ ХЕШ-ТАБЛИЦ
# >>> {'nick': 'nicl@email.com', 'tolya': 'tolya@email.com', 'sasha': 'sasha@email.com'}
# 2.1 Если нужно созранить порядок, то не рекомендуется используется ПРОСТОЙ словарь в пайтое, а использовать его с колллекции:
from collections import OrderedDict
ordered_dict = OrderedDict()


data_for_dict_with_duplicate = {'nick': "nicl@email.com", 'nick': "nicl@email.com",'nick': "new value of previous key", "tolya": "tolya@email.com", "sasha": "sasha@email.com"}
print(data_for_dict_with_duplicate)
# >>> {'nick': 'new value of previous key', 'tolya': 'tolya@email.com', 'sasha': 'sasha@email.com'} -
# т.е по одному и тому же ключу для раришения колиззий - перьвій перезатирается

print("т.е. исходя из вьіше сказанного, для хеш таблицьі\n"
      " - они не отсортированьі\n"
      " - они не могут иметь дупликатов КЛЮЧЕЙ\n\n")

print(" -  3.Как словарь питона устроен внутри?     - \n")
# каждое значение - єто комбинация из трех значений: < hash|key|value >

print(" -  4.как или какие обьектьі спосбньі получить хеш?     - \n")
#  4.1. к примру получим дваждьі хеш ключа "nick"
#  4.2. но из типа list(), словаря, множества или другой коллекции - нельзя получить хєш
# print(hash(list()))   #  line 40, in <module> TypeError: unhashable type: 'list'
# print(hash([]))   #  line 41, in <module> TypeError: unhashable type: 'list'
# print(hash({"ц"}))   #  line 41, in <module>  TypeError: unhashable type: 'set'
# print(hash({"ц":"і"}))   #  line 41, in <module>   TypeError: unhashable type: 'dict'
#  4.3.  Но из строки или инта - спокойно
print(hash("nick"))
print(hash("nick"))
# >>> 4969293777060974545
# >>> 4969293777060974545
print(hash(342))
print(hash(10_000_000))
# >>> 342
# >>> 10000000
print(" -  5. как сделать хешированньій кастомньій тип? Т.е. сделать свой обьект изменяемьім?     - \n")
class Test_immutable:
    """по дфеолту каждьій созданньій тип - неизменямьій"""
    pass

class Test_mutable:
    """говоирм что наш тип - не может измениться, т.е не может бьіть захешированньім"""
    __hash__ = None


print(hash(Test_immutable()))  # 283985917 - ХЕШ ЄТО АДРЕС В ПАМЯТИ
# print(hash(Test_mutable()))  #  >>>  line 60, in <module> TypeError: unhashable type: 'Test_mutable'

print(" -     7.UNION AND INTERSECTION    - ")

my_fav = {"red", "green", "black", "blue", "purple"}
her_fav= {"blue", "orange", "purple", "green"}

#union
all_favs = my_fav | her_fav
print(all_favs) #no repetition
#You may see + to combine lists, in which there are repeats.
#But we are not working with lists...so i'll try to focus here.

#intersection (elements shared between both)
wedding_colors = my_fav & her_fav
print(wedding_colors)
#this is like the inside section of a venn diagram

#There are also method versions:
all_favs = my_fav.union(her_fav)
print(all_favs)

wedding_colors = my_fav.intersection(her_fav)
print(wedding_colors)


######### DIFFERENCE AND SYMMETRIC DIFFERENCE #########


my_fav = {"red", "green", "black", "blue", "purple"}
her_fav= {"blue", "orange", "purple", "green"}

#Difference
only_my_colors = my_fav - her_fav
print(only_my_colors) #elements in left getting rid of all in right.
#Could go other way too:
only_her_colors = her_fav - my_fav
print(only_her_colors)

#symmetric difference is like if you took colors only I liked union with colors only she liked and put em together:

symmetric = my_fav ^ her_fav
print(symmetric)

#This is like:
symmetric = only_my_colors | only_her_colors
print(symmetric)
