# Задача 2. Найдите сумму цифр трехзначного числа.

n = int(input("Введите трехзначное число: "))

res = n // 100 + (n // 10) % 10 + n % 10

print("Сумма цифр трехзначного числа:", res)