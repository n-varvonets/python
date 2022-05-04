import uuid
from utils import send_mail  # з нашего модуля импортируем наши доп функции для взаимодействия с классом(утилиты)

SUBJECT_REGISTRATION = 'Welcome, {name}!'
BODY_REGISTRATION = 'You are welcome!'


class User:

    def __init__(self, email, first_name, last_name, uid=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = uid or uuid.uuid4()

    def get_full_name(self):
        return '{first_name} {last_name}'.format(
            first_name=self.first_name,
            last_name=self.last_name
        )

    def send_mail(self):
        """отправка почты... - сейчас это заглушка, но могла быть реальная отправка"""
        send_mail(
            self.email,  # эемейлом пользователя
            SUBJECT_REGISTRATION.format(name=self.get_full_name()),  # темой регистрации
            BODY_REGISTRATION  # тело регистрации
        )

    def __str__(self):
        """метод стр возращает такую строку при взятии инстанса как обьекта"""
        return 'User: <{id}: {name}>'.format(
            id=self.id,
            name=self.get_full_name()
        )
