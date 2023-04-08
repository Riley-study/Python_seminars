
def menu():
    input("Введите номер пункта меню либо 0 для повторного вызова меню: ")


def all_menu():
    print("Menu: ")
    print("1. Показать всю телефонную книгу: ")
    print("2. Добавить новую запись: \n3. Удалить запись")
    print("4. Редактировать существующую запись: ")
    print("5. Поиск контакта: \n6. Выход")


def show_all():
    file = open('sample1.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    print("1. Вся телефонная книга: ")
    for item in data:
        print(*item.split(';'))
    file.close()


def add_contact():
    file = open('sample1.txt', 'a', encoding='UTF-8')
    new_contact = input("2. Добавить новую запись. Введите имя, номер телефона и комментарий через ';' :")
    file.write(f'\n{new_contact}')
    file.close()


def delete_contact():  # через резервную копию справочника
    file = open('sample1.txt', 'r', encoding='UTF-8')
    file_res = open('sample_reserve.txt', 'w+', encoding='UTF-8')
    find_str = input("3. Удалить контакт. Введите имя контакта: ")
    data = file.readlines()
    for line in data:
        if find_str in line:
            print(line)
    confirm_msg = input("Удалить этот контакт? (да/нет): ")   # подтверждение, если нашел не то контакт или несколько
    if confirm_msg == "да":
        for line in data:
            if find_str not in line:
                file_res.write(line)
        print("Контакт удален")
    else:
        for line in data:
            file_res.write(line)
    file.close()
    file_res.close()
# восстанавливаем из резервной копии
    file = open('sample1.txt', 'w', encoding='UTF-8')
    file_res = open('sample_reserve.txt', 'r', encoding='UTF-8')
    data_res = file_res.readlines()
    for line in data_res:
        file.write(line)
    file.close()
    file_res.close()


def find_contact():
    file = open('sample1.txt', 'r', encoding='UTF-8')
    find_str = input("5. Поиск контакта. Введите имя: ")
    data = file.readlines()
    for line in data:
        if find_str in line:
            print(line)
    file.close()


def exit_message():
    print("6. Выход. Благодарим за внимание, до новых встреч!")


def change_contact():
    file = open('sample1.txt', 'r+', encoding='UTF-8')
    find_str = input("4. Изменить существующий контакт. Введите имя контакта: ")
    data = file.readlines()
    for line in data:
        if find_str in line:
            print(line)
    confirm_msg = input("Изменить этот контакт? (да/нет): ")  # подтверждение, если нашел не то контакт или несколько
    if confirm_msg == "да":
        new_name = input("4. Введите НОВЫЕ данные через ';' : ")
        for item in data:
            if find_str in item:
                item_to_del = item
                item = item.replace(f'{item}', f'{new_name}')
                print("Контакт изменен")
                file.writelines(f'\n{item}')
    file.close()
