import re
from os import listdir
from os.path import isfile, join
from time import time
from collections import defaultdict
from logzero import logger, logfile
import logging
import logzero
import json

# local pc dirs
# logfile("/home/nick/PycharmProjects/gutenberg_ebooks/data/logging/counting/counting_logfile.log")
# DIRECTORY_TO_EXTRACT_TO_TXT = '/home/nick/PycharmProjects/gutenberg_ebooks/data/output/txt/'

# dirs for server
logfile("/home/ubuntu/gutenberg_ebooks/data/logging/counting/counting_logfile.log")
DIRECTORY_TO_EXTRACT_TO_TXT = '/home/ubuntu/gutenberg_ebooks/data/output/txt/'


my_formatter = logging.Formatter('%(filename)s - %(asctime)s - %(levelname)s: %(message)s')
logzero.formatter(my_formatter)


files = [f for f in listdir(DIRECTORY_TO_EXTRACT_TO_TXT) if isfile(join(DIRECTORY_TO_EXTRACT_TO_TXT, f))]

COMMON_LST_WORD_FREQUENCY = []

t0 = time()
for idx, file in enumerate(files):
    dir_file_from = ''.join((DIRECTORY_TO_EXTRACT_TO_TXT, file))

    with open(dir_file_from, "r") as f:
        """
        1)учитываем одно значение слова, которые разнятся по имени существительном, прилагательному, количественному показателю или
         глаголу как разные (т.е. к примеру это четыре разных слова: 'attract', attracts, 'attracted' and 'attractive')
        2)убираем все числа, знаки вопроса, восклицания, кавычки, двоеточия, слеши и т.п. и берем отдельно слово
        3)учитываются только те слова у которых длина больше одной буквы
        """
        try:
            lines = f.read()
        except Exception as e:
            logger.error(f'The file #{idx} {file} has next problem')
            print(f'The file #{idx} {file} has next problem', e)
            continue

        litters_for_removing = '[!|[|?|,|.|;|$|=|<|>|/|@|#|*|=|(|)||_|\n|&|0|1||"|2|3|4|5|6|7|8|9|-|:]'

        cleaned_text = re.sub(litters_for_removing, " ", lines)

        for word in cleaned_text.strip().split(' '):
            if word != '' and len(word) > 1:
                COMMON_LST_WORD_FREQUENCY.append(word.lower())
        print(f'File #{idx} {file} was processed')

logger.warning(f'time spend on loop and collecting all words to list: {time() - t0}. \n \
Now starts process of calculating words in list with common words {len(COMMON_LST_WORD_FREQUENCY)}, need some time...')


dct_counted_common_words = defaultdict(lambda: 0)
t1 = time()
for idx, word in enumerate(COMMON_LST_WORD_FREQUENCY):
    dct_counted_common_words[word] += 1
    print(f'left words {len(COMMON_LST_WORD_FREQUENCY) - idx + 1}')
logger.warning(f'time spend on calculating words in list: {time() - t1}')

sorted_dict_book_words = {k: dct_counted_common_words[k] for k in sorted(dct_counted_common_words, key=dct_counted_common_words.get, reverse=True)}
ten_top_common_words = {k: sorted_dict_book_words[k] for k in list(sorted_dict_book_words)[:1000]}


def create_json_top_1000_common_words(dictionary):
    with open("/home/nick/PycharmProjects/gutenberg_ebooks/data/output/results/top_1000_common_words.json", "w") as outfile:
        json.dump(dictionary, outfile, indent=4, ensure_ascii=False)
        print('File json_top_1000_common_words was successfully created')


def create_json_with_whole_counted_words(dictionary):
    with open("/home/nick/PycharmProjects/gutenberg_ebooks/data/output/results/whole_counted_words.json", "w") as outfile:
        json.dump(dictionary, outfile, indent=4, ensure_ascii=False)
        print('File json_with_whole_counted_words was successfully created')


create_json_top_1000_common_words(ten_top_common_words)
create_json_with_whole_counted_words(sorted_dict_book_words)



