# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.
import os

def create_phonebook():
    with open('phonebook.txt', 'w') as file:
        file.write('')
    print("Телефонный справочник успешно создан.")


def check_phonebook():
    if not os.path.exists('phonebook.txt'):
        create_choice = input("Файл телефонного справочника не найден. Желаете создать новый справочник? (y/n): ")
        if create_choice.lower() == 'y':
            create_phonebook()
        else:
            print("Программа завершена.")
            return True
    elif os.stat('phonebook.txt').st_size == 0:
        fill_choice = input("Телефонный справочник пуст. Желаете заполнить его сейчас? (y/n): ")
        if fill_choice.lower() == 'y':
            return False
        else:
            print("Программа завершена.")
            return True
    else:
        return False


def get_contact_number():
    with open('phonebook.txt', 'r') as file:
        data = file.read().splitlines()
    return len(data) + 1


def add_contact():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    phone_number = input("Введите номер телефона: ")
    description = input("Введите описание: ")
    contact_number = get_contact_number()
    with open('phonebook.txt', 'a') as file:
        file.write(f"{contact_number}--{surname}--{name}--{phone_number}--{description}\n")
    print("Контакт успешно добавлен.")


def display_data():
    with open('phonebook.txt', 'r') as file:
        data = file.read().splitlines()
    if len(data) == 0:
        print("Телефонный справочник пуст.")
    else:
        print('\n{: <10} {: <10} {: <10} {: <15} {: <20}'.format('Номер', 'Фамилия', 'Имя', 'Номер телефона', 'Описание'))
        print('-' * 67)
        for row in data:
            contact = row.split('--')
            print('{: <10} {: <10} {: <10} {: <15} {: <20}'.format(contact[0], contact[1], contact[2], contact[3], contact[4]))
        print()


def search_data(keyword):
    with open('phonebook.txt', 'r') as file:
        data = file.read().splitlines()
    results = []
    for row in data:
        contact = row.split('--')
        if keyword.lower() in contact[1].lower() or keyword.lower() in \
                contact[2].lower() or keyword.lower() in contact[3].lower() or keyword.lower() in contact[4].lower():
            results.append(row)
    if len(results) == 0:
        print("Записей не найдено.")
    else:
        print("Результаты поиска:")
        print('\n{: <10} {: <10} {: <10} {: <15} {: <20}'.format('Номер', 'Фамилия', 'Имя', 'Номер телефона', 'Описание'))
        print('-' * 67)
        for row in results:
            contact = row.split('--')
            print('{: <10} {: <10} {: <10} {: <15} {: <20}'.format(contact[0], contact[1], contact[2], contact[3], contact[4]))
        print()


def update_contact():
    contact_number = input("Введите номер контакта, который хотите изменить: ")
    new_surname = input("Введите новую фамилию (оставьте пустым для пропуска): ")
    new_name = input("Введите новое имя (оставьте пустым для пропуска): ")
    new_phone_number = input("Введите новый номер телефона (оставьте пустым для пропуска): ")
    new_description = input("Введите новое описание (оставьте пустым для пропуска): ")
    with open('phonebook.txt', 'r') as file:
        data = file.readlines()
    found = False
    for i, row in enumerate(data):
        contact = row.split('--')
        if contact_number == contact[0]:
            found = True
            if new_surname:
                contact[1] = new_surname
            if new_name:
                contact[2] = new_name
            if new_phone_number:
                contact[3] = new_phone_number
            if new_description:
                contact[4] = new_description
            data[i] = '--'.join(contact)
            break
    if found:
        with open('phonebook.txt', 'w') as file:
            file.write(''.join(data))
        print("Контакт успешно обновлен.")
    else:
        print("Контакт не найден.")


def delete_contact():
    contact_number = input("Введите номер контакта, который хотите удалить: ")
    with open('phonebook.txt', 'r') as file:
        data = file.read().splitlines()
    results = []
    for i, row in enumerate(data):
        contact = row.split('--')
        if contact_number == contact[0]:
            results.append(i)
    if len(results) == 0:
        print("Контакт не найден.")
    elif len(results) == 1:
        del data[results[0]]
        with open('phonebook.txt', 'w') as file:
            file.write('\n'.join(data))
        print("Контакт успешно удален.")
    else:
        print("Найдено несколько контактов с таким номером. Введите более точные данные.")


def clear_phonebook():
    confirm = input("Вы уверены, что хотите очистить весь телефонный справочник? (y/n): ")
    if confirm.lower() == 'y':
        with open('phonebook.txt', 'w') as file:
            file.write('')
        print("Телефонный справочник очищен.")
    else:
        print("Очистка телефонного справочника отменена.")


def main():
    exit_program = check_phonebook()
    if exit_program:
        return
    while True:
        print("1. Просмотреть данные")
        print("2. Поиск данных")
        print("3. Добавить контакт")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Очистить телефонный справочник")
        print("7. Выйти\n")
        choice = input("Введите номер выбранного действия: ")
        if choice == "1":
            display_data()
        elif choice == "2":
            keyword = input("Введите ключевое слово для поиска: ")
            search_data(keyword)
        elif choice == "3":
            add_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            clear_phonebook()
        elif choice == "7":
            print("Программа завершена.")
            break
        else:
            print("Неправильный выбор. Попробуйте снова.")


main()
