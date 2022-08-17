from contextlib import contextmanager, ContextDecorator
from datetime import datetime


class FileHandler:

    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        try:
            self.file = open(self.file_name, self.mode)
            return self.file
        except FileNotFoundError:
            print('File not found')

    def __exit__(self, exc_type, exc_value, exc_traceback):
        try:
            self.file.close()
        except AttributeError:
            print('Exit')


@contextmanager
def file_handler(filename, mode):
    file = open(filename, mode)
    yield file
    file.close()


class file_handler_mixin(ContextDecorator):
    def __init__(self, file_name, file_mode):
        self._file_name = file_name
        self._file_mode = file_mode
        self._file = None

    def __enter__(self):
        self._file = open(self._file_name, self._file_mode)
        self._file.write(str(datetime.now()))
        return self._file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self._file.close()


@file_handler_mixin("log.txt", "w")
def write_to_file():
    print("Writing current timestamp to file")


@contextmanager
def logger(filename, mode):
    try:
        file = open(filename, mode)
        yield file
        file.close()
    except:
        print('Some exception')


def is_even_and_gt_3(num):
    if num % 2 == 0 and num >= 3:
        return True
    elif num < 3:
        raise Exception('Number is less than 3')
    elif num % 2 != 0:
        raise Exception('Number is not even')
    else:
        raise Exception('Something went wrong')


class MySquareIterator:
    def __init__(self, lst):
        self.lst = lst
        self.n = len(lst) + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.n -= 1
        if self.n == 0:
            raise StopIteration
        else:
            return self.lst[-self.n] ** 2


def endless_generator():
    n = 1
    while True:
        yield n
        n += 2


def endless_fib_generator():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b


def g1():
    yield 1
    yield 3


def g2():
    yield 2
    yield 4


def your_generator(g1, g2):
    for i in g1:
        yield i
    for i in g2:
        yield i


if __name__ == "__main__":
    # Task 7.1
    with FileHandler('test.txt', 'w') as f:
        f.write('test')

    with FileHandler('test1.txt', 'r') as f:
        if f is not None:
            print(f.read())

    with FileHandler('test.txt', 'r') as f:
        print(f.read())

    # Task 7.2
    with file_handler("test2.txt", "w") as f:
        f.write("Test2")

    # Task 7.3
    write_to_file()

    # Task 7.4
    with logger('log1.txt', 'w') as f:
        f.write('log')

    # Task 7.5
    print(is_even_and_gt_3(4))
    # print(is_even_and_gt_3(5))
    # print(is_even_and_gt_3(2))

    # Task 7.6
    lst = [1, 2, 3, 4, 5]
    itr = MySquareIterator(lst)
    for item in itr:
        print(item)

    # Task 7.7
    # gen = endless_generator()
    # while True:
    #     print(next(gen))

    # Task 7.8
    # gen = endless_fib_generator()
    # while True:
    #     print(next(gen))

    # Task 7.9
    g1 = g1()
    g2 = g2()
    # print(next(g1))
    # print(next(g1))
    # print(next(g2))
    # print(next(g2))
    for i in your_generator(g1, g2):
        print(i)
