from classes import AddressBook, Record


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"\033[91mError: {e}\033[0m"
        except IndexError:
            return "\033[91mInvalid number of arguments.\033[0m"
        except KeyError:
            return "\033[91mContact not found.\033[0m"
        except Exception as e:
            return f"\033[91mUnexpected error: {e}\033[0m"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book):
    if len(args) != 2:
        raise IndexError
    name, phone = args
    new_record = Record(name)
    new_record.add_phone(phone)
    book.add_record(new_record)
    return "\033[92mContact added.\033[0m"


@input_error
def add_birthday(args, book):
    if len(args) != 2:
        raise IndexError("Two arguments required: name and birthday")
    name, birthday = args
    record = book.find(name)
    if record is None:
        raise KeyError(f"Contact '{name}' not found")
    record.add_birthday(birthday)
    return f"\033[92mBirthday added for {name}.\033[0m"


@input_error
def change_contact(args, book):
    if len(args) != 2:
        raise IndexError
    name, new_phone = args
    record = book.find(name)
    if record is None:
        raise KeyError
    record.edit_phone(record.phones[0].value, new_phone)
    return "\033[92mContact updated.\033[0m"


@input_error
def show_phone(args, book):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError
    return f"\033[94m{name}'s phone number is {record.phones[0].value}\033[0m"


def show_birthday(args, book):
    if len(args) != 1:
        raise IndexError("One argument required: name")
    name = args[0]
    record = book.find(name)
    if record is None:
        return "\033[91mContact not found.\033[0m"
    elif record.birthday is None:
        return "\033[93mNo birthday information available for this contact.\033[0m"
    return f"\033[94m{name}'s birthday is on {record.birthday.value}\033[0m"


@input_error
def show_birthdays_this_week(book):
    birthdays = book.get_birthdays_per_week()
    if not birthdays:
        return "\033[93mNo birthdays in the upcoming week.\033[0m"
    birthday_info = []
    for day, names in birthdays.items():
        birthday_info.append(f"\033[94m{day}: \033[92m{', '.join(names)}\033[0m")
    return "\n".join(birthday_info)


def show_all(book):
    if not book:
        return "\033[93mNo contacts saved.\033[0m"
    return "\n".join(
        [
            f"\033[94m{record.name.value}: {', '.join(phone.value for phone in record.phones)}\033[0m"
            for record in book.data.values()
        ]
    )


def show_help():
    help_text = """
    \033[1mAvailable commands:\033[0m
    - \033[94mhello\033[0m: Greet the bot.
    - \033[92madd [name] [phone number]\033[0m: Add a new contact.
    - \033[92mchange [name] [new phone number]\033[0m: Change an existing contact's phone number.
    - \033[93mphone [name]\033[0m: Retrieve the phone number of a contact.
    - \033[93madd-birthday [name] [birthday]\033[0m: Add a birthday to a contact.
    - \033[93mshow-birthday [name]\033[0m: Show the birthday of a contact.
    - \033[93mbirthdays\033[0m: Show upcoming birthdays within the next week.
    - \033[93mall\033[0m: Show all saved contacts.
    - \033[95mhelp\033[0m: Show this help message.
    - \033[91mclose/exit\033[0m: Exit the program.
    """
    return help_text


def main():
    try:
        book = AddressBook.load_from_file("addressbook.data")
    except Exception as e:
        print(f"Error loading address book: {e}")
        book = AddressBook()

    print("\033[96mWelcome to the assistant bot!\033[0m")

    while True:
        user_input = input("\033[95mEnter a command: \033[0m")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("\033[91mGood bye!\033[0m")
            book.save_to_file("addressbook.data")
            break
        elif command == "hello":
            print("\033[94mHow can I help you?\033[0m")
        elif command == "help":
            print(show_help())
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(show_birthdays_this_week(book))
        else:
            print("\033[91mInvalid command.\033[0m")


if __name__ == "__main__":
    main()
