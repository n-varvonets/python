# 1. Напишите обьічньій декратор, которьій принимает произвольное число аргументов и ХАРДКОРНО изменяет нашу
# функцию(без динамически переданньіх аргументов, как параметров) и вьіведите ее результат через декоратор как:
#   - синтаксический сахар;
#   - паттерн програмирования.

import datetime
import random

city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 'Odessa', 'Kiev', 'Lviv', 'London']

user_id = random.randint(0, 100)
user_city = random.choice(city_list)
user_action_time = datetime.datetime.now()

def change_id_user(func):
    def inner(*args, **kwargs):
        print('*args, **kwargs')
        return func(*args, **kwargs)
    return inner


def show_user_info(user_id: int, user_city: str, user_action_time: datetime):
    print(f'User #{user_id} from {user_city} was connected at {str(user_action_time)[:-7]}')


@change_id_user
def show_user_info_2(user_id: int, user_city: str, user_action_time: datetime):
    print(f'User #{user_id} from {user_city} was connected at {str(user_action_time)[:-7]}')


change_id_user(show_user_info)(user_id, user_city, user_action_time)
show_user_info_2(user_id, user_city, user_action_time)


