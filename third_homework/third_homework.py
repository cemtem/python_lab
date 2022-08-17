import os
from collections import Counter
import pandas as pd


def sort_names():
    f = open('files/unsorted_names.txt')
    content = f.read().split()
    new_f = open('files/sorted_names.txt', mode='w')
    [new_f.write(name + '\n') for name in sorted(content)]
    f.close()


def lorem_ipsum():
    f = open('files/lorem_ipsum.txt')
    content = f.read()
    words = content.split()

    def most_common_words(words, num_of_words):
        return Counter(words).most_common(num_of_words)

    return most_common_words(words, 3)


def students():
    def get_top_performers(file_path, number_of_top_students=5):
        df = pd.read_csv(file_path)
        df.columns = ['Name', 'Age', 'Avg_mark']
        return df.nlargest(number_of_top_students, 'Avg_mark')

    print(get_top_performers('files/students.csv', 5))

    def desc_students(file_path):
        df = pd.read_csv(file_path)
        df.columns = ['Name', 'Age', 'Avg_mark']
        return df.sort_values('Age', ascending=False)

    desc_students('files/students.csv').to_csv('desc_students.csv')


def find_duplicates(path: str):
    contents = {}
    res = {}
    directory = os.listdir(path)
    for file in directory:
        f = open(path + '\\' + file)
        content = f.read()
        contents[file] = content

    for key, value in contents.items():
        res.setdefault(value, set()).add(key)

    return [values for key, values in res.items()
            if len(values) > 1]


prev_res = []


def remember_result(f):
    def wrapper(*args, **kwargs):
        global prev_res
        print('Last result = ' + str(prev_res))
        res = f(*args, **kwargs)
        prev_res = res
        return res

    return wrapper


@remember_result
def sum_list(*args):
    result = ''
    for item in args:
        if type(item) == int:
            if type(result) != int:
                result = 0
            result += item
        else:
            result += item
    print(f"Current result = '{result}'")
    return result


cache = 0


def call_once(f):
    def wrapper(*args):
        global cache
        if cache == 0:
            cache = f(*args)
        return cache

    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


def validate(low_bound, upper_bound):
    def parametrized_validate(f):
        def wrapper(*args):
            if args[0][2] < low_bound or args[0][2] > upper_bound:
                print("Function call is no valid!")
                return
            else:
                return f(args)

        return wrapper

    return parametrized_validate


@validate(low_bound=0, upper_bound=256)
def set_pixel(pixel_values):
    print("Pixel created!")


if __name__ == '__main__':
    # Task 4.1
    sort_names()

    # Task 4.2
    print(lorem_ipsum())

    # Task 4.3
    students()

    # Task 4.4
    print('Similar files: ' + str(find_duplicates('C:\Projects\learning\laba\\third_homework\\files')))

    # Task 4.5
    sum_list("a", "b")
    sum_list("abc", "cde")
    sum_list(3, 4, 5)

    # Task 4.6
    print(sum_of_numbers(13, 42))
    print(sum_of_numbers(999, 100))
    print(sum_of_numbers(134, 412))
    print(sum_of_numbers(856, 232))

    # Task 4.7
    set_pixel((0, 127, 300))
    set_pixel((0, 127, 250))
