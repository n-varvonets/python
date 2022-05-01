def concat_sequence_v1(s1, s2):
    """
    Скленивание двух последовательностей.
    """
    print('here')
    for elem in s1:
        print('--1--')
        yield elem
    for elem in s2:
        print('--5--')
        yield elem
        print('--6--')


def concat_sequence_v2(s1, s2):
    """
    Аналогично примеру concat_sequence_v1- склеиваем две последовательности,
    но уже с использованием yield from, что позволит нам не запускать цикла.
    """
    print('--2--')
    yield from s1
    print('--3--')
    yield from s2
    print('--4--')


seq1 = range(10)
seq2 = range(10, 20)
result = concat_sequence_v1(seq1, seq2)  #  в генератор передали
#пока генератор не отраотает - дальше не пойдем



print(result, "\n", list(result))
print('Seq 1')
cnt = 1
for i in result:
    print(f'{cnt}--tut--')
    print(i)

seq1 = range(10)
seq2 = range(10, 20)
result = concat_sequence_v2(seq1, seq2)

print('Seq 2')
for i in result:
    print(i)
