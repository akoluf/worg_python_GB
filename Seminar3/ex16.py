# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

# Запрашиваем у пользователя число N
N = int(input("Введите число N от 1 до 100 : "))

# Генерируем случайный массив A[1..N]
A = [random.randint(1, 100) for _ in range(N)]

# Выводим первоначальный массив
print("Первоначальный массив A:", A)

# Запрашиваем у пользователя искомое число
X = int(input("Введите искомое число X: "))

# Вычисляем, сколько раз искомое число X встречается в массиве
count = A.count(X)

# Выводим результат
print("Число", X, "встречается в массиве", count, "раз(а)")
