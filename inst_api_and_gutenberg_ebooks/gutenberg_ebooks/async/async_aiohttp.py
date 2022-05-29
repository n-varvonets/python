import asyncio
import aiohttp
from time import time
from logzero import logger, logfile
import logging
import logzero
from bs4 import BeautifulSoup
import re
import json
import io
from collections import defaultdict

# local pc dirs
ABS_PATH_TO_CHROMEDRIVER = '/home/nick/PycharmProjects/gutenberg_ebooks/data/input/chromedriver'
logfile("/home/nick/PycharmProjects/gutenberg_ebooks/data/logging/download/download_logfile.log")
DOWNLOAD_DIR = '/home/nick/PycharmProjects/gutenberg_ebooks/data/output/zip'

# dirs for server
# ABS_PATH_TO_CHROMEDRIVER = '/home/ubuntu/gutenberg_ebooks/data/input/chromedriver'
# logfile("/home/ubuntu/gutenberg_ebooks/data/logging/download/download_logfile.log")
# DOWNLOAD_DIR = '/home/ubuntu/gutenberg_ebooks/data/output/zip'

my_formatter = logging.Formatter('%(filename)s - %(asctime)s - %(levelname)s: %(message)s')
logzero.formatter(my_formatter)

LINK = 'https://www.gutenberg.org/files/'


async def get_count_duplicated_words(lst_words_in_books):
    dct_counted_common_words = defaultdict(lambda: 0)
    for idx, word in enumerate(lst_words_in_books):
        dct_counted_common_words[word] += 1

    return dct_counted_common_words


async def make_cleaned_context(soup):
    # check typical header of gutenburg if exit - cut him and take essential text dor file {}-0.txt

    litters_for_removing = '[!|[|?|,|.|;|$|=|<|>|/|@|#|*|=|(|)||_|\n|&|0|1||"|2|3|4|5|6|7|8|9|-|:]'
    phrase_for_first_cutting_text = "THE SMALL PRINT! FOR PUBLIC DOMAIN ETEXTS"

    if phrase_for_first_cutting_text in soup:

        # return first text after first cleaning
        soup = soup.split(phrase_for_first_cutting_text)[-1][24:]

        # second filter
        second_phrase = 'All of the original'
        if second_phrase in soup:
            # просто обрезам вступление состоящие из двух абзацев из 13ти рядков
            soup = ' '.join(soup.split('\r\n')[13:])

    cleaned_text = re.sub(litters_for_removing, " ", soup.strip())

    return cleaned_text


async def get_words_lst_form_book(cleaned_text):

    lst_excluded_words = ['ebooks', 'project', 'gutenberg', '’s', 'etext']

    lst_words_in_books = []

    for word in cleaned_text.split(' '):
        if word != '' and len(word) > 1 and word.lower() not in lst_excluded_words:
            lst_words_in_books.append(word.lower())

    return lst_words_in_books


async def write_data_in_txt(soup, book_name):

    # check typical header of gutenburg if exit - cut him and take essential text dor file {}-0.txt

    cleaned_text = await make_cleaned_context(soup)
    lst_words_in_books = await get_words_lst_form_book(cleaned_text)
    dct_counted_duplicated_words_book = await get_count_duplicated_words(lst_words_in_books)

    json_name = f'/home/nick/PycharmProjects/gutenberg_ebooks/data/output/json_books/{book_name}.json'

    with io.open(json_name, 'w', encoding='utf-8') as f:
        json.dump(dct_counted_duplicated_words_book, f, ensure_ascii=False, indent=4)
        print(f'File #{book_name} was processed')


async def download_file(session, url, book_name):
        async with session.get(url) as response:
            data = await response.read()
            soup = BeautifulSoup(data).get_text()
            await write_data_in_txt(soup, book_name)


async def process_and_download_file(soup, session, no_book):
    if soup.replace('\n', '')[:3] != '404':
        name_book_1 = str(no_book)
        url = LINK + f'{no_book}/{name_book_1}.txt'  # url for first url to download file
        print(f'task {name_book_1} was created')
        await download_file(session, url, name_book_1)
    else:
        try:
            name_book_2 = str(no_book) + '-0'
            url = LINK + f'{no_book}/{name_book_2}.txt'
            print(f'task {name_book_2} was created')
            await download_file(session, url, name_book_2)

        except Exception as e:
            print(f'There is ni such file {no_book} to download book.zip', e)
            logger.error(f'Check url of file #{no_book}')


async def get_content(no_book, session):

    url = LINK + f'{no_book}/{no_book}.txt'
    async with session.get(url) as response:
        data = await response.read()
        soup = BeautifulSoup(data).get_text()

        # 1) download_file()
        await process_and_download_file(soup, session, no_book)


def _set_up_pack(HOW_MUCH_BOOKS_DOWNLOAD, cnt_packs=1):
    """
    Здесь рекурсивоно задаем диапазон книг которой скачать,
    :return: список покетов
    """

    if HOW_MUCH_BOOKS_DOWNLOAD < PACK_SIZE:
        return cnt_packs, HOW_MUCH_BOOKS_DOWNLOAD
    else:
        HOW_MUCH_BOOKS_DOWNLOAD -= PACK_SIZE
        cnt_packs += 1
        return _set_up_pack(HOW_MUCH_BOOKS_DOWNLOAD, cnt_packs)


async def main(idx_pack):

    tasks = []
    start_from_dyn_increase = START_FROM_BOOK + (idx_pack * PACK_SIZE)

    try:
        # важно не возвращать список задач, а то loop.run_until_complete(main(idx_pack)) в цикле \
        # раньше закончится выполнения всех корутин

        async with aiohttp.ClientSession() as session:

            for no_book in range(start_from_dyn_increase, start_from_dyn_increase + PACK_SIZE):
                task = asyncio.ensure_future(get_content(no_book, session))
                tasks.append(task)
            await asyncio.gather(*tasks)

    except:
        print(f'----------{idx_pack}----------')


if __name__ == '__main__':

    # below indicate range books and specify size books in one pack(need to reduce the stress on the RAM)
    START_FROM_BOOK = 2900
    HOW_MUCH_BOOKS_DOWNLOAD = 1100  # rounded  values like 25, 50, 75, 500, ... - в противном случае остаток не скачается
    PACK_SIZE = 200

    t0 = time()

    packs, remained_files = _set_up_pack(HOW_MUCH_BOOKS_DOWNLOAD)

    loop = asyncio.get_event_loop()

    for idx_pack in range(packs):
        loop.run_until_complete(main(idx_pack))  # +1 потому что рэндж начинается с 0, а нам нужно что бы с еденицы
    loop.close()

    print(time() - t0)

