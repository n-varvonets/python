import requests
from time import time


def get_file(url):
    """функция запрос на сервер(I/O)"""
    r = requests.get(url, allow_redirects=True)  # allow_redirects , т.к. эта ссылка редиркетит на другую рандомную с котиками
    return r


def write_file(response):
    # укзываем имя фаайла из ответа url разбив по слешу и взяв посл елемент как название файла
    # https://loremflickr.com/cache/resized/4775_39828746875_3f1507d934_320_240_nofilter.jpg
    filename = f"test_imgs/{response.url.split('/')[-1]}"
    with open(filename, 'wb') as file:  # для записи бинарного файла(картинки)
        file.write(response.content)  # и записываю контент бинарника в файл


def main():
    """
    в данной функци  мы 20 раз вызовем две последовательные функции
    и посмотрим за сколько времени она отрабатала
     """
    url = 'https://loremflickr.com/320/240'
    t0 = time()
    for i in range(20):
        write_file(get_file(url))
    print(time() - t0)


if __name__ == '__main__':
    main()