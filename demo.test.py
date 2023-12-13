from classes import AddressBook, Record


def demo():
    print("Створення нової адресної книги")
    book = AddressBook()

    print("\nСтворення та додавання запису для John")
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)

    print("\nСтворення та додавання запису для Jane")
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    print("\nВиведення всіх записів у книзі:")
    for name, record in book.data.items():
        print(record)

    print("\nЗнаходження та редагування телефону для John")
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    print(john)

    print("\nПошук конкретного телефону у записі John")
    found_phone = john.find_phone("5555555555")
    print(f"{john.name.value}: {found_phone}")

    print("\nВидалення запису Jane")
    book.delete("Jane")

    print("\nВиведення всіх записів у книзі після видалення Jane:")
    for name, record in book.data.items():
        print(record)


if __name__ == "__main__":
    demo()
