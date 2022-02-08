a = [5, 6, 7, 8]
b = [100, 200, 300, 40]

for i in range(4):
    print(a[i], b[i])

# тоже самое делает zip функция... только уже в данном случае если эелемент выйдет за пределы,
# то не будет ошибку как при цикле for

lst_with_3_vals = [100,200,300]
for vals in zip(a, lst_with_3_vals, a):
    print({"first_row": vals[0], "second_row": vals[1], "third_row": vals[2]})
