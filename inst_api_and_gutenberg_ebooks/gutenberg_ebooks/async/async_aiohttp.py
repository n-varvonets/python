import asyncio
import aiofiles as aiofiles
import aiohttp
import json
from logzero import logger
from collections import defaultdict
from add_data import *
from bs4 import BeautifulSoup
from multiprocessing import Pool


# @time_of_function
def get_count_duplicated_words(lst_words_in_books: List[str]) -> Dict[str, int]:
    """
    Используем самый быстрый алгоритм подсчета дупликатов слов нашего списка via библиотеки collections
    :param lst_words_in_books: список слов
    :return dct_counted_common_words: словарь, где ключ=слово из книги, а значение -его количество дупликатов в книге
    """
    dct_counted_common_words = defaultdict(lambda: 0)
    for idx, word in enumerate(lst_words_in_books):
        dct_counted_common_words[word] += 1

    return dct_counted_common_words


# @time_of_function
def _set_up_pack(HOW_MUCH_BOOKS_DOWNLOAD: int, cnt_packs: int = 0) -> Tuple[int, int]:
    """
    Рекурсивно задаем диапазон книг которой скачать,
    :return cnt_packs: список покетов[int] и число оставшихся файлов в неполном пакете[int]
    """

    if HOW_MUCH_BOOKS_DOWNLOAD < PACK_SIZE:
        return cnt_packs, HOW_MUCH_BOOKS_DOWNLOAD
    else:
        HOW_MUCH_BOOKS_DOWNLOAD -= PACK_SIZE
        cnt_packs += 1
        return _set_up_pack(HOW_MUCH_BOOKS_DOWNLOAD, cnt_packs)


# @time_of_function
def make_cleaned_context(soup: str) -> str:
    """
    Фильтруем уже читабельный текст:
        - делим(обрезаем) хедер представления сайта gutenberg(тип.1 ) по тексту "THE SMALL PRINT! FOR PUBLIC DOMAIN ETEXTS"
        - делим(обрезаем) хедер представления сайта gutenberg(тип.1 ) по тексту 'All of the original'
        - убираем ненужные буквы от слов '[!|[|?|,|.|;|$|=|<|>|/|@|#|*|=|(|)||_|\n|\r|&|0|1||"|2|3|4|5|6|7|8|9|-|:]'
    :param soup: ниш текст книги, который нужно отфильтровать
    :return: cleaned_text: уже отфильтрованный текст
    """

    # first filter
    soup = make_first_filter(soup)

    # second filter
    soup = make_second_filter(soup)

    # third filter
    cleaned_text = make_third_filter(soup)

    return cleaned_text


# @time_of_function
def get_words_lst_form_book(cleaned_text: str) -> List[str]:
    """
    Фильтр условий:
        - исключаем часто повторяющиеся слова не из самого содержания книги, а просто потому что добавлены \
         от сайта как их подпись ['ebooks', 'project', 'gutenberg', '’s', 'etext']
         - текст делим по пробелу в lst_cleaned_text[lst]
         - если слово меньше единицы или входит в наш список слов для исключения и не пустая строка, то
         добавляем его в наш список слов книги lst_words_in_books[lst]
    :param cleaned_text: наш очищенный и отфильтрованный текст
    :return lst_words_in_books: список слов в книге
    """
    lst_excluded_words = ['ebooks', 'project', 'gutenberg', '’s', 'etext', '--']

    lst_words_in_books = []
    lst_cleaned_text = cleaned_text.split(' ')
    for word in lst_cleaned_text:
        if word != '' and len(word) > 1 and word.lower() not in lst_excluded_words:
            lst_words_in_books.append(word.lower())

    return lst_words_in_books


async def create_json(dct_counted_duplicated_words_book: Dict[str, int], json_words_book: int) -> None:
    """
    Create a new json file with counted words in book via async method
    :param dct_counted_duplicated_words_book: Lst words of book;
    :param json_words_book: idx of book;
    :return None: but in inner dir of project should be created a new json with counted words and print/log
    about status of operation.
    """
    json_name = PATH_TO_JSON_WORDS_BOOK + f'{json_words_book}.json'

    async with aiofiles.open(json_name, mode='w') as f:
        await f.write(json.dumps(dct_counted_duplicated_words_book, indent=4, ensure_ascii=False))
        logger.info(f'File #{json_words_book} was processed')


