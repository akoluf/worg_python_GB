# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
# из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
# get_dummies?
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

import pandas as pd
import random

# Генерируем исходные данные
random.seed(0)
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем словарь для кодирования категорий
categories = list(set(data['whoAmI']))
categories_dict = {category: [int(category == value) for value in categories] for category in categories}

# Создаем one-hot кодировку для столбца 'whoAmI'
one_hot_data = pd.DataFrame([categories_dict[value] for value in data['whoAmI']], columns=categories)

# Объединяем исходный DataFrame с полученным one-hot представлением
data = pd.concat([data, one_hot_data], axis=1)

data.head()
print(data.head)
