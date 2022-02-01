import csv

sniffer = csv.Sniffer()  # помагает определить какой диалект в полученном файле используется
dialect = None

# стандартное повоедение не опредеяет диалект и выводит просто массив из одного эелемента(т.е. он читает целую строку как одно значение, хотя по факту - нет)
with open('data/inderfined_dialect.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

with open('data/inderfined_dialect.csv', 'r') as f:
    content = f.read()
    dialect = sniffer.sniff(content)

print(dialect.delimiter, dialect.doublequote, dialect.quoting)

with open('data/inderfined_dialect.csv', 'r') as f:
    reader = csv.reader(f , dialect=dialect)
    for row in reader:
        print(row)