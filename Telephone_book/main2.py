import readfile

# if __name__ == "__main2.py__":
print("Menu: ")
print("1. Показать всю телефонную книгу: ")
print("2. Добавить новую запись: ")
print("3. Редактировать существующую запись: ")
print("4. Поиск контакта: ")

user_choice = int(input("Введите номер пункта меню: "))
if user_choice == 1:
    readfile.show_all(user_choice)