async def create_json_counted_words_of_book(
        no_book: int, session: [ClientSession], change_url: bool = False, second_try_for_first_url: bool = False
) -> None:
    """
    Пробуем по первой ссылке асинхронно достучаться к ресурсу как к обьекту response,
        если статус 200, то:
            - асинхронно конвертируем сырую дату в текст;
            - очищаем текст от ненужных символов и возвращаем cleaned_text[str];
            - синхронно разделяем содержимое очищенной книги по словам и получаем lst_words_in_books[Lst[str]];
            - синхронно считаем наш список дупликатов(повторяющихся слов) в книге и возвращаем его dct_counted_duplicated_words_book[dct];
            - асинхронно записываем наш список посчитанных слов в json файл
    если нет, то сессия метода get прерывает свою работу,
        тогда пробуем:
            - рекурсивно повторить нашу функцию, но уже с другим url изменив флаг change_url на True;
        в противном случае может ресурс на книгу отсутствовать, тогда:
            - бывает так что асинк не смог достучаться по первой ссылка, а вторая просто для него не релевантна, то \
            в таких активируем вторую попытку для первого(как следствие и для второго url) выставив \
            атрибут change_url=False, тем самым рекурсивно прогоняю корутину заново по ссылкам, \
            - но если во второй раз обе окажутся 404, то second_try_for_first_url=True уже будет активным и попадем в \
            исключение, которое говорит что действительно уже ресурс может быть неактивным и стоит через лог проверить его.
    :param second_try_for_first_url:
    :param no_book: индекс книги;
    :param session: сессия корутины
    :param change_url: флаг одного из двух типов нашего url
    :return None: but in dir data/output/json_books has to be created a new json file with counted words for each book
    """
    try:

        url = get_book_url(no_book, change_url)

        async with session.get(url) as response:
            assert response.status == 200

            text = await response.text()

            cleaned_text: str = make_cleaned_context(text)
            lst_words_in_books: List[str] = get_words_lst_form_book(cleaned_text)
            dct_counted_duplicated_words_book: Dict[str, int] = get_count_duplicated_words(lst_words_in_books)

            await create_json(dct_counted_duplicated_words_book, no_book)

    except:
        if not change_url:
            await create_json_counted_words_of_book(no_book, session, change_url=True)

        else:
            if not second_try_for_first_url:
                await create_json_counted_words_of_book(no_book, session, change_url=False,
                                                        second_try_for_first_url=True)
            else:
                logger.error(f'Check url of file #{no_book}')


async def main() -> None:
    """
    Launch our event loop and collect tasks in which we asynchronously access the book reuses and write their context
    in json with the already counted number of duplicate words in the book
    :return None: but has to be created a new json file in local dir with counted q-ty duplicates in book
    """
    async with aiohttp.ClientSession() as session:
        tasks = []

        for idx_pack in range(packs):

            start_from_dyn_increase = START_FROM_BOOK + (idx_pack * PACK_SIZE)

            for no_book in range(start_from_dyn_increase, start_from_dyn_increase + PACK_SIZE):
                task = asyncio.ensure_future(create_json_counted_words_of_book(no_book, session))
                tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    """
    Below need to indicate:
        - from which book should start downloading books;
        - q-ty books for downloading.  
        - len books in one pack (need to reduce the stress on the RAM);
    after that we activate two cores and execute them into two pools(processes) from multiprocessing \
    for running our event_loop.
    """
    START_FROM_BOOK: int = 57_600
    HOW_MUCH_BOOKS_DOWNLOAD: int = 2400  # HOW_MUCH_BOOKS_DOWNLOAD should be equal of PACK_SIZE otherwise, the rest of \
    # the files will be discarded; like if PACK_SIZE = 25, then HOW_MUCH_BOhtOKS_DOWNLOAD should be 25, 50, 75, 400, ...
    PACK_SIZE: int = 20  # чем меньше число, тем меньше нагрузка на cpu. т.е. это наше кол-во тасок на ядро и как
    # следствие более упорядоченное выполнения тасок с меньшей нагрузкой

    packs, remained_files = _set_up_pack(HOW_MUCH_BOOKS_DOWNLOAD)

    pool = Pool(processes=2)
    loop = asyncio.get_event_loop()

    pool.map(loop.run_until_complete(main()), range(packs))

    loop.close()
