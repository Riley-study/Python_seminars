class Contact:
    def __init__(self, name: str, phone: str, comment: str = ''):
        self.name = name
        self.phone = phone
        self.comment = comment

    def __str__(self) -> str:
        return f'{self.name: <30} {self.phone: <20} {self.comment: <30}'

    def contact_to_str(self):
        return f'{self.name}; {self.phone}; {self.comment}'

    def change(self, name: str, phone: str, comment: str = ''):
        self.name = name if name else self.name
        self.phone = phone if phone else self.phone
        self.comment = comment if comment else self.comment


class PhoneBook:
    def __init__(self, path: str):
        self.path = path
        self.phone_book: list[Contact] = []
        self.original_book: list[Contact] = []
        self.is_change = False

    def load(self):  # открывает тел книгу
        self.phone_book.clear()
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for contact in data:
            contact = contact.strip().split(';')
            self.phone_book.append(Contact(contact[0], contact[1], contact[2]))

    def save(self):  # сохраняет книгу
        data = []
        for contact in self.phone_book:
            data.append(contact.contact_to_str())
        data = '\n'.join(data)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)
        self.is_change = False

    def get(self):  # присваивает тел книгу
        return self.phone_book

    def add(self, contact: Contact):  # добавляет контакт в конец книги
        self.phone_book.append(contact)
        self.is_change = True

    def exit(self) -> bool:  # закрывает книгу и проверяет, чтобы изменения были сохранены
        return self.is_change

    def find(self, user_request: str) -> list[Contact]:  # ищет контакты по введенному слову
        result = []
        for contact in self.phone_book:
            if user_request in contact.contact_to_str():
                result.append(contact)
        return result

    def change_contact(self, contact: tuple[int, Contact]) -> None:  # меняет контакт
        index, new = contact
        self.phone_book[index-1].change(new.name, new.phone, new.comment)
        self.is_change = False

    def del_contact(self, index: int) -> str:  # удаляет контакт
        deleted_contact = self.phone_book.pop(index - 1)
        self.is_change = False
        return deleted_contact.name
