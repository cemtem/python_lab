def print_numbers(phonebook, names):
    if len(phonebook) == 0:
        print('phonebook is empty')
        return
    if len(names) == 0:
        print('Name is not specified')
        return

    print('Name', end='\t')
    print('Phone number', end='\t')
    for name in names:
        print()
        print(name, end='\t')
        print(phonebook[name], end='\t')
    print()


def run():
    print(
        'Welcome!'
        '\nCommands: '
        '\n 1 - Add phone number and name '
        '\n 2 - Display numbers by name '
        '\n 3 - Delete entry from phonebook'
        '\n 0 - quit')
    command = None
    book = {'igor': ['89191919191'], 'ihor': ['22222222', '3333333']}
    while command != 0:
        try:
            command = int(input('Enter command:'))
        except:
            print('Wrong command. Try again')
            command = None

        if command == 1:
            print('Add phone number and name')

            name = input('Name: ')
            phone_numbers = input('Phone numbers separated by blanks: ')
            list_numbers = phone_numbers.split(" ")
            book[name] = list_numbers
            print('Added ' + str(name) + ' with numbers ' + str(list_numbers))
        elif command == 2:
            print('Display numbers by name')

            name = input('Name separated by blank: ').split(" ")
            try:
                print_numbers(book, name)
            except:
                print('There is no ' + str(name) + '\'s in phone book')
        elif command == 3:
            print('Delete person')

            name = input('Name: ')
            try:
                del book[name]
                print(str(name) + ' deleted')
            except:
                print('There is no ' + str(name) + '\'s in the phone book')
        elif command == 0:
            print('Exit...')
            exit(1)
        else:
            if command is not None:
                command = None
                print('Wrong command. Try again')


if __name__ == '__main__':
    run()
