import readfile
#if __name__ == "__main2.py__":
readfile.all_menu()

start = True
while start == True:
    user_choice = input("\nВведите номер пункта меню либо 0 для повторного вызова меню: ")
    if user_choice == '1':
        readfile.show_all()
    elif user_choice == '2':
        readfile.add_contact()
    elif user_choice == '3':
        readfile.delete_contact()
    elif user_choice == '4':
        readfile.change_contact()
    elif user_choice == '5':
        readfile.find_contact()
    elif user_choice == '0':
        readfile.all_menu()
    elif user_choice == '6':
        start = False
        readfile.exit_message()
        break
    else:
        print("Что-то пошло не так, попробуйте еще раз ")
