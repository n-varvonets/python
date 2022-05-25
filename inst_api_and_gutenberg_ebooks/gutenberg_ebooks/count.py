import re
from os import listdir
from os.path import isfile, join
from time import time
from collections import defaultdict


DIRECTORY_TO_EXTRACT_TO_TXT = '/home/nick/PycharmProjects/gutenberg_ebooks/data/output/txt/'

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
        3)учитываются только те слова у которых длина больше 2х букв(т.е. исключаем слоги и 'I', 'be' 'of', 'if' 'is', 'am', 'a' и т.д.)
        4)исключил ['the', 'and', 'for', 'not', 'that', 'this', 'which', 'may', 'are', 'shall', 'have', 'but',
                                     'with', 'the', 'from', 'will', 'would', 'you', 'all', 'any', 'other', 'their', 'our', 'them',
                                     'such', 'has', 'they', 'these', 'can', 'what', 'within', 'into', 'been', 'his'] \
        из списка хоть они и подходит под условие длины как и остальные 'end', 'run'.. но т.к. стало очевидно что они служат для \
        того что бы построить предложения и используется в поражающем большинстве случаев относительно остальных слов (список 
        подобных слов можно обговорить и исключить из выборки)
        """
        try:
            lines = f.read()
        except Exception as e:
            print(f'The file #{idx} {file} has next problem', e)
            continue

        litters_for_removing = '[!|[|?|,|.|;|$|=|<|>|/|@|#|*|=|(|)||_|\n|&|0|1||"|2|3|4|5|6|7|8|9|-|:]'
        lst_excluded_common_words = ['the', 'and', 'for', 'not', 'that', 'this', 'which', 'may', 'are', 'shall', 'have', 'but',
                                     'with', 'the', 'from', 'will', 'would', 'you', 'all', 'any', 'other', 'their', 'our', 'them',
                                     'such', 'has', 'they', 'these', 'can', 'what', 'within', 'into', 'been', 'his',
                                     'etext', 'you', 'ebooks', 'gutenberg']

        cleaned_text = re.sub(litters_for_removing, " ", lines)

        for word in cleaned_text.strip().split(' '):
            if word != '' and len(word) > 2 and word not in lst_excluded_common_words:
                COMMON_LST_WORD_FREQUENCY.append(word.lower())

        print(f'File #{idx} {file} was processed')


print(f'time spend on loop and collecting all words to list: {time() - t0}. \n \
Now starts process of calculating words in list with common words {len(COMMON_LST_WORD_FREQUENCY)}, need some time...')


dct_counted_common_words = defaultdict(lambda: 0)
t1 = time()
for idx, word in enumerate(COMMON_LST_WORD_FREQUENCY):
    dct_counted_common_words[word] += 1
    print(f'left words {len(COMMON_LST_WORD_FREQUENCY) - idx + 1}')
print(f'time spend on calculating words in list: {time() - t1}')

sorted_dict_book_words = {k: dct_counted_common_words[k] for k in sorted(dct_counted_common_words, key=dct_counted_common_words.get, reverse=True)}
ten_top_common_words = {k: sorted_dict_book_words[k] for k in list(sorted_dict_book_words)[:10]}
print(ten_top_common_words)

# обработал 200 книг - это 13 млн слов

most = {
 'was': 155491, 'had': 100944, 'her': 94727, 'she': 81046, 'him': 73028, 'and': 56517, 'said': 54556, 'were': 50232, 'one': 45924,
 'there': 43965, 'when': 40560, 'out': 34473, 'your': 33487, 'who': 32176, 'then': 31740, 'upon': 29821, 'more': 29168, 'now': 29033,
 'man': 28147, 'about': 26902, 'could': 26871, 'but': 24829, 'than': 24349, 'lord': 23903, 'thou': 23741, 'unto': 23495, 'some': 22592,
 'did': 22581, 'like': 22580, 'time': 22552, 'very': 21531, 'over': 21263, 'before': 21118, 'see': 20950, 'come': 20693, 'little': 19948,
 'know': 19762, 'only': 18679, 'should': 18593, 'came': 18592, 'good': 18199, 'down': 18145, 'thy': 18054, 'must': 17774, 'made': 17544,
 'people': 17376, 'two': 16934, 'after': 16726, 'how': 16718, 'its': 16443, 'great': 16186, 'day': 16035, 'say': 15686,
 'well': 15666, 'project': 15614, 'thee': 15508, 'first': 15390, 'way': 15279, 'again': 15193, 'god': 14980, 'make': 14824,
 'never': 14799, 'much': 14623, 'work': 14610, 'even': 14477, 'men': 14226, 'where': 14165, 'might': 13989, 'here': 13912,
 'own': 13909, 'rate': 13696, 'went': 13576, 'land': 13508, 'away': 13152, 'through': 13090, 'hand': 13053, 'back': 13049,
 'most': 13009, 'house': 13008, 'old': 13007, 'est': 12889, 'long': 12686, 'let': 12562, 'every': 12520, 'for': 12388,
 'without': 12310, 'himself': 12289, 'life': 12112, 'things': 12091, 'too': 12053, 'years': 12047, 'think': 11973, 'yet': 11853,
 'take': 11846, 'also': 11826, 'being': 11697, 'those': 11677, 'eyes': 11677, 'many': 11591, 'they': 11312
}

