"""Single responsibility - один класс должен иметь только одну зону ответсенности"""
print('-------------- Before -------------')

class ExportCsv:
    """
    Данньій класс нарушает:
        - форматируем и подготавливаем данньіе для вьіводу куда-то
        - и что-то куда-то пишет
    """
    def __init__(self, raw_data):
        self.data = self.prepare(raw_data)
    def prepare(self, raw_data):
        result = ''
        for item in raw_data:
            new_line = ','.join((item['name'], item['surname']))
            result += f'{new_line}\n'
        return result
    def write_file(self, filename):
        with open(filename, 'w', encoding='UTF-8') as f:
            f.write(self.data)
data = [
    {'name': "Nick", 'surname': "Var"},
    {'name': "Alex", 'surname': "Var2"}
]
exporter = ExportCsv(data)
exporter.write_file('out.csv')

print('-------------- After -------------')
class FormatDataSRP:
    """
    Данньій класс:
        - данньій класс будет принимать просто сьіріьіе данньіе
        - и подготовит данньіе
    """
    def __init__(self, raw_data):
        self.raw_data = self.raw_data

    def prepare(self):
        result = ''
        for item in self.raw_data:
            new_line = ','.join((item['name'], item['surname']))
            result += f'{new_line}\n'
        return result

class FileWriterSRP:
    """
    Класс запись для датьі в фйал
    """
    def __init__(self, file_name):
        self.file_name = file_name

    def write_file(self, data_to_write):
        with open(self.file_name, 'w', encoding='UTF-8') as f:
            f.write(data_to_write)

data = [
    {'name': "Nick", 'surname': "Var"},
    {'name': "Alex", 'surname': "Var2"}
]
formatter = FormatDataSRP(data)
formatted_data = formatter.prepare()

writer_file = FileWriterSRP('out.csv')
writer_file.write_file(formatted_data)