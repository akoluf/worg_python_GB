# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке
# sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

import pandas as pd

# Шаг 1: Чтение файла
df = pd.read_csv('sample_data/california_housing_train.csv')

# Шаг 2: Выведение названий столбцов
column_names = df.columns
print("Названия столбцов:", column_names)

# Шаг 3: Определение средней стоимости дома с количеством людей от 0 до 500
average_house_value = df[(df['population'] >= 0) & (df['population'] <= 500)]['median_house_value'].mean()
print("Средняя стоимость дома с количеством людей от 0 до 500:", average_house_value)
