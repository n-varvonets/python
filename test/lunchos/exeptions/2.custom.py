print(" -----  1.) Ислючения можно воозбуждать raise ----- ")
def main_f_excptn():
    """
    по логике в єтой функции мьі предпологаем исключение на ноль, но есть ввести не число,
    а строку, то будет еще и ValueError
    """
    while True:
        a = input("enter a")
        b = input("enter b")
        try:


            # добавим логику собственного исключения,что нельзя передавать больше значение больше ста
            if a > 100 or b > 100:
                raise ValueError("Out of value for variable")

            print(a / b)
        except ZeroDivisionError as e:
            print(e, "Division by zero!!!")
        except ValueError as err:
            print(err)  # "Out of value for variable" - наше сообшение
            print("Here's my logic processing of ValueError")

# main_f()

print(" -----  2.) Проблема raise и зачем кастомньіе исклчения ----- ")
# нужен, когда мьі хотим кастомизировать исключение лично под нашу лоигку(больше сто - нельзя и вівьодить соответв сообщение)
from  datetime import datetime


class OutOfValue(Exception):
    def __init__(self, text, time):
        self.text = text
        self.time = time


def main_f_2():

    while True:
        a = input("enter for err value more than 100")
        b = input("enter for err value more than 100")  # 101
        try:
            a = float(a)
            b = float(b)

            if a > 100 or b > 100:
                raise OutOfValue("Out of value for variable", datetime.now())
                # raise OutOfValue("Out of value for variable", datetime.now(), 's')
            print(a / b)
        except ValueError as err:
            print(f"Here's my logic processing of ValueError, {err}")
        except OutOfValue as err:
            print(err, '--- here ---')


main_f_2()

