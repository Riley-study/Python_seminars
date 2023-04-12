import view
import model
import text_fields as txt

def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                view.print_info(txt.pb_open)
                model.load_file()
            case 2:
                model.save_book()
                view.print_info(txt.safe_book_successful)
            case 3:
                view.show_all_contacts(model.get_phone_book(), view.print_info(txt.pb_not_found))
            case 4:
                contact = view.new_contact()
                model.add_new_contact(contact)
                view.print_info(txt.contact_added)
            case 5:
                find_word = view.find_contact_from_user()
                result_request = model.find_contact(find_word)
                view.show_all_contacts(result_request, txt.pb_not_found)
            case 6:
                book = model.get_phone_book()
                view.show_all_contacts(book, view.print_info(txt.pb_not_found))
                changed_contact = view.change_contact(book, txt.index_to_change)
                model.change_contact(changed_contact)
                view.print_info(txt.successful_change)
            case 7:
                book = model.get_phone_book()
                view.show_all_contacts(book, view.print_info(txt.pb_not_found))
                index = view.input_index(book, txt.index_to_del)
                if view.confirm_del(txt.confirm_to_delete):
                    model.del_contact(index)
                    view.print_info(txt.successful_delete_contact)
            case 8:
                if model.exit_book():
                    if model.confirm(txt.confirm_massage):
                        model.save_book()
                        view.print_info(txt.safe_book_successful)
                view.print_info(txt.goodbye_message)
                exit()

