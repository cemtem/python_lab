from typing import Iterable


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


def write_number(book, name, numbers):
    book[name] = numbers
    print('Added ' + str(name) + ' with numbers ' + str(numbers))


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
            raise Exception('Wrong command. Try again')

        if command == 1:
            print('Add phone number and name')

            cmd = int(input('1 - import via file'
                            '\n2 - import via console\n'))

            if cmd == 1:
                filename = input('Enter file name: ')
                try:
                    file = open(filename)
                except FileNotFoundError:
                    raise Exception("There is no file with name " + filename)
                content = file.read()
                start = content.find('{')
                end = content.find('}')
                numbers = content[start + 1:end].split(',')
                for item in numbers:
                    pairs = item.split(':')
                    try:
                        name = pairs[0].strip()
                        list_numbers = pairs[1].split(' ')
                    except IndexError:
                        raise Exception('Wrong format of file. Please use {name:number number....}')
                    write_number(book, name, list_numbers)

            elif cmd == 2:
                name = input('Name: ')
                phone_numbers = input('Phone numbers separated by blanks: ')
                list_numbers = phone_numbers.split(" ")
                write_number(book, name, list_numbers)

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
                raise Exception('Wrong command. Try again')


class MyNumberCollection:
    lst = []

    def append(self, other):
        self.__add__(other)

    def __init__(self, *args):
        if len(args) == 3:
            self.start = args[0]
            self.end = args[1]
            self.step = args[2]

            for i in range(self.start, self.end, self.step):
                self.lst.append(i)

            if self.lst[-1] != self.end:
                self.lst.append(self.end)
        elif len(args) == 1:
            for i in args[0]:
                if type(i) is not int:
                    raise TypeError('MyNumberCollection supports only numbers')

            self.lst = list(args[0])
            self.start = self.lst[0]
            self.end = self.lst[-1]
        self.n = len(self.lst)

    def __str__(self):
        return str(self.lst)

    def __add__(self, other):

        if type(other) is MyNumberCollection:
            return self.lst + other.lst
        elif issubclass(type(other), Iterable):
            for i in other:
                if type(i) is not int:
                    raise TypeError(str(i) + ' object is not a number!')
        elif type(other) is not int:
            raise TypeError(str(other) + ' object is not a number!')
        return self.lst.append(other)

    def __getitem__(self, item):
        return self.lst[item] ** 2

    def __iter__(self):
        self.c = 0
        return self

    def __next__(self):
        if self.n < 0:
            raise StopIteration
        else:
            self.n -= 1
            res = self.lst[self.c]
            self.c += 1
            return res


if __name__ == '__main__':
    # Task 1
    # run()

    # Task 2
    col1 = MyNumberCollection(0, 5, 2)
    print(col1)

    col2 = MyNumberCollection((1, 2, 3, 4, 5))
    print(col2)

    # col3 = MyNumberCollection((1, 2, 3, "4", 5))

    col1.append(7)
    print(col1)

    # col2.append("string")
    # print(col2)

    print(col1 + col2)

    print(col1)

    print(col2)

    print(col2[4])

    for item in col1:
        print(item)
