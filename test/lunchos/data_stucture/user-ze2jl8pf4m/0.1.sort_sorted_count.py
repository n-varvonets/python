print(" ----   1. Посчитать количество вхождений букв в слово ---- ")
first = "строка уже задана".count("а")
sec = sum(1 for i in "строка уже задана" if i == "а")
print(first, sec)
print(" ----   2. sort() vs list.sorted  ---- ")
# 2.1.встроенная функцию в пайтоне sort() сортирует список на месте, изменяя его индексы и возвращая None,
# тогда как sorted () - встроенный метод списка и возвращает новый отсортированный список, оставляя исходный список неизменным.
array_nums = [2, 3, 1, 5, 6, 4, 0]

print(sorted(array_nums))   # [0, 1, 2, 3, 4, 5, 6]
print(array_nums)           # [2, 3, 1, 5, 6, 4, 0]

print(array_nums.sort())    # None
print(array_nums)           # [0, 1, 2, 3, 4, 5, 6]

# 2.2. Другое отличие состоит в том, что sorted() принимает любые итерации,
# в то время как list.sort () является методом класса списка и может использоваться только со списками

my_string_as_array = "my_string_as_array"
my_tuple = (1, 2, 6, -3)

print(sorted(my_string_as_array))  # ['_', '_', '_', 'a', 'a', 'a', 'g', 'i', 'm', 'n', 'r', 'r', 'r', 's', 's', 't', 'y', 'y']
print(my_string_as_array)  # my_string_as_array

print(sorted(my_tuple))  # [-3, 1, 2, 6]
print(my_tuple)  # (1, 2, 6, -3)

# в то время как метод обьекта типа list - вьідаст ошибку
# print(my_string_as_array.sort())
# print(my_tuple.sort())
