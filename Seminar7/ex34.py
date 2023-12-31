# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке

def check_rhythm(poem):
    phrases = poem.split()

    syllables = list(map(count_syllables, map(lambda x: x.split('-'), phrases)))

    if len(set(syllables)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"

def count_syllables(words):
    vowels = 'аеёиоуыэюя'
    return sum(1 for word in words for letter in word if letter.lower() in vowels)

poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)
