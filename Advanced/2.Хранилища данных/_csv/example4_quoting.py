import csv

with open('data/output.csv', 'w') as f:
    writer = csv.DictWriter(
        f,
        fieldnames=['first_name','last_name', 'age'],

    )  # QUOTE_ALL

    """ DictWriter - сейчас будем передавать словарь вместо масива"""  # масив - writer.writerow((['1','2','3']))
    writer.writeheader()   # пишет наши заголвки стобцов('first_name','last_name', 'age') в файл

    writer.writerow({
        'first_name':'Ivan',
        'last_name':'Petrov test',
        'age': 20
    })

    writer.writerow({
        'first_name': 'Nick',
        'last_name': 'Varv',
        'age': 25
    })

    writer.writerow({
        'first_name': 'Sash',
        'last_name': 'Varvqew',
        'age': 30
    })

