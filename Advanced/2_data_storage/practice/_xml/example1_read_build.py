from xml.etree import ElementTree as ET

# открываем файл
tree = ET.parse('data/test.xml')
# получаем корневой DOM элемент
root = tree.getroot()

# выбираем все дочерние элементы
children = root.getchildren()

for student_data in children:
    # .attrib- доступ к атрибутам тега
    print("PK: ", student_data.attrib)
    # итерируемся по всем внутренним тегам и печатаем название тега и контент
    for child in student_data:  # child - это аттрибут студента(age, first/last_name)
        print('{}: {}'.format(child.tag, child.text))


root = ET.Element('record')   # создаем корневой элемент 'record'
for i in range(10):
    sub_element = ET.SubElement(root, 'value{}'.format(i))  # SubElement - создает дочерний аргумент рута(root)
    sub_element.text = str(i * 10)  # присваиваем полученное значение к созданному элементу
print(ET.dump(root))  # only for dev/trace  - дамп должен использоваться исключительно в тестрованном режиме(что бы проверить правильность занчений), а в проде - метод write,что бы записать данные в файл
# <record><value0>0</value0><value1>10</value1><value2>20</value2><value3>30</value3><value4>40</value4><value5>50</value5><value6>60</value6><value7>70</value7><value8>80</value8><value9>90</value9></record>


data = [
    {'x': 10, 'y': 29, 'z': 90},
    {'x': 11, 'y': 28, 'z': 91},
    {'x': 12, 'y': 27, 'z': 92},
    {'x': 13, 'y': 26, 'z': 93},
    {'x': 14, 'y': 25, 'z': 94},
]

root = ET.Element('records')

for item in data:
    record = ET.SubElement(root, 'record')  # для корневого значения(root) создаем дочернего его значение 'record'
    # item = {'x': 10, 'y': 29, 'z': 90}
    for key, value in item.items():
        e = ET.SubElement(record, key)  # создаем его атрибут
        e.text = str(value)  # вписываем в созданный аттрибут наше значение

# от у нас уже созданный обьект root
print(root)

# для того что бы записать данные в файл - создаем наш екземляр класса в который передаем нащ корневой элемент
tree = ET.ElementTree(root)
tree.write('data/output.xml', encoding='utf-8')
