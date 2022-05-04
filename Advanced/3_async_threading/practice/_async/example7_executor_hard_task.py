import asyncio

"""
Бывают такие ситация когда нам высоконагруженную задачу нужно запустить в отдельном треде. 
Т.е. возникает блокирующая задача, которую мы не можем запускать в event_loop
"""

def highload_operation(value):
    result = 0
    for i in range(0, value):
        result += i
    return result


async def main(value):
    """определяем нашу высоконагруженную функцию, которая выполняет сложные вычисления,
    т.е - НЕПОЗВОЛИТЕЛЬНО ДОЛГО ЧТО БЫ ЗАПУСКАТЬ ЭТУ ЗАДАЧУ В цикле событий - тем самым блкоируя поток"""
    # выполнение синхронной задачи в pool-е и получение результата.
    result = await loop.run_in_executor(None, highload_operation, value)   # None - то наш екзекьютер(может
    # инциализатор, честно, - хз, так тип сказал...),
    # highload_operation - наша синхронная функция и дальше пармтры функции. Т.е. пока в отдельном потоке
    # не вычислиться значение функции highload_operation(), т.е. пока не return result - наша сопрограмма уснет
    print('Result is {}'.format(result))


loop = asyncio.get_event_loop()
tasks = asyncio.wait([
    loop.create_task(main(10_000_000)),  #  это те же 10 миллионов - только _ это как условная точка, как ниже
    loop.create_task(main(10000000)),
])
loop.run_until_complete(tasks)
loop.close()
