from uuid import uuid4


class Tumbochka:
    """Какой-то родетельский класс с его переенной class_tmb_cnt"""
    class_tmb_cnt = 0
    def __init__(self, id):
        self.tumb_id = id
        Tumbochka.class_tmb_cnt += 1

    def open_door(self):
        print(f"Открили дверь тумбочки с id {self.tumb_id}")

    @staticmethod
    def cut_by_scissors(smth):
        print(f"Режим ножницами {smth}")

    @classmethod
    def show_me_total_tumb_count(cls):
        return cls.class_tmb_cnt


class ProTumbChild(Tumbochka):
    """Какой-то дочерней класс с его переенной class_tmb_cnt"""
    class_tmb_cnt = 100500



