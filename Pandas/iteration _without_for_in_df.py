import pandas as pd

# Task: Преобразовываем DataFrame в одномерный массив и получаем уникальные значения без использования цикла for
data = {
    'A': [1, 2, 2, 3, 4, 4, 5],
    'B': ['a', 'b', 'b', 'c', 'c', 'd', 'e']
}

df = pd.DataFrame(data)


"""---------------V1-------------  via flattern """
unique_values = set(df.values.flatten().tolist())
print(f"Уникальные значения массива V1:\n{unique_values}")

"""---------------V2-------------  via apply() """
# Получаем уникальные значения для каждого столбца без использования цикла for
unique_values_2 = df.apply(lambda x: x.unique())
print(f"Уникальные значения массива V2:\n{unique_values_2}")


"""пример использования flatten() для преобразования матрицы в одномерный массив"""
# matrix = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# flattened_array = set(df.values.flatten().tolist())
# print(flattened_array)  # >>> [1 2 3 4 5 6 7 8 9]

