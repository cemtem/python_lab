import collections
import functools
import math
import operator
import string
from typing import Iterable, List


def intersect(*args: Iterable):
    return set.intersection(*map(set, args))


def union(*args: Iterable):
    return set.union(*map(set, args))


def to_int(string: str):
    res = ''
    for char in string:
        res += str(ord(char))
    return int(res)


def replacer(string: str):
    res = ''
    for char in string:
        if char == '\'':
            res += '\"'
        elif char == '\"':
            res += '\''
        else:
            res += char
    return res


def palindrome(string: str):
    for x in range(0, math.ceil(len(string) / 2)):
        eq = string[x] == string[(x + 1) * -1]
        if not eq:
            return eq
    return True


def not_split(string: str, sep=None):
    if sep == '':
        raise ValueError('empty separator')

    res = []
    start = 0
    while string.find(sep, start + 1) != -1:
        end = string.find(sep, string.find(sep, start + 1))
        res.append(string[start:end].replace(sep, ''))
        start = string.find(sep, start + 1)
    res.append(string[start:].replace(sep, ''))
    return res


def not_split2(string: str, sep=None):
    if sep == '':
        raise ValueError('empty separator')

    res = []
    start = 0
    while string.find(sep, start) != -1:
        left = string[start:string.find(sep, start)]
        string = string[string.find(sep, start):].replace(sep, '', 1)
        res.append(left)

    res.append(string[start:])
    return res


def split_by_index(s: str, indexes: List[int]):
    res = []
    prev = 0
    index = 0
    for index in indexes:
        left = s[prev:index]
        res.append(left)
        prev = index

    if index < len(s):
        res.append(s[index:])

    return res


def get_digits(number: int):
    res = ()
    for integer in str(number):
        res += (int(integer),)
    return res


def get_longest_word(string: str):
    list_of_words = string.split()
    longest_word = max(list_of_words, key=lambda x: len(x))
    return longest_word


def foo(integers: List[int]):
    res = []

    for integer in integers:
        res.append(math.prod(integers) / integer)

    return res


def get_pairs(lst: List):
    index = 0
    tupl = ()
    res = []
    if len(lst) == 1:
        return None
    while index < len(lst):
        if len(tupl) < 2:
            tupl += (lst[index],)
            index += 1
        else:
            res.append(tupl)
            tupl = ()
            index -= 1
    res.append(tupl)
    return res


def task_3_10_1(*strings):
    return sorted(set.intersection(*map(set, strings)))


def task_3_10_2(*strings):
    return sorted(set.union(*map(set, strings)))


def task_3_10_3(*strings):
    res = []
    for item in strings:
        res += set(item)

    return sorted([item for item, count in collections.Counter(res).items() if count > 1])


def task_3_10_4(*strings):
    return sorted(set(string.ascii_lowercase).difference(set.union(*map(set, strings))))


def generate_squares(num: int):
    return {i: pow(i, 2) for i in range(1, num + 1)}


def combine_dicts(*args):
    return dict(functools.reduce(operator.add, map(collections.Counter, args)))


def merge_dicts(dict1, dict2):
    res = {}
    for k, v in dict1.items():
        res[k] = v
    for k, v in dict2.items():
        if k in res:
            res[k] = res[k] | v
        else:
            res[k] = v

    return res


if __name__ == '__main__':
    # Task 3.0
    print(intersect([1, 2, 3], (1, 4)))
    print(union([1, 2, 3], (1, 4)))

    # Task 3.1
    print(to_int('abcd'))

    # Task 3.2
    print(replacer("\"hmhmhmh\' \'sdsdsd\""))

    # Task 3.3
    print(palindrome('madam'))
    print(palindrome('rotor'))
    print(palindrome('radar'))
    print(palindrome('racecar'))

    # Task 3.4
    print(not_split2('string/string', '/'))
    print('string/string'.split('/'))
    print(not_split2('test,case,test,case', ','))
    print('test,case,test,case'.split(','))
    print(not_split2('test', 'test'))
    print('test'.split('test'))
    print(not_split2('test', ' '))
    print('test'.split(' '))
    print(not_split2('test', 'es'))
    print('test'.split('es'))
    print(not_split2('test', 't'))
    print('test'.split('t'))

    # Task 3.5
    print(split_by_index('test', [1, 2, 3, 4]))
    print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
    print(split_by_index("no luck", [42]))

    # Task 3.6
    print(get_digits(87178291199))

    # Task 3.7
    print(get_longest_word('Python is simple and effective!'))
    print(get_longest_word('Any pythonista like namespaces a lot.'))

    # Task 3.8
    print(foo([1, 2, 3, 4, 5]))
    print(foo([3, 2, 1]))

    # Task 3.9
    print(get_pairs(['need', 'to', 'sleep', 'more']))
    print(get_pairs([1, 2, 3, 8, 9]))
    print(get_pairs([1]))

    # Task 3.10
    test_strings = ["hello", "world", "python", ]
    print(task_3_10_1(*test_strings))
    print(task_3_10_2(*test_strings))
    print(task_3_10_3(*test_strings))
    print(task_3_10_4(*test_strings))

    # Task 3.11
    print(generate_squares(5))

    # Task 3.12
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}

    print(combine_dicts(dict_1, dict_2))
    print(combine_dicts(dict_1, dict_2, dict_3))

    # Task 3.13
    dict_1 = {"a": {"b": "c"}}
    dict_2 = {"a": {"e": "d"}, "b": {"1": "2"}}
    print(merge_dicts(dict_1, dict_2))
