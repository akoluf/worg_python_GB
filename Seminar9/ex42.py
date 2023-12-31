# Задача 42: Узнать какая максимальная households в зоне минимального значения population

import pandas as pd

# Шаг 1: Чтение файла
df = pd.read_csv('/media/iht/Хранилище/GB/DZ_python_GB/Seminar9/sample_data/california_housing_train.csv')

# Шаг 2: Нахождение минимального значения переменной "population"
min_population = df['population'].min()

# Шаг 3: Выборка данных, где переменная "population" равна минимальному значению
subset = df[df['population'] == min_population]

# Шаг 4: Нахождение максимального значения переменной "households" в этом подмножестве данных
max_households_in_min_population = subset['households'].max()
print("Ответ:", max_households_in_min_population)
