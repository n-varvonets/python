# SOLID - крепкий, - єто принципьі как пострить код из пунктов

# принципьі, правила - хорошо, но не нужно забьівать о здравом смьісле - т.е. НЕ бьіть слишком
# педантичньім и следовать всем правилам, там где єто ладе и не нужно(И ЄТО НЕ ТОЛЬКО ПРО айти)

"""Single responsibility - один класс должен иметь только одну зону ответсенности"""
class ExportCsv:
    """
    Данньій класс нарушает:

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
