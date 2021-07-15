# Декораторы - это просто функции
def my_decorator(func):
    print("Я обычная функция")

    def wrapper():
        print("Я - функция, возвращаемая декоратором")
        return func()

    return wrapper  # МЫ ВОЗВРАЩАЕМ ОБЬЕКТ, а не вызываем функцию

# Так что, мы можем вызывать её, не используя "@"-синтаксис:
def lazy_function():
    print("zzzzzzzz")

decorated_function = my_decorator(lazy_function)
print('---')
decorated_function()
print('---')


# выведет: Я обычная функция

# Данный код выводит "Я обычная функция", потому что это ровно то, что мы сделали:
# вызвали функцию. Ничего сверхъестественного

@my_decorator
def lazy_function():
    print("zzzzzzzz")  # выведет: Я обычная функция