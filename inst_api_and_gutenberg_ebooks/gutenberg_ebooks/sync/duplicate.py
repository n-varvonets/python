some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

from collections import defaultdict

word_dict = defaultdict(lambda: 0)
for word in some_list:
    word_dict[word] +=1

print(word_dict)