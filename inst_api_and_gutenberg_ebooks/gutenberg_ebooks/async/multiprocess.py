from multiprocessing import Pool
from os.path import isfile, join
from os import listdir
import json
from time import time


DIRECTORY_EXTRACT_FROM = '/home/nick/PycharmProjects/gutenberg_ebooks/data/output/json_books/'
PACK_SIZE = 100  # q-ty books in pack


def get_dct_counted_word_of_pack(idx_pack, pack):

    dct_pack_counted_words = dict()

    for name_book in pack:
        json_dir = DIRECTORY_EXTRACT_FROM + str(name_book)
        with open(json_dir) as f:
            dct_words_in_book = json.load(f)
            for key, value in dct_words_in_book.items():
                if key in dct_pack_counted_words:
                    dct_pack_counted_words[key] += value
                else:
                    dct_pack_counted_words[key] = value

    return dct_pack_counted_words


def create_json_top_5000_common_words_of_pack(dct_top_5000_words, idx_pack):
    filename = f'/home/nick/PycharmProjects/gutenberg_ebooks/data/output/results/{idx_pack}.json'
    with open(filename, "w") as outfile:
        json.dump(dct_top_5000_words, outfile, indent=4, ensure_ascii=False)


def create_words_results(pack):

    dct_counted_word_of_pack = get_dct_counted_word_of_pack(pack[0], pack[1])

    top_5000_the_most_common_words_of_pack = {k: dct_counted_word_of_pack[k] for k in list(dct_counted_word_of_pack)[:5000]}

    # add names_books_in_pack
    top_5000_the_most_common_words_of_pack[f'_{pack[0]}'] = pack

    create_json_top_5000_common_words_of_pack(top_5000_the_most_common_words_of_pack, pack[0])
    print(f'The result of counted words was created for books: {pack}')


if __name__ == '__main__':
    lst_books = [f for f in listdir(DIRECTORY_EXTRACT_FROM) if isfile(join(DIRECTORY_EXTRACT_FROM, f))]

    packed_lst_books = {}

    if len(lst_books) > PACK_SIZE:

        # collect pack
        for idx_pack in range((len(lst_books) // PACK_SIZE)+1):
            packed_lst_books[f'pack_{idx_pack+1}'] = lst_books[PACK_SIZE*idx_pack+1:PACK_SIZE*idx_pack+1 + PACK_SIZE]

        pool = Pool(processes=3)
        pool.map(create_words_results, packed_lst_books.items())

    else:
        packed_lst_books = lst_books
        pool = Pool(processes=3)
        pool.map(create_words_results, packed_lst_books)