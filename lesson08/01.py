# Задача №49. Решение в группах
# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные,
# которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. 
# Ваша программа не должна быть линейной

from os import path  # модуль os с множеством функций os.path вложенный

file_base = "base.txt"
all_data = []
id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

def read_records():  # чтение записи
    global all_data, id

    with open(file_base) as f:
        all_data = [i.strip() for i in f]
        if all_data:
            id = int(all_data[-1][0])

        return all_data

def show_all():  #показать все
    if not all_data:
        print("Empty data")  # Пустые данные
    else:
        print(*all_data, sep="\n")

def add_new_contact():  # добавить новый контакт
    global id
    array = ['surname','name','surname_2','phone_number']  # 'фамилия','имя','отчество','номер телефона'
    string = ''
    for  i in array:
        string += input(f"enter {i} ") + " "
    id += 1
    # print(f'{id} {string}')

    with open(file_base, 'a', encoding="utf-8") as f:
        f.write(f'{id} {string}\n')

# add_new_contact()

def main_menu():  # главное меню
    play = True
    while play:
        read_records()                  # чтение записи
        answer = input("Phone book:\n"     # Tелефонная книга
                       "1. Show all records\n"     #показать все
                       "2. Add a record\n"      # Добавить запись
                       "3. Search a record\n"    # Поиск записи
                       "4. Delete\n"       # Удалить
                       "5. Exit\n")         # Выход
        match answer:
            case "1":
                show_all()  #показать все
            case "2":
                add_new_contact()  # добавить новый контакт
            case "3":
                pass
            case "4":
                pass
            case "5":
                play = False
            case _:
                print("Try again!\n")


main_menu()

