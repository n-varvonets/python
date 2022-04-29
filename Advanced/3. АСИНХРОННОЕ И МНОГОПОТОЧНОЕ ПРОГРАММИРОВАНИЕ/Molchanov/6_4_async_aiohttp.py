import asyncio
import aiohttp  # asyncio оставляет работу для протоковол udp/tcp (уровень сокетов). интрнет протокла http него нет
from time import time

# документация aiohttp подчеркивает что все запросы клиент-сервер лучше делать
# через сессии(async with) - т.к. длительное общение


def write_image(data):
    """
    Синхронная функция потому что - asyncio не предоставляет возможность работы с файловыми обьектами(запись картинки).
    Такая возможность есть у библиотеки aiofiles(потоки), но для примера сделать блочную функции(так делать не нужно).
    Даже несмотря что write_image будет синхронным(будет блочить выполнение других функций) - все равно прирост
    скорости будет значительным.
    Ньюанс: что бы вызвать асинхронную функцию, то наш ВЫЗЫВАЮЩИЙ код тоже должен быть асинхронным,
    т.е. вызов всех асинхронных функций выполняется их корутин(async def), НО...
    внутри асинхронных функций, мы можем исползовать синхронный код
    """
    filename = f'test_imgs/file-{int(time() * 1000)}.jpeg'
    with open(filename, 'wb') as file:
        file.write(data)


async def get_content(url, session):
    # with open - сессия это что-то вроде как чтение-запись файла
    async with session.get(url, allow_redirects=True) as response: # allow_redirect точно для того же что и в прошлом примере
        data = await response.read()  # блок функцию на одну единцу чего-то
        # теперь нужно продолжить корутину и записать в файл
        write_image(data)  # да, синхронную функцию... описание почему внутри функции


async def main():
    """
    здесь я должен открыть сессию и 20ть раз вызвать get_content
    """
    url = 'https://loremflickr.com/320/240'
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(20):
            # того что бы наша корутина попвала в очередь задач - её нужно обернуть в класс Task via create_task().
            # поскольку у нас будет 10ть вызовов, то эти 10ть задач нужно где-то хранить(список который буду наполнять).
            # task = asyncio.create_task(get_content(url, session))
            task = asyncio.ensure_future(get_content(url, session))
            tasks.append(task)

        # затем внутри сессии я должен дождаться результат работы корутин и вызвать метод gather
        await asyncio.gather(*tasks)  # gather ушает изменений наших корутин(async def) принимает
        # распакованную последовательность корутин

if __name__ == '__main__':
    t0 = time()
    # asyncio.run(main())
    loop = asyncio.get_event_loop()  # здадим обьект ивент лупа
    loop.run_until_complete(main())  # говорим обьекту слушать генератор пока не будет прерван цикл
    loop.close()
    print(time() - t0)