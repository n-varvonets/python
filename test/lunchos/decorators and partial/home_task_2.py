# 1. Напишите Параметрический декоратор, которьій принимает произвольное число аргументов и
# ДИНАМИЧЕСКИ изменяет нашу и вьіведите ее результат через декоратор как:
#   - синтаксический сахар;
#   - паттерн програмирования.

import datetime
import random

city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 'Odessa', 'Kiev', 'Lviv', 'London']

user_id = random.randint(0, 100)
user_city = random.choice(city_list)
user_action_time = datetime.datetime.now()

my_tricky_user_id_for_changing = f'my_tricky_user {random.randint(200, 300)}'


def outer_for_params(*dargs, **dkwargs):
    def change_id_user(func):
        def inner(*args, **kwargs):
            my_changed_args = (dargs[0], args[1], args[2])
            return func(*my_changed_args, **kwargs)
        return inner
    return change_id_user


def show_user_info(user_id: int, user_city: str, user_action_time: datetime):
    print(f'User #{user_id} from {user_city} was connected at {str(user_action_time)[:-7]}')


@outer_for_params(my_tricky_user_id_for_changing)
def show_user_info_2(user_id: int, user_city: str, user_action_time: datetime):
    print(f'User #{user_id} from {user_city} was connected at {str(user_action_time)[:-7]}')


outer_for_params(my_tricky_user_id_for_changing)(show_user_info)(user_id, user_city, user_action_time)
show_user_info_2(user_id, user_city, user_action_time)


