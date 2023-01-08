from time import sleep
from multiprocessing import Process, Pool
from random import randint
# CASE: как поломать семафору и добиться еффекта одновременной записи процессов в один файл?


# 1.1) Та же ситуция, НО изменим его порядок вьіполнения сделав кучу маленьких сокетов семафор, вместо блока двух больших
def file_writer(start: int, finish: int):
    """Функция будет для кажого значения открьівать и закрівать файл,
    тем самьім будет 10ть маленьких семафор, вместо двух - болших и блокриующих работу другой"""
    for i in range(start, finish):
        with open("test_data/locker.txt", "a") as f_o:
            sleep(randint(0, 3))
            print(i)
            f_o.write(f"{i}\n")


if __name__ == "__main__":
    p1 = Process(target=file_writer, args=(0, 5))
    p2 = Process(target=file_writer, args=(5, 10))
    p1.start()
    p2.start()


# 1.2) результат - если откріть файл , то можно увидеть последоватеьность УЖЕ НЕ отсортированньіх чисел как и вкоонсоли
