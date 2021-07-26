from xml.etree import ElementTree as ET

tree = ET.parse('data/test.xml')
root = tree.getroot()

children = root.getchildren() # берем все дочернии эелементы тега  data  из root

for student_data in children:
    print("PK", student_data.attrib)  # выводит атрибут тега <person pk="20"> >>>  PK {'pk': '20'}
    for child in student_data:
        print(f"{child.tag} --and-- {child.text}")  # >>> first_name --and-- Dmitriy

root = ET.Element('record')
for i in range(10):
    sub_element = ET.SubElement(root, f"value is.... {i}")
    sub_element.text = str(i*10)

print(ET.dump(root))  # only for dev/trace

data = [
    {'x':10, 'y':29, 'z':95},
    {'x':11, 'y':28, 'z':94},
    {'x':12, 'y':27, 'z':93},
    {'x':13, 'y':26, 'z':92},
    {'x':14, 'y':25, 'z':91},
]