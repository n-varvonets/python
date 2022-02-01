import csv

with open('data/example1.csv', 'r') as f:
    reader = csv.reader(f)
    print('Line nums', reader.line_num)
    print('Diaclect', reader.dialect)
    for row in reader:
        print(row)


# Line nums 0
# Diaclect <_csv.Dialect object at 0x7fe22efb0068>
# ['name', 'category', 'price']
# ['Sumsng A5', 'Smartphoners', '15000']
# ['IPhone 5S', 'Smartphoners', '18000']
# ['HP Laser Jet', 'Printers', '12000']
# ['iMac 21.5', 'MonoBlocks', '25000']