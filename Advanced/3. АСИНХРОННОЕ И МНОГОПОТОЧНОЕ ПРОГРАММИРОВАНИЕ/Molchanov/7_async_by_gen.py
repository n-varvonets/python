"""
Любой асинхронный код состоит из двух элементов:
1. Конструкция языка, которая позволяет передавать управление куда-нибудь(yield, yield from, await, callbacks);
2. Event_loop - решает какой код должен выполняться в тот или иной момент.
"""

# для того что бы создать событийный цикл, то наши корутины(задачи) нужно поместить в ОЧЕРЕДЬ выполнения в main()
from time import sleep

queue = []

def counter():
    counter = 0
    while True:
        print(counter)
        counter += 1
        yield  #  не будет ничего возвращать, а просто отдавать управление


def printer():
    """
    создам функцию, которая раз в 3 три итерации будет печатать что-то, но каждую итерацию цикла - отдавать управление
    """
    counter = 0
    while True:
        if counter % 3 == 0:
            print("Bang!")
        counter += 1
        yield


def main():
    while True:
        """что бы выполнять последовательно, то нужно из очереди последовтельно доставать обьект корутины:
        - отправить на выполенеие next() и записываю в конец очереди опять по кругу"""
        g = queue.pop(0)
        next(g)
        queue.append(g)
        sleep(0.5)  # шком быстро выполняется... поэтому блокирующей функцией замедлю на пол секунды


if __name__ == '__main__':

    # terminal 1(check workability def counter()):
    g1 = counter()
    next(counter())  #  >> 0
    next(counter())  #  >> 0
    next(g1)  #  >> 0
    next(g1)  #  >> 1
    for i in range(5):
        next(g1) #  >> 2, ...

    # terminal 2(check workability def printer()):
    g2 = printer()
    next(g2)  # >>> "Bang!"
    next(g2)  # >>>
    next(g2)  # >>>
    next(g2)  # >>>
    next(g2)  # >>> "Bang!"
    next(g2)  # >>>

    print('~~~ Event loop ~~~')

    """
    Теперь нужно заставить эти генераторы работать один за другим. ОЧЕРЕДЬ
    Поэтому сейчас вверху помещу мои корутины в список очереди
    """
    g1_ev_loop = counter()
    queue.append(g1_ev_loop)
    g2_ev_loop = printer()
    queue.append(g2_ev_loop)

    main()



