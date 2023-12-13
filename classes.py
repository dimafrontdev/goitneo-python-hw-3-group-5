from collections import UserDict, defaultdict
import datetime
import pickle


class Field:
    # Базовий клас для зберігання даних поля.
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # Клас для зберігання імені контакту.
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    # Клас для номера телефону з перевіркою на 10 цифр.
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain 10 digits")
        super().__init__(value)


class Birthday(Field):
    # Клас для зберігання інформації про день народження
    def __init__(self, birthday):
        if not self.is_valid_birthday(birthday):
            raise ValueError("Invalid birthday format. Use DD.MM.YYYY")
        super().__init__(birthday)

    @staticmethod
    def is_valid_birthday(birthday):
        try:
            datetime.datetime.strptime(birthday, "%d.%m.%Y")
            return True
        except ValueError:
            return False


class Record:
    # Клас для зберігання інформації про контакт (ім'я та телефони)
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    # Методи для додавання, редагування, видалення та пошуку телефонів.

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if str(self.phones[i]) == old_phone:
                self.phones[i] = Phone(new_phone)

    def remove_phone(self, del_phone):
        for i, p in enumerate(self.phones):
            if str(self.phones[i]) == del_phone:
                phone = self.phones[i]
                self.phones.remove(phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p

    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones)
        return f"\033[94mContact name: \033[92m{self.name.value}, \033[94mphones: \033[92m{phones_str}\033[0m"


class AddressBook(UserDict):
    # Клас для управління адресною книгою (додавання, пошук, видалення записів).
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_birthdays_per_week(self):
        today = datetime.date.today()
        one_week_later = today + datetime.timedelta(days=7)
        birthdays_this_week = defaultdict(list)

        for name, record in self.data.items():
            if record.birthday:
                try:
                    # Перетворення рядка дати народження в об'єкт datetime
                    birthday_date = datetime.datetime.strptime(
                        record.birthday.value, "%d.%m.%Y"
                    ).date()
                    # Налаштування на поточний або наступний рік
                    birthday_this_year = birthday_date.replace(year=today.year)
                    if birthday_this_year < today:
                        birthday_this_year = birthday_this_year.replace(
                            year=today.year + 1
                        )

                    # Перевірка, чи день народження припадає на наступний тиждень
                    if today <= birthday_this_year < one_week_later:
                        day_of_week = birthday_this_year.strftime("%A")
                        birthdays_this_week[day_of_week].append(name)
                except ValueError:
                    # Обробка помилок невірного формату дати народження
                    print(
                        f"Invalid birthday format for {name}. Please use DD.MM.YYYY format."
                    )

        return dict(birthdays_this_week)

    # Метод для зберігання даних у файлі
    def save_to_file(self, file_name):
        with open(file_name, "wb") as file:
            pickle.dump(self.data, file)

    # Метод для читання даних з файлу
    @classmethod
    def load_from_file(cls, file_name):
        try:
            with open(file_name, "rb") as file:
                data = pickle.load(file)
                address_book = cls()
                address_book.data = data
                return address_book
        except FileNotFoundError:
            return cls()
