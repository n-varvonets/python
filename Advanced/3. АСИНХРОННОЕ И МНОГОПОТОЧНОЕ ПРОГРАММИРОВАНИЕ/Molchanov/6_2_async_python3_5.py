"""Изменения преднедщего кода asyncio с выходом python3.5:
- все тоже сомое, но заменили декораторы на async def  и  yield from на await и оно работает;
- (необязательно) но пайтон3.5 использует еще create_task вместо ensure_future и if main  изменили.
"""

import asyncio


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print(f'{count} seconds passed')
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.ensure_future(print_nums())
    task2 = asyncio.ensure_future(print_time())
    # task1 = asyncio.create_task(print_nums())
    # task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()  # здадим обьект ивент лупа
    loop.run_until_complete(main())  # говорим обьекту слушать генератор пока не будет прерван цикл
    loop.close()
    # asyncio.run(main())
