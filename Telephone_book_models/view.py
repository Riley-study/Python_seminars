import text_fields as txt


def main_menu() -> int:
    print('''\n Главное меню:
    1. Найти контакт
    2. Показать все контакты
    3. Создать контакт
    4. Сохранить файл
    5. Изменить контакт
    6. Удалить контакт
    7. Выход''')
    while True:
        choice = input("Выберите пункт меню:")
        if choice.isdigit() and 0 < int(choice) < 8:
            return int(choice)
        else:
            print("Введите число от 1 до 7")


def print_info(message: str):
    print('\n' + '>'*len(message))
    print(message)
    print('<'*len(message) + '\n')


# если список не пустой, формируется тел книга, если пустой, выводим сообщение
def show_all_contacts(book: list[dict], message: str):
    if book:
        print('\n' + '=' * 90)
        for n, contact in enumerate(book, 1):
            print(f'{n}. {contact.get("name"):<30}'
                  f'{contact.get("phone"):<20}'
                  f'{contact.get("comment"):<40}')
        print('=' * 90 + '\n')
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
