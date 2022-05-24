import re


with open("data/output/1-0.txt", "r") as f:
    """
    1)учитываем одно значение слова, которые разнятся по имени существительном, прилагательному, количественному показателю или
     глаголу как разные (т.е. к примеру это четыре разных слова: 'attract', attracts, 'attracted' and 'attractive')
    2)убираем все числа, знаки вопроса, восклицания, кавычки, двоеточия, слеши и т.п. и берем отдельно слово
    3)учитываются только те слова у которых длина больше 2х букв(т.е. исключаем слоги и 'I', 'be' 'of', 'is', 'am', 'a' и т.д.)
    4)исключил ['the', 'and', 'for', 'not', 'that', 'this', 'which', 'may', 'are', 'shall', 'have', 'but',
                                 'with', 'the', 'from', 'will', 'would', 'you', 'all', 'any', 'other', 'their', 'our', 'them',
                                 'such', 'has', 'they', 'these', 'can', 'what', 'within', 'into', 'been', 'his'] \
    из списка хоть они и подходит под условие длины как и остальные 'end', 'run'.. но т.к. стало очевидно что они служат для \
    того что бы построить предложения и используется в поражающем большинстве случаев относительно остальных слов (список 
    подобных слов можно обговорить и исключить из выборки)
    """
    lines = f.read()

    litters_for_removing = '[!|[|?|,|.|;|$|=|<|>|/|@|#|*|=|(|)||_|\n|&|0|1||"|2|3|4|5|6|7|8|9|-|:]'
    lst_excluded_common_words = ['the', 'and', 'for', 'not', 'that', 'this', 'which', 'may', 'are', 'shall', 'have', 'but',
                                 'with', 'the', 'from', 'will', 'would', 'you', 'all', 'any', 'other', 'their', 'our', 'them',
                                 'such', 'has', 'they', 'these', 'can', 'what', 'within', 'into', 'been', 'his']

    cleaned_text = re.sub(litters_for_removing, " ", lines)

    cleaned_list_words = []
    for word in cleaned_text.strip().split(' '):
        if word != '' and len(word) > 2 and word not in lst_excluded_common_words:
            cleaned_list_words.append(word.lower())

    dct_counted_words = {i: cleaned_list_words.count(i) for i in cleaned_list_words}

    # дальше будет на первое время хардкорно убиранием ненужные слова + 'the', потому что the все таки почему-то появляется
    del dct_counted_words['the']
    del dct_counted_words['etext']
    del dct_counted_words['you']
    del dct_counted_words['ebooks']
    del dct_counted_words['gutenberg']

    sorted_dict = {k: dct_counted_words[k] for k in sorted(dct_counted_words, key=dct_counted_words.get, reverse=True)}

    top_ten_words = {k: sorted_dict[k] for k in list(sorted_dict)[:10]}

    print(top_ten_words)
