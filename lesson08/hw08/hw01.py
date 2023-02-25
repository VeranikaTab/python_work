# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

import os
import shutil 

from os import path  

file_base = "base.txt"
all_data = []
id = 0


if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

def read_records():  # чтение записи
    global all_data, id

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            id = int(all_data[-1][0])

        return all_data
 
def show_all(): 
    if not all_data:
        print("Empty data")
    else:
        print(*all_data, sep="\n") 

def adding ():
    global all_data, id
    add_id = int(id)
    with open(file_base, "a", encoding="utf-8") as f:
        first_name = input("Write first name: ").upper()
        last_name = input("Write last name: ").upper()
        new_phone = input("Write phone number: ")
        f.write(f"{add_id} {first_name} {last_name}  {new_phone}\n")
        add_id = int(id) + 1
    return print("Added information")

def add_new():
    flag = True
    while flag:
        answer = input("Press:\n"
                        "1 - Add another post? \n"
                        "2 - Back to menu \n")
        match answer:
            case "1":
                adding()
            case "2":
                flag = False
            case _:
                print("Try again!\n")

def search_by_name(string):
    global all_data
    count = 0
    result = []
    for i in all_data:
        if string in i:
            result.append(count)
        count += 1
    return result

def search_record():
    os.system('CLS')
    want_find = input("Enter data to search: ").upper()
    list_find = search_by_name(want_find)
    if list_find == []:
        print("Data not found!")
    else:
        print(*[all_data[i] for i in list_find], sep='\n')

def changing(num):
    new_first_name = input("Write new first name: ").upper()
    new_last_name = input("Write new last name: ").upper()
    new_phone = input("Write new phone number: ")
    changed_line = num+" "+new_first_name+" "+new_last_name+" "+new_phone
    return changed_line

def change_record():
    show_all()
    global id
    answer = input(f"Specify the line number to make changes? \n"
        "1 - Yes\n"
        "2 - No\n")
    match answer:
        case "1":
            line_to_change = input("Enter the line number: ")
        case "2":
            line_to_change = search_record()
            if len(line_to_change) > 1:
                line_to_change = input("Number is not correct: ")
            elif len(line_to_change) == 0:
                print("Not found!")
    new_string = changing(line_to_change)

    all_data[int(line_to_change)] = new_string
    with open(file_base, 'w', encoding="utf-8") as f:
        for i in all_data:
            f.write(i + "\n")

    print("change!")

def delete_record():
    print("ALL PHONE BOOK")
    show_all()
    result_str = ""
    num_line = input("Which line do you want to delete? ")
    with open(file_base, encoding="utf-8") as f:
        lines = f.readlines()
    with open(file_base, 'w', encoding="utf-8") as f:
        for line in lines:
            if line[0] != num_line:
                result_str += line
        f.write(result_str)
        print("delete!")

def export_file():
    new_file_name = input("Enter the name of creating file: ")
    if path.exists(new_file_name):
        print("File exixts!")
    else:
        shutil.copyfile(file_base, new_file_name)
        print("export!")

def import_file():
    importing_file = input("Enter the name of importing file: ")
    if not path.exists(importing_file):
        print("File not exixts!")
    else:
        file_base = importing_file
        print("Done!")
    
def main_menu():                                   
    play = True      
    while play:
        read_records()
        answer = input("Phone book: \n"
                        "1. Show all records.\n"   
                        "2. Add a new record.\n"
                        "3. Search a record.\n"
                        "4. Change a record.\n" 
                        "5. Delete a record.\n" 
                        "6. Import the file.\n"
                        "7. Export the file.\n" 
                        "8. Exit.\n" ) 
                                                                                         
        match answer:
            case "1":
                show_all()
            case "2":
                add_new()
            case "3":
                search_record()
            case "4":
                change_record()  
            case "5":
                delete_record()
            case "6":
                import_file()
            case "7":
                export_file()
            case "8":
                play = False
            case _:                          
                print("Try again!\n")
main_menu()
