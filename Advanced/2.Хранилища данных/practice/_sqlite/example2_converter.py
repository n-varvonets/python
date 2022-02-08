import json
import sqlite3


# пишем свой адантер, который преобразует словарь в текст формата JSON
def adapt_json(data):
    return json.dumps(data)


# пишем свой конвертер, который преобразует текст формата JSON в словарь
# действие обратное адаптеру
def convert_json(raw):
    return json.loads(raw)


"""ниже пример выдаст ошибку о типе json"""
# conn = sqlite3.connect(":memory:")  # - sql позволяет создавать файл бд в оперативной памяти и как только мы перестанем
# работать с ней, то он автоматически удалится
# cur = conn.cursor()
# cur.execute('CREATE TABLE test(p json)')  # оздам таблицу со своим собственным типом данным - json. Вс пройдет  |||| тоже самое что и cur.execute('CREATE TABLE users(first_name char(20))')
# успешно, потому что в скл есть такое понятие как аффинировать
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 1, 'ppp': 10},))
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 2, 'ppp': 11},))
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 3, 'ppp': 12},))
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 4, 'ppp': 13},))
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 5, 'ppp': 14},))
# cur.execute('SELECT * FROM test')
# row = cur.fetchone()
#
# conn.close()
"поэтому нужно реализовать поддержку своих типов(json)"

# регистрируем адаптер(обьекты пайтон в формат sql) и конвертер(из формата sql к обьектам типа данных пайтон).
# определяем поведения для конвертации в двух направлениях способом PARSE_DECLTYPES
sqlite3.register_adapter(dict, adapt_json)  # 1. из языка Python в базу данных
sqlite3.register_converter('json', convert_json)  # 2. из базы данных SQLite в типы данных Python (в нашем случае dict)

# определяем базу данных в оперативной памяти
conn = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES)  # PARSE_DECLTYPES - позволяет нам преобразовывать типы данных в соответсивие с типом столбцов
cur = conn.cursor()

# создаем таблицу с нашим типом данных и пробуем вставить dict
cur.execute('CREATE TABLE test(p json)')
cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 1, 'ppp': 10},))
cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 2, 'ppp': 11},))

# берем первую запись и проверяем работу нашего адаптера и конвертера
cur.execute('SELECT * FROM test')
record = cur.fetchone()
print(type(record[0]))
