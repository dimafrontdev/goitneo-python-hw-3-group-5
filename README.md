# goitneo-python-hw-3-group-5

## Overview

This project implements an advanced console-based assistant bot featuring an enhanced data management system through custom classes and improved error handling. The assistant supports various functionalities, including contact management and birthday reminders.

## Features

- **Advanced Error Handling**: Utilizes the `input_error` decorator for robust error management across different commands.
- **Enhanced Data Management**: Introduces classes like `AddressBook` and `Record` for efficient contact management.
- **Birthday Management**: Ability to add, store, and display contact birthdays.
- **Contact Management**: Add, change, find, and delete contact information with ease.
- **Persistence**: Save and restore address book data from disk using serialization, ensuring data is not lost between sessions.

## Getting Started

To interact with the assistant, run the `main.py` file. The assistant supports a range of commands to manage contacts and their information:

- `add [name] [phone number]`: Add a new contact with a name and phone number.
- `change [name] [new phone number]`: Change an existing contact's phone number.
- `phone [name]`: Retrieve the phone number of a contact.
- `all`: Display all saved contacts.
- `add-birthday [name] [birthday]`: Add a birthday for a specified contact.
- `show-birthday [name]`: Show the birthday of a specified contact.
- `birthdays`: Show birthdays occurring in the upcoming week.
- `hello`: Greet the bot.
- `close` or `exit`: Exit the application.

To see a demonstration of these functionalities, run the `demo.test.py` script.

## Testing

Run `demo.test.py` to execute a series of automated actions demonstrating the bot's capabilities. This includes creating contacts, adding phone numbers, managing birthdays, and showcasing persistence features.

## Additional Notes

- The project's error handling system ensures a user-friendly experience, gracefully managing incorrect inputs and providing clear instructions.
- Data validation includes checks for correct phone number formats and valid date inputs for birthdays.
- The application saves data to disk upon exit and retrieves it upon startup, ensuring data persistence.
