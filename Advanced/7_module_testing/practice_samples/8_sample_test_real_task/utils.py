# есть 3 утилиты(какие-то рабочие функции для нашего модуля)..
# 1 - отправки почты
# 2 - конкатенации
# 3 - присваение инстансу нового аттрибута

def send_mail(email: str, subject: str, body: str):
    print(email, subject, body)


def concat_name(first_name: str, last_name: str):
    return '{first_name} {last_name}'.format(
        first_name=first_name,
        last_name=last_name
    )


def set_user_meta(instance, value: dict):
    instance.meta = value
