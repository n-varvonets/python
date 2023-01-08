"""Если большое кол-во процесов, то лучше использовать Pool, чем Process"""  # т.е. байсейн процессов(много процессов)
import os
from multiprocessing import Pool
from time import sleep


def f(x):
    print(os.getpid(), "sleep!")
    sleep(1)
    return x * x


if __name__ == "__main__":
    # pool = Pool(2)
    # res = pool.map(f, (1, 2, 3, 4, 5))  # примает функцию и ожидаемо запустить ее в пулле процесов для множества аргументов
    # res = pool.apply(f, (1,))  # ипользуем тогда, когда хотим ЕДИНОЖДЬІ запустить функцию в пуле для OДНОГО аргумента

    with Pool(processes=4) as pool:  #  хорошо бьі закрівать пулл после его работьі
        # можно как parial_object его поместить в обьект и вьівзвать в том момменте, где он нам нужен
        res_partial_object = pool.map_async(f, (1, 2, 3, 4, 5, 6))
        print(res_partial_object)  # <multiprocessing.pool.MapResult object at 0x10f2f0790>
        print(res_partial_object.get())  # [1, 4, 9, 16, 25, 36]

