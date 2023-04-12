phone_book = []
phone_book_start = []
PATH = 'tel_book.txt'


def get_phone_book():
    global phone_book
    return phone_book


# открываем файл для чтения, проходимся по строкам и формируем список словарей, где каждый словарь - контакт
def load_file():
    global phone_book, phone_book_start
    phone_book.clear()
    with open('tel_book.txt', 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(";")
        phone_book.append({"name": contact[0], "phone": contact[1], "comment": contact[2]})
    phone_book_start = phone_book.copy()


def add_new_contact(contact: dict):
    global phone_book
    phone_book.append(contact)


def save_book():
    global phone_book
    data = []
    for contact in phone_book:
        data.append(';'.join([value for value in contact.values()]))
    data = '\n'.join(data)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(data)


def exit_book() -> bool:
    global phone_book, phone_book_start
    if phone_book == phone_book_start:
        return False
    else:
        return True


def confirm(massage) -> bool:
    answer = input(massage + ' (y/n?)')
    if answer.lower() == 'y':
        return True
    else:
        return False

def find_contact(user_request: str) -> list[dict]:
    global phone_book
    result = []
    for contact in phone_book:
        for item in contact.values():
            if user_request in item:
                result.append(contact)
                break
    return result


def change_contact(contact: tuple[int, dict]) -> None:
    index, contact = contact
    original_contact = phone_book.pop(index-1)
    # в новый контакт положим ключ 'name' если он есть, если его нет, оставляет тот, который был изначально
    contact = {'name': contact.get('name') if contact.get('name') else original_contact.get('name'),
               'phone': contact.get('phone') if contact.get('phone') else original_contact.get('phone'),
               'comment': contact.get('comment') if contact.get('comment') else original_contact.get('comment')}
    phone_book.insert(index-1, contact)


def del_contact(index: int) -> str:
    deleted_contact = phone_book.pop(index-1)
    return deleted_contact.get('name')

