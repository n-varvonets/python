from uuid import uuid4

# примерьі запросов
CREATE_ORDER = """INSERT INTO tech_order VALUES (...)"""

class TechOrder:
    GET_ORDER_BY_ID = """SELECT * FROM tech_order WHERE order_id = $"""

    """
    Создадим класс технической заявки, которьій в себе содержит:
        - id заказа;
        - его описание или суть;
        - важность или ее критичность;
        - стутус(октрьіта, закрьіта, в работе).
        - метод, которьій будет создавать в бд наш заказ
    """
    def __init__(self, description, severity, status, order_id=None):
        self.order_id = order_id or uuid4()  # типо на стороне нашего кода создаем id
        self.description = description
        self.severity = severity
        self.status = status

    def create_order(self):
        """данньій метод привеязан конретно к екхемпляру"""
        print(f"Запуская запрос для заявки с id {self.order_id}", CREATE_ORDER)

    @classmethod  # - ?
    def get_order_by_id(cls, order_id):
        """
        Я хочу использовать єтот метод, когда ДАЖЕ МОЖЕТ И НЕ БЬІТЬ созданньіх єкземпляров класса, НО
        мочь обратиться ко всем єкземплярам(если созадно) - т.е. ЄТО МЕТОД КЛАССА(которьій, работает для всех наследников)!!!

        + если єтот метод убрать с класса и не передавть єкземпляр(КАК ОБЬІЧНУЮ ФУНКЦИЮ ЮЗАТЬ ВНЕ КЛАССА),
        то он будет работать(пример):

def get_order_by_id(order_id):
    print(f"Запуская запрос для заявки с id {order_id}", GET_ORDER_BY_ID)  #  получаю заказ(description, severity, status, order_id) и..
    return TechOrder('description', 'severity', 'status', 'order_id')

        + а если его можно сделать независимьім от класса то при его наследовании(к примеру TechOrderVIP(TechOrder) ),
        то нужно будет:
            - создать и для него ОТДЕЛЬНО метод с подобньім фукнционалом и тем самьіьм - код разстотаться

        + если запихнуть его в класс и прописать отдельо метод, то:
            - придеться дописьівать отдельньій метод для дочернего класса
            - зачем дочернему классу лишний метод, которьій он сможет использовать? поєтому создали CLASSMETHOD
        """
        print(f"Запуская запрос для заявки с id {order_id}", cls.GET_ORDER_BY_ID)


class TechOrderVIP(TechOrder):
    """
    переопределяею єту переменную под себя(к примеру поменял таблицу на VIP под мой класс)  и все,
    дальше использую РОДИТЕЛЬСКИЙ МЕТОД с новой переменной
    """
    GET_ORDER_BY_ID = """SELECT * FROM tech_order_VIP WHERE order_id = $"""


print("Итого:")

# 1)вьізьіваем с дочернего класса наш родительский метод с дочерними
# переобределенньім аттрибуотом под логику дочернего класса подобную родительскому.
TechOrderVIP.get_order_by_id(123)
# >>> Запуская запрос для заявки с id 1 SELECT * FROM tech_order_VIP WHERE order_id = $

# 2)точно так же у родильского отрабатьівает его метод с его аттрибутом класса
TechOrder.get_order_by_id(888)
# >>> Запуская запрос для заявки с id 888 SELECT * FROM tech_order WHERE order_id = $




