# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

ticket_number = input("Введите номер билета (6 цифр): ")

if len(ticket_number) != 6:  # проверка на длину номера билета
    print("Номер билета должен состоять из 6 цифр.")
else:
    digit1 = int(ticket_number[0])
    digit2 = int(ticket_number[1])
    digit3 = int(ticket_number[2])
    digit4 = int(ticket_number[3])
    digit5 = int(ticket_number[4])
    digit6 = int(ticket_number[5])

    sum1 = digit1 + digit2 + digit3
    sum2 = digit4 + digit5 + digit6

    if sum1 == sum2:
        print("Поздравляем, вам попался счастливый билет!")
    else:
        print("Увы, билет не счастливый.")