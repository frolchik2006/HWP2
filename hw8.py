# Task 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и 
# Вы должны реализовать функционал для изменения и удаления данных

def print_menu():
    print("""
    ***************************** \n
    1 - Все контакты  
    2 - Поиск контакта
    3 - Добавить контакт 
    4 - Изменить данные контакта 
    5 - Удалить контакт 
    6 - Выход  
    ***************************** \n 
    """)

def addition():
    with open(file_path, 'a', encoding='utf8') as open_book:
        add_f = (input('Введите фамилию: ' ).title())
        add_i = (input('Введите имя: ' ).title())
        add_tel = (input('Введите телефон: ' ).title())
        new_line = add_f +' '+add_i +' '+ add_tel 
        open_book.writelines(f'\n{new_line}')
        print(new_line)

def search():
    with open(file_path, 'r', encoding='utf8') as open_book:
        seach_param = (input('Введите параметр для поиска: ' ).title())
        for line in open_book:
            if seach_param in line:
                print(line)

def remove_contact():
    with open(file_path, 'r', encoding="utf-8") as open_book:
        X = input('Введите Имя или Фамилию для удаления: ')
        lines = open_book.readlines()
        with open(file_path, 'w', encoding="utf-8") as open_book:
            for line in lines:
                if X in line:
                    print("Строка удалена")
                else:
                    print(line)    
                    open_book.write(line)


def edit():
    with open(file_path, 'r', encoding="utf-8") as open_book:
        seach_param = (input('Введите параметр для поиска: ' ).title())
        with open (file_path, 'w', encoding='utf8') as open_book:
            for line in seach_param:
                if seach_param in line:
                    print(line)
                    add_f = (input('Введите фамилию: ' ).title())
                    add_i = (input('Введите имя: ' ).title())
                    add_tel = (input('Введите телефон: ' ).title())
                    new_line = add_f +' '+add_i +' '+ add_tel + '\n'
                    line = line.replace(line, new_line)
                open_book.writelines(line)

def read_all():
    with open(file_path, 'r', encoding='utf8') as open_book:
        print()
        for line in open_book:
            print(line)  



def tasks(task):
   if task > 6: print('Ошибка')
   if task == 6: print('До скорых встреч!')
   else:
    match task:
        case 1: # вывести все контакты
            read_all()
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))   
        case 2: # поиск контактов
            search()
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))
        case 3: # добавить контакт
            addition()
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))
        case 4: # изменить контакт
            edit()
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))
        case 5: # удалить контакт
            remove_contact()
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))            

file_path = 'phone_book.txt'
print_menu()
tasks(int(input('Введите номер задачи от 1 до 6: ')))