import hashlib
from concurrent.futures import ThreadPoolExecutor

import tornado.ioloop
import tornado.web
import tornado.gen

# создаем pool из 5 потоков
pool = ThreadPoolExecutor(5)

"""Создам http-сервер который, будет хешировать пароль асинхронно"""


def sync_highload_task(password):
    """
    Синхронная нагруженная, блокирующая функция - как и предедущем примере
    """
    for i in range(9876565):
        password = hashlib.sha256(password).hexdigest().encode()
    return password


@tornado.gen.coroutine
def make_password(password) -> str:
    """как и пред примере запуксает синхронную высоконагрженную функцию в отдельном патоке"""
    # отправляем в отдельный потом и ждем результата
    hashed_password = yield pool.submit(
        sync_highload_task,
        password.encode()
    )
    return hashed_password


class IndexHandler(tornado.web.RequestHandler):
    """
    Пример обработчика HTTP запроса.
    Определяем главную страницу нашего сайта от торнадо
    """

    @tornado.gen.coroutine
    def get(self):
        """
        Отмечаем наш обработчик как корутину, что позволит нам использовать yield.
        """
        value = self.get_query_argument('password', '')  # учае если нам передали параметр password, то мы его берем
        if value:  # если есть значения пароля, то отправляем на хеширование наш пароль
            # хэшируем пароль и дожидаемся ответа
            hashed_password = yield make_password(value)  # дождемся результата хеширования, то ..
            self.write('<h1>Hashed password: {}</h1>'.format(
                hashed_password.decode())
            )  # выводим его  html
        self.write(
            '<form>'
            '<input type="text" name="password" placeholder="Password"/>'
            '<input type="submit"/>'
            '</form>'
        )  # же создадим html что бы пользователь смог ввести новый пароль


def make_app():
    """
    Данная функция создает tornado app c конфигурациями(настройки, роутинг)
    Создаем приложение с urls, autoreload позволит перезгружать сервер по любому изменению файла.
    :return экземпляр класса Application
    """
    url_handlers = [
        tornado.web.URLSpec(r'^/$', IndexHandler, name='index'),
    ]  # определяем набор роутов. name - подадресс, который войдет в регулярное выражения(r'^/$',) нашего url
    # + мы пердаемый целый класс(IndexHandler), в котором должны быть реализованы методы get,post,..,
    # т.е. http метод == метод класса(http get == get())
    return tornado.web.Application(
        url_handlers,
        autoreload=True
    )  # и передаем эту конфигурацию в наш инстанс арр of Application


if __name__ == '__main__':
    app = make_app()
    # прослушиваем порт 8888
    app.listen(8888)
    print('started')
    tornado.ioloop.IOLoop.current().start()


