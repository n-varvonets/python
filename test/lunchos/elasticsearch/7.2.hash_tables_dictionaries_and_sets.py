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
print(data_for_dict) # обрати внимание что порядок вьівода такой же как мьі и ввели - ЄТО НЕ СТАНДАРТНАЯ ВЕЩЬ ДЛЯ ХЕШ-ТАБЛИЦ
# >>> {'nick': 'nicl@email.com', 'tolya': 'tolya@email.com', 'sasha': 'sasha@email.com'}

