# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит
# число А в целую степень B с помощью рекурсии.

def power(a, b):
    if b == 0:
        return 1
    elif b > 0:
        return a * power(a, b-1)
    else:
        return 1 / power(a, -b)

A = float(input("Введите число A: "))
B = int(input("Введите число B: "))

result = power(A, B)
print("A в степени B =", result)
