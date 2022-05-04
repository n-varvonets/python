import json
import os
import uuid
from typing import ClassVar

"""Фикстуры в контексте PyTest — это вспомогательные функции для наших тестов, которые не являются частью тестового сценария.
Назначение фикстур может быть самым разным. Одно из распространенных применений фикстур — это подготовка тестового
окружения и очистка тестового окружения и данных после завершения теста. Но, вообще говоря, фикстуры можно использовать
для самых разных целей: для подключения к базе данных, с которой работают тесты, создания тестовых файлов или подготовки
 данных в текущем окружении с помощью API-методов.
Классический способ работы с фикстурами — создание setup- и teardown-методов в файле с тестами"""


class Counter:
    """
    класс Counter создан специально для тестового подсчета вызова фикстур, т.е. наших тестовых функций.
    основаные модели User и Post наслдеуются от него что с fixture=False и Counter никак не виляет на их основную работу.
    в test_models.py -> def test_constructor() мы создаем тест-инстанс user  и что бы в каждом тест-методе не определять
    его, то conftest определяем его создание и дальше используем как фикстуру в наших тест-методах.
    """

    counter: ClassVar[int] = 0

    def __init__(self, fixture):  # fixture
        if fixture:
            self.update_counter()

    def update_counter(self):
        """
        сохраняем кол-во вызовов конструтора __init__ класса Counter. Т.е. сколько инстансов у нашего подкласса User
        """
        self.__class__.counter += 1  # увеличивает у класса каунтер(кол-во екземпляров)
        name = self.__class__.__name__.lower()  # приводит к нижнему регистру его имя и сохраняет
        data = {}
        if os.path.exists('results.json'):  # ли есть уже результат то читаем файл и добавляем в не дату
            with open('results.json', 'r') as f:
                data = json.load(f)
        data.setdefault(name, 0)  # D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D.
        # т.е. если список имеет имя класса, то ничего не делаем,
        # если нет, то устанавливаем первый эелемент с именем и значением 0
        data[name] += 1  # увеличиваем предедущее значение на еденицу, т.к. по кругу прошлись и создали новый инстанс(вызвали конструктор)
        with open('results.json', 'w') as f:
            json.dump(data, f)


class User(Counter):

    def __init__(self, email, first_name, last_name, uid=None, fixture=False):
        super().__init__(fixture)  # если передана fixture, то counter в results.json будет увеличиваться,
        # т.е. для обычном работы класса fixture - не нужен
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = uid or uuid.uuid4()

    def get_full_name(self):
        return '{first_name} {last_name}'.format(
            first_name=self.first_name,
            last_name=self.last_name
        )

    def __str__(self):
        return 'User: <{id}: {name}>'.format(
            id=self.id,
            name=self.get_full_name()
        )


class Post(Counter):

    def __init__(self, user, comment: str, fixture=False):
        super().__init__(fixture)
        self.user = user
        self.comment = comment
