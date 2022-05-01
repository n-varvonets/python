import asyncio


"""
та же самая задача, но уже пошаговое возращение цисел, а не цельное возвращенире
результата списка чисел в отдельном треде(как в прошлом примере) 
"""

@asyncio.coroutine
def test_cor(cor_index, number):
    result = 0
    for i in range(number):
        result += i
        print('--before yield ')
        mock_result = yield from asyncio.sleep(0, result=12)
        # yield from asyncio.sleep(0)
        # yield
        print('Index: {} -> {} + {}'.format(cor_index, i, mock_result))
    return result


event_loop = asyncio.get_event_loop()
tasks = asyncio.wait([
    event_loop.create_task(test_cor(1, 5)),
    event_loop.create_task(test_cor(2, 10))
])
event_loop.run_until_complete(tasks)
event_loop.close()
