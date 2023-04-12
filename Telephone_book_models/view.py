import text_fields as txt


def main_menu() -> int:
    print('''\n Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход''')
    choice = ''
    while True:
        choice = input("Выберите пункт меню:")
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        else:
            print("Введите число от 1 до 8")


def print_info(message: str):
    print('\n' + '-'*len(message))
    print(message)
    print('-'*len(message) + '\n')


# если список не пустой, формируется тел книга, если пустой, выводим сообщение
def show_all_contacts(book: list[dict], message: str):
    if book:
        print('\n' + '-' * 90)
        for n, contact in enumerate(book, 1):
            print(f'{n}. {contact.get("name"):<30}'
                  f'{contact.get("phone"):<20}'
                  f'{contact.get("comment"):<40}')
        print('-' * 90 + '\n')
    else:
        print(message)


# создаем словарик из запросов от пользователя (новый контакт)
def new_contact() -> dict:
    name = input(txt.new_name)
    phone = input(txt.new_phone)
    comment = input(txt.new_comment)
    return {"name":  name, "phone":  phone, "comment":  comment}


def find_contact_from_user() -> str:
    find_element = input(txt.find_elnt)
    return find_element


def change_contact(book: list, message: str) -> tuple[int, dict[str, str]]:
    index = 0
    while True:
        choice = input(message)
        if choice.isdigit() and 0 < int(choice) < len(book)+1:
            index = int(choice)
            break
    # print(txt.enter_or_empty)
    contact = new_contact()
    return index, contact


def input_index(book: list, message: str) -> int:
    while True:
        choice = input(message)
        if choice.isdigit() and 0 < int(choice) < len(book)+1:
            return int(choice)


def confirm_del(message: str):
    answer = input(message + ' y/n ? ')
    if answer.lower() == 'y':
        return True
    else:
        return False

