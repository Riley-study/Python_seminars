import view_in_class
import classes
import text_fields_in_class as txt


def start():
    book = classes.PhoneBook('tel_book_in_class.txt')
    book.load()
    view_in_class.print_info(txt.pb_open)
    while True:
        choice = view_in_class.main_menu()
        match choice:
            case 1:  #
                find_word = view_in_class.find_contact_from_user()
                result_request = book.find(find_word)
                view_in_class.show_all_contacts(result_request, view_in_class.print_info(txt.pb_not_found))
            case 2:  #
                pb = book.get()
                view_in_class.show_all_contacts(pb, txt.massage_tel_book)
            case 3:  #
                contact = view_in_class.new_contact()
                book.add(contact)
                view_in_class.print_info(txt.contact_added)
            case 4:  #
                book.save()
                view_in_class.print_info(txt.safe_book_successful)
            case 5:
                pb = book.get()
                view_in_class.show_all_contacts(pb, view_in_class.print_info(txt.massage_tel_book))
                changed_contact = view_in_class.change_contact(pb, txt.index_to_change)
                book.change_contact(changed_contact)
                view_in_class.print_info(txt.successful_change)
            case 6:  #
                pb = book.get()
                view_in_class.show_all_contacts(pb, view_in_class.print_info(txt.massage_tel_book))
                index = view_in_class.input_index(pb, txt.index_to_del)
                if view_in_class.confirm_del(txt.confirm_to_delete):
                    book.del_contact(index)
                    view_in_class.print_info(txt.successful_delete_contact)
            case 7:  #
                if book.exit():
                    if view_in_class.confirm(txt.confirm_massage):
                        book.save()
                        view_in_class.print_info(txt.safe_book_successful)
                else:
                    view_in_class.print_info(txt.goodbye_message)
                exit()
