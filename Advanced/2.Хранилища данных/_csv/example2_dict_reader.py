import csv

with open('data/example1.csv', 'r') as f:
    reader = csv.DictReader(f)
    print('Line nums', reader.line_num)
    print('Diaclect', reader.dialect)
    for row in reader:
        print(row)
        # row['name'] --> row[0]

# Line nums 0
# Diaclect excel
# OrderedDict([('name', 'Sumsng A5'), ('category', 'Smartphoners'), ('price', '15000')])
# OrderedDict([('name', 'IPhone 5S'), ('category', 'Smartphoners'), ('price', '18000')])
# OrderedDict([('name', 'HP Laser Jet'), ('category', 'Printers'), ('price', '12000')])
# OrderedDict([('name', 'iMac 21.5'), ('category', 'MonoBlocks'), ('price', '25000')])