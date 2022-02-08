from lxml import etree as ET


class PersonTarget:
    """
    Порциональная обработка данных XML файла.
    """

    def __init__(self):
        # определяем дефолтные значения перед началом работы
        self.records = []
        self.current_index = None
        self.current_node = None

    def start(self, tag, attrib):
        """метод старт вызывается когда парсер открывает тег, но еще не добрался к его данным"""

        # + в данном случае нас не интересует корневой тег data, а интересует тег person

        # при входе в тег person, добавляем новую запись в список,
        # которую далее будем заполнять в методе data.
        if tag == 'person':
            self.records.append({
                'first_name': '',
                'last_name': '',
                'age': None,
                'metadata': attrib
            })  # print(self.records[0]) >>> {'first_name': '', 'last_name': '', 'age': None, 'metadata': {'pk': '20'}}
            # как только отрывается тег персен, то автоматически определяем индекс, что бы определить в каком именно персоне смы находимся
            self.current_index = len(self.records) - 1  # и присваиваем чему равен текущи индекс person(для его определения self.records[0]) что бы не вычеслять его постоянно
        # указываем текущий тег, чтобы проверять его в data.
        self.current_node = tag

    def end(self, tag):
        # print(tag) >>> first_name,...
        # по завершению теги сбрасываем текущий тег (обновляем его что бы при новом вызове метода
        # start current_node был не равен текщему тегу)
        self.current_node = ''

    def data(self, data):
        """дата вызывает именно тогда, когда мы читаем данные из тега после вызова метода tart"""
        print('Data: {} -> "{}"'.format(self.current_node, data))
        # проверяем текущий тег, если он является одним из интересующих нас,
        # то берем данные из тега и записываем в элемент с индексом
        # self.current_index.
        if self.current_node in ['first_name', 'last_name', 'age']:
            #
            self.records[self.current_index][self.current_node] = data

    def close(self):
        return self.records


# связь парсера с нашим классом обработчиком- target.
parser = ET.XMLParser(target=PersonTarget())
infile = 'data/test.xml'
# после вызова метода парс нам вернётся
print(parser.target)
results = ET.parse(infile, parser)

for r in results:
    print(r)
